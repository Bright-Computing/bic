## This RPM .spec file will provide a build process for a cluster-ready Lmod: https://github.com/TACC/Lmod
## Please provide feedback about it at collaboration repo: http://github.com/plabrop/bic

%define cmrelease       7.0 
%define release         cm7.0
%define name            Lmod
%define secname         Lmod-files
%define version         7.5.4
%define debug_package   %{nil}

%define rhel6_based %(test -e /etc/redhat-release && grep -q -E '(CentOS|Red Hat Enterprise Linux Server|Scientific Linux) release 6' /etc/redhat-release && echo 1 || echo 0)
%define rhel7_based %(test -e /etc/os-release && source /etc/os-release && echo "${ID}  ${VERSION_ID}" | grep -q -E "^(rhel|centos)  7" && echo 1 || echo 0)
%define sles11      %(test -e /etc/SuSE-release && test $(awk '$1=="VERSION"{printf $3}' /etc/SuSE-release) = "11" && echo 1 || echo 0)
%define sles12      %(test -e /etc/os-release && source /etc/os-release && echo "${ID}  ${VERSION_ID}" | grep -q "^sles  12" && echo 1 || echo 0)
                
%if %{rhel7_based}
%define git_rev     %(git rev-list --count --first-parent HEAD)
%endif

%if %{rhel6_based}
%define git_rev     %(git rev-list master --first-parent | wc -l)
%endif

%define git_tag     16d6146 
%define lmod_upstream_gitid git-%{git_tag}

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
Packager:       Fotis/Johnny (illumina/Bright Computing)
BuildArch:      noarch
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  lua-filesystem
BuildRequires:  lua-json
BuildRequires:  lua-posix
BuildRequires:  lua-term
%if %{rhel6_based}
BuildRequires:  lua-bit32
Requires:  lua-bit32
%endif
Requires:       lua
Requires:       lua-filesystem
Requires:       lua-json
Requires:       lua-posix
Requires:       lua-term
###Requires:       cm-config-cm = %cmrelease  ### unhash me when all is fine
Provides:       environment(modules)
Patch0:         lmod-bash-xtrace.patch
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
# Remove unneeded shebangs
sed -i -e '/^#!/d' init/*.in
%setup -c -D -T -a 1

%patch0 -p1

%build
%configure --prefix=%{_datadir}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p %{buildroot}%{_sysconfdir}/site/lmod      ## Local lmod customizations, fi. SitePackage.lua
mkdir -p %{buildroot}%{_sysconfdir}/site/modules   ## intentionally distinct from /etc/modulefiles, for more control
mkdir -p %{buildroot}%{_sysconfdir}/site/extras    ## we insert here special configuration files etc
install -m 644 contrib/Bright/SitePackage.lua        %{buildroot}%{_sysconfdir}/site/lmod/SitePackage.lua

# init scripts are sourced
chmod -x %{buildroot}%{_datadir}/lmod/%{version}/init/*
mkdir -p %{buildroot}%{_datadir}/lmod/%{version}/templates
mkdir -p %{buildroot}%{_datadir}/modulefiles
mkdir -p %{buildroot}%{_sysconfdir}/modulefiles
mkdir -p %{buildroot}%{_sysconfdir}/profile.d

# Local business customization
install -m 644 %{secname}-%{cmrelease}/00-INIT-MODULES.sh      %{buildroot}/%{_sysconfdir}/profile.d/00-INIT-MODULES.sh
install -m 644 %{secname}-%{cmrelease}/00-INIT-MODULES.csh     %{buildroot}/%{_sysconfdir}/profile.d/00-INIT-MODULES.csh
# guarded definition of $MODULEPATH, could be overwritten above
install -m 644 %{secname}-%{cmrelease}/00-modulepath.sh        %{buildroot}/%{_sysconfdir}/profile.d/00-modulepath.sh
install -m 644 %{secname}-%{cmrelease}/00-modulepath.csh       %{buildroot}/%{_sysconfdir}/profile.d/00-modulepath.csh
# This is escape valve for user root, so that no parallel fs default modulefiles would be loaded (fi. sge)
install -m 644 %{secname}-%{cmrelease}/00-USER_IS_ROOT.sh      %{buildroot}/%{_sysconfdir}/profile.d/00-USER_IS_ROOT.sh
install -m 644 %{secname}-%{cmrelease}/00-USER_IS_ROOT.csh     %{buildroot}/%{_sysconfdir}/profile.d/00-USER_IS_ROOT.csh
# This is Lmod shell initialization; the last couple files do defaults & restores
install -m 644 %{secname}-%{cmrelease}/z00_lmod.sh             %{buildroot}/%{_sysconfdir}/profile.d/z00_lmod.sh
install -m 644 %{secname}-%{cmrelease}/z00_lmod.csh            %{buildroot}/%{_sysconfdir}/profile.d/z00_lmod.csh
install -m 644 %{secname}-%{cmrelease}/z01-default_modules.sh  %{buildroot}/%{_sysconfdir}/profile.d/z01-default_modules.sh
install -m 644 %{secname}-%{cmrelease}/z01-default_modules.csh %{buildroot}/%{_sysconfdir}/profile.d/z01-default_modules.csh
# install -Dpm 644 %{SOURCE1} %{buildroot}/%{macrosdir}/macros.%{name}

## # Install templates
## install -m 644 %{secname}-%{cmrelease}/00-INIT-MODULES.sh      %{buildroot}/%{_datadir}/lmod/%{version}/templates/00-INIT-MODULES.sh
## install -m 644 %{secname}-%{cmrelease}/00-INIT-MODULES.csh     %{buildroot}/%{_datadir}/lmod/%{version}/templates/00-INIT-MODULES.csh

# Install the contrib directory
cp -a contrib                                          %{buildroot}%{_datadir}/lmod/%{version}
cp -a contrib/use.own.eb                               %{buildroot}%{_sysconfdir}/site/modules
# this symlink ensures settarg functionality
ln -s /usr/share/lmod/lmod/modulefiles/Core/settarg    %{buildroot}%{_sysconfdir}/site/modules
# this defines coloring and where the cache lives
cp -a %{secname}-%{cmrelease}/lmodrc.lua               %{buildroot}%{_sysconfdir}/site/extras

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
%doc INSTALL License README.md README.new README_lua_modulefiles.txt
%config(noreplace) %attr(755, root, root) %{_sysconfdir}/site/modules
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/site/lmod/SitePackage.lua
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/site/extras/lmodrc.lua
%config(noreplace) %attr(755, root, root) %{_sysconfdir}/modulefiles
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/profile.d/00-INIT-MODULES.sh
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/profile.d/00-INIT-MODULES.csh
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/profile.d/00-modulepath.sh
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/profile.d/00-modulepath.csh
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/profile.d/00-USER_IS_ROOT.sh
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/profile.d/00-USER_IS_ROOT.csh
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/profile.d/z00_lmod.sh
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/profile.d/z00_lmod.csh
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/profile.d/z01-default_modules.sh
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/profile.d/z01-default_modules.csh
%{_datadir}/lmod
%{_datadir}/modulefiles
## %config(noreplace) %attr(644, root, root) %{_datadir}/lmod/%{version}/templates/00-INIT-MODULES.sh
## %config(noreplace) %attr(644, root, root) %{_datadir}/lmod/%{version}/templates/00-INIT-MODULES.csh
# %{macrosdir}/macros.%{name}
