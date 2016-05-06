%define cmrelease       7.0 
%define release         cm7.0
%define name            Lmod
%define secname         Lmod-files
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
Source1:        Lmod-files-%{cmrelease}.tar.gz
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
%setup -c -D -T -a 1


%build
%configure --prefix=%{_datadir}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p %{buildroot}%{_sysconfdir}/site/lmod
install -m 644 contrib/SitePackage/SitePackage.lua %{buildroot}%{_sysconfdir}/site/lmod/SitePackage.lua

# init scripts are sourced
chmod -x %{buildroot}%{_datadir}/lmod/%{version}/init/*
mkdir -p %{buildroot}%{_sysconfdir}/modulefiles
mkdir -p %{buildroot}%{_datadir}/modulefiles
mkdir -p %{buildroot}%{_sysconfdir}/profile.d

install -m 700 %{secname}-%{cmrelease}/00-modulepath.sh %{buildroot}/%{_sysconfdir}/profile.d/00-modulepath.sh
install -m 700 %{secname}-%{cmrelease}/00-modulepath.csh %{buildroot}/%{_sysconfdir}/profile.d/00-modulepath.csh
install -m 700 %{secname}-%{cmrelease}/0-0-USER_IS_ROOT.sh %{buildroot}/%{_sysconfdir}/profile.d/0-0-USER_IS_ROOT.sh
install -m 700 %{secname}-%{cmrelease}/0-0-USER_IS_ROOT.csh %{buildroot}/%{_sysconfdir}/profile.d/0-0-USER_IS_ROOT.csh
install -m 700 %{secname}-%{cmrelease}/z001-default_modules.sh %{buildroot}/%{_sysconfdir}/profile.d/z001-default_modules.sh
install -m 700 %{secname}-%{cmrelease}/z001-default_modules.csh %{buildroot}/%{_sysconfdir}/profile.d/z001-default_modules.csh
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

%post

%files
%doc INSTALL License README README_lua_modulefiles.txt
%{_sysconfdir}/site/lmod/SitePackage.lua
%{_sysconfdir}/modulefiles
%{_sysconfdir}/profile.d/z00_lmod.csh
%{_sysconfdir}/profile.d/z00_lmod.sh
%config(noreplace) %attr(700, root, root) %{_sysconfdir}/profile.d/00-modulepath.sh
%config(noreplace) %attr(700, root, root) %{_sysconfdir}/profile.d/00-modulepath.csh
%config(noreplace) %attr(700, root, root) %{_sysconfdir}/profile.d/0-0-USER_IS_ROOT.sh
%config(noreplace) %attr(700, root, root) %{_sysconfdir}/profile.d/0-0-USER_IS_ROOT.csh
%config(noreplace) %attr(700, root, root) %{_sysconfdir}/profile.d/z001-default_modules.sh
%config(noreplace) %attr(700, root, root) %{_sysconfdir}/profile.d/z001-default_modules.csh
%{_datadir}/lmod
%{_datadir}/modulefiles
# %{macrosdir}/macros.%{name}

