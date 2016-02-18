%define cvosrelease %(svn info | grep URL | sed s/'.*\\/'//g)
%define releasetag %(test %{cvosrelease} = trunk && echo cvos || echo cvos%{cvosrelease})
%define release %(svn info | grep "Last Changed Rev" | sed s/'Last Changed Rev: '//g)_%{releasetag}
%define name env-modules
%define version 3.2.6
%define project modules
%define is_suse %(test -e /etc/SuSE-release && echo 1 || echo 0)

Summary: Environment Modules
Name: %{name}
Requires: cvos-config-cvos = %cvosrelease
Version: %{version}
Release: %{release}
Source: http://dev.clustervision.com/src/modules/modules-3.2.6.tar.gz
License: GPL
Group: Utilities/Shell
URL: http://modules.sourceforge.net
Packager: Martijn de Vries <martijn@clustervision.com>
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Patch0: rcfiles.patch
Patch1: default-modules.patch
AutoReq: 0

%description
The Modules package provides for the dynamic modification of a user's
environment via modulefiles.  

%package slave
Requires: cvos-config-cvos = %cvosrelease
Summary: Environment Modules initialization scripts
Group: Utilities/Shell
Requires: cvos-slave

%description slave
The Modules package provides for the dynamic modification of a user's
environment via modulefiles.

%prep
%setup -n modules-%{version}
%patch -p 1
%patch1 -p 1

%build
./configure --prefix=/cvos/local/apps/environment-modules/%{version}/ \
            --with-module-path=/cvos/local/modulefiles \
            --with-version-path=/cvos/local/apps/environment-modules/version/%{version} \
            --with-split-size=960 \
            --without-x \
            --with-tcl-inc=/usr/include \
            --with-tcl-lib=/usr/lib
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/cvos/local/apps
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/cvos/local/modulefiles
mv %{buildroot}/cvos/local/apps/environment-modules/%{version}/Modules/%{version}/modulefiles/* %{buildroot}/cvos/local/modulefiles
rmdir  %{buildroot}/cvos/local/apps/environment-modules/%{version}/Modules/%{version}/modulefiles

mv %{buildroot}/cvos/local/apps/environment-modules/%{version}/Modules/%{version}/* %{buildroot}/cvos/local/apps/environment-modules/%{version}
rm -rf %{buildroot}/cvos/local/apps/environment-modules/%{version}/Modules

ln -sf . %{buildroot}/cvos/local/apps/environment-modules/%{version}/Modules
ln -sf . %{buildroot}/cvos/local/apps/environment-modules/%{version}/default
ln -sf . %{buildroot}/cvos/local/apps/environment-modules/%{version}/%{version}

%if ! %is_suse
ln -sf share/man %{buildroot}/cvos/local/apps/environment-modules/%{version}/man
%endif
mkdir -p %{buildroot}/etc/profile.d

cp -af rcfiles/modules.sh %{buildroot}/etc/profile.d
cp -af rcfiles/modules.csh %{buildroot}/etc/profile.d

cat etc/global/profile.modules >> %{buildroot}/etc/profile.d/modules.sh
echo "export -f module" >> %{buildroot}/etc/profile.d/modules.sh

cat etc/global/csh.modules >> %{buildroot}/etc/profile.d/modules.csh

cp -af rcfiles/bash.bashrc.local %{buildroot}/etc
cp -af rcfiles/csh.cshrc.local %{buildroot}/etc

mkdir -p %{buildroot}/cvos/shared/modulefiles
cp -a default-modules/default-* %{buildroot}/cvos/shared/modulefiles
cp -a default-modules/shared %{buildroot}/cvos/local/modulefiles

mv -f modulefiles/* %{buildroot}/cvos/local/modulefiles
rm -f %{buildroot}/cvos/local/modulefiles/module-cvs

rm -f %{buildroot}/cvos/local/modulefiles/Makefile*
rm -f %{buildroot}/cvos/local/modulefiles/*.in

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0755)
/cvos/local/apps/environment-modules
%config(noreplace) /cvos/local/modulefiles
%config(noreplace) /cvos/shared/modulefiles
%config(noreplace)/etc/profile.d/modules.csh
%config(noreplace)/etc/profile.d/modules.sh
%config(noreplace)/etc/bash.bashrc.local
%config(noreplace)/etc/csh.cshrc.local

%files slave
%defattr(-, root, root, 0755)
/cvos/local/apps/environment-modules
%config(noreplace) /cvos/local/modulefiles
%config(noreplace)/etc/profile.d/modules.csh
%config(noreplace)/etc/profile.d/modules.sh
%config(noreplace)/etc/bash.bashrc.local
%config(noreplace)/etc/csh.cshrc.local

