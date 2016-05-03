%define cmrelease       7.0 
%define release         cm7.0
%define name            Lmod-site-config
%define version         6.3.1
%define debug_package   %{nil}

%define rhel6_based %(test -e /etc/redhat-release && grep -q -E '(CentOS|Red Hat Enterprise Linux Server|Scientific Linux) release 6' /etc/redhat-release && echo 1 || echo 0)
%define rhel7_based %(test -e /etc/os-release && source /etc/os-release && echo "${ID}  ${VERSION_ID}" | grep -q -E "^(rhel|centos)  7" && echo 1 || echo 0)
%define sles11      %(test -e /etc/SuSE-release && test $(awk '$1=="VERSION"{printf $3}' /etc/SuSE-release) = "11" && echo 1 || echo 0)
%define sles12      %(test -e /etc/os-release && source /etc/os-release && echo "${ID}  ${VERSION_ID}" | grep -q "^sles  12" && echo 1 || echo 0)
                
%define git_rev     %(git rev-list --count --first-parent HEAD)
%define git_tag     %(git describe --always)
%define lmod_upstream_gitid git-1921f91

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
Source0:        %{name}-%{cmrelease}.tar.gz
Packager:       Fotis/Johnny (Illumina/Bright Computing)
BuildArch:      noarch
Requires:       cm-config-cm = %cmrelease
Provides:       environment(modules)
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
This package provides the default site configuraion for Lmod.

%prep
%setup -c  %{name}-%{version}-%{cmrelease}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
pwd
ls
install -m 700 %{name}-%{version}-%{cmrelease}/00-user_is_root.sh %{buildroot}/%{_sysconfdir}/profile.d/00-user_is_root.sh
install -m 700 %{name}-%{version}-%{cmrelease}/z01-default_modules.sh %{buildroot}/%{_sysconfdir}/profile.d/z01-default_modules.sh
install -m 700 %{name}-%{version}-%{cmrelease}/z01-default_modules.csh %{buildroot}/%{_sysconfdir}/profile.d/z01-default_modules.csh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config(noreplace) %attr(700, root, root) /etc/profile.d/00-user_is_root.sh
%config(noreplace) %attr(700, root, root) /etc/profile.d/z01-default_modules.sh
%config(noreplace) %attr(700, root, root) /etc/profile.d/z01-default_modules.csh

