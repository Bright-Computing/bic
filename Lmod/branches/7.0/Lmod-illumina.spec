%define cmrelease       7.0 
%define release         cm7.0
%define name            Lmod
%define version         6.3.1
%define debug_package   %{nil}

%define rhel6_based %(test -e /etc/redhat-release && grep -q -E '(CentOS|Red Hat Enterprise Linux Server|Scientific Linux) release 6' /etc/redhat-release && echo 1 || echo 0)
%define rhel7_based %(test -e /etc/os-release && source /etc/os-release && echo "${ID}  ${VERSION_ID}" | grep -q -E "^(rhel|centos)  7" && echo 1 || echo 0)
%define sles11      %(test -e /etc/SuSE-release && test $(awk '$1=="VERSION"{printf $3}' /etc/SuSE-release) = "11" && echo 1 || echo 0)
%define sles12      %(test -e /etc/os-release && source /etc/os-release && echo "${ID}  ${VERSION_ID}" | grep -q "^sles  12" && echo 1 || echo 0)
                
%define git_rev     %(git rev-list --count --first-parent HEAD)
%define git_tag     %(git describe --always)
%define lmod_upstream_gitid git-669af9b

%if %{rhel6_based}
%define release %{git_rev}_%{git_tag}_cm%{cmrelease}_el6
%endif

%if %{rhel7_based}
%define release %{git_rev}_%{git_tag}_cm%{cmrelease}_el7
%endif

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Environmental Modules System in Lua
Group:          Utilities/Shell
License:        MIT and LGPLv2
URL:            https://www.tacc.utexas.edu/tacc-projects/lmod
Source0:        https://github.com/TACC/%{name}/archive/%{version}.tar.gz
Packager:       Fotis/Johnny (Illumina/Bright Computing)
BuildArch:      noarch
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  lua-filesystem
BuildRequires:  lua-json
BuildRequires:  lua-posix
BuildRequires:  lua-term
Requires:       lua
Requires:       lua-filesystem
Requires:       lua-json
Requires:       lua-posix
Requires:       lua-term
Requires:       cm-config-cm = %cmrelease
Provides:       environment(modules)
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
Lmod is a Lua based module system that easily handles the MODULEPATH
Hierarchical problem.  Environment Modules provide a convenient way to
dynamically change the users' environment through modulefiles. This includes
easily adding or removing directories to the PATH environment variable.
Modulefiles for library packages provide environment variables that specify
where the library and header files can be found.


%prep
%setup -q
sed -i -e 's,/usr/bin/env ,/usr/bin/,' src/*.tcl
# Remove bundled lua-term
rm -r pkgs tools/json.lua
#sed -i -e 's, pkgs , ,' Makefile.in
# Remove unneeded shbangs
sed -i -e '/^#!/d' init/*.in


%build
%configure --prefix=%{_datadir}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
# init scripts are sourced
chmod -x %{buildroot}%{_datadir}/lmod/%{version}/init/*
mkdir -p %{buildroot}%{_sysconfdir}/modulefiles
mkdir -p %{buildroot}%{_datadir}/modulefiles
mkdir -p %{buildroot}%{_sysconfdir}/profile.d

ln -s %{_datadir}/lmod/lmod/init/profile %{buildroot}%{_sysconfdir}/profile.d/z00_lmod.sh
ln -s %{_datadir}/lmod/lmod/init/cshrc %{buildroot}%{_sysconfdir}/profile.d/z00_lmod.csh
# install -Dpm 644 %{SOURCE1} %{buildroot}/%{macrosdir}/macros.%{name}

%if %{sles11}
# For sles11 /usr/bin/lua is not in the rpm file list, its created with the alternatives-update command in the post section of the lua package.
#  /usr/bin/lua5.1 is provided by lua rpm.
for FILE in `find ${RPM_BUILD_ROOT}%{_datadir} -type f`; do
  sed -i '1!b;s%^#\!/usr/bin/lua%#\!/usr/bin/lua5.1%' ${FILE}
done
%endif

# Fix @gitid@ bug in upstream version
sed -i 's/local s = "@git@"/local s = "(%{lmod_upstream_gitid})"/g' %{buildroot}/usr/share/lmod/%{version}/libexec/Version.lua
sed -i 's/local s = "@git@"/local s = "(%{lmod_upstream_gitid})"/g' %{buildroot}/usr/share/lmod/%{version}/settarg/Version.lua


%clean
rm -rf $RPM_BUILD_ROOT

# the conditional structure of the post-Install directive of this .spec, turns it into a non-idempotent caase;
# This aspect becomes important if we have other RPMs providing any of files /etc/profile.d/00-modulepath.*sh
%post
SETMODULEPATH_SH="no" 
SETMODULEPATH_CSH="no" 
if [ ! -f /etc/profile.d/00-modulepath.sh ]; then
  SETMODULEPATH_SH="yes"
fi

if [ ! -f /etc/profile.d/00-modulepath.csh ]; then
  SETMODULEPATH_CSH="yes"
fi

if [ $SETMODULEPATH_SH == "yes" ];then
  echo 'export MODULEPATH=/etc/modulefiles:/usr/share/modulefiles:/usr/share/Modules/modulefiles' > /etc/profile.d/00-modulepath.sh
fi
if [ $SETMODULEPATH_CSH == "yes" ];then
  echo 'setenv MODULEPATH=/etc/modulefiles:/usr/share/modulefiles:/usr/share/Modules/modulefiles' > /etc/profile.d/00-modulepath.csh
fi

%files
%doc INSTALL License README README_lua_modulefiles.txt
%{_sysconfdir}/modulefiles
%{_sysconfdir}/profile.d/z00_lmod.csh
%{_sysconfdir}/profile.d/z00_lmod.sh
%{_datadir}/lmod
%{_datadir}/modulefiles
# %{macrosdir}/macros.%{name}

