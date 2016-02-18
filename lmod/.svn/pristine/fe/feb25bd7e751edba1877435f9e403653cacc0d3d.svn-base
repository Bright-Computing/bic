%define cmrelease %(svn info | grep ^URL | sed s/'.*\\/'//g)
%define releasetag %(test %{cmrelease} = trunk && echo cm || echo cm%{cmrelease})
%define release %(svn info | grep "Last Changed Rev" | sed s/'Last Changed Rev: '//g)_%{releasetag}
%define name env-modules
%define version 3.2.10
%define project modules
%define is_suse %(test -e /etc/SuSE-release && echo 1 || echo 0)
%define debug_package     %{nil}

Summary: Environment Modules
Name: %{name}
Vendor: modules project
Requires: cm-config-cm = %cmrelease
Provides: environment-modules
Version: %{version}
Release: %{release}
Source: http://dev.bright.office/src/modules/modules-3.2.10.tar.gz
License: GPL
Group: Utilities/Shell
URL: http://modules.sourceforge.net
Packager: Martijn de Vries <martijn.devries@brightcomputing.com>
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Patch0: rcfiles.patch
Patch1: default-modules.patch
AutoReq: 0

%description
The Modules package provides for the dynamic modification of a user's
environment via modulefiles.  

%package slave
Requires: cm-config-cm = %cmrelease
Provides: environment-modules
Summary: Environment Modules initialization scripts
Group: Utilities/Shell
Requires: cm-slave

%description slave
The Modules package provides for the dynamic modification of a user's
environment via modulefiles.

%prep
%setup -n modules-%{version}
%patch0 -p 1
%patch1 -p 1

%build
CPPFLAGS="-DUSE_INTERP_ERRORLINE" \
./configure --prefix=/cm/local/apps/environment-modules/%{version}/ \
            --with-module-path=/cm/local/modulefiles \
            --with-version-path=/cm/local/apps/environment-modules/version/%{version} \
            --with-split-size=960 \
            --without-x \
            --with-tcl-inc=/usr/include \
            --with-tcl-lib=/usr/lib
make
sed -i -e "s/__VERSION__/%{version}/g" rcfiles/modules.*sh

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/cm/local/apps
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/cm/local/modulefiles
mv %{buildroot}/cm/local/apps/environment-modules/%{version}/Modules/%{version}/modulefiles/* %{buildroot}/cm/local/modulefiles
rmdir  %{buildroot}/cm/local/apps/environment-modules/%{version}/Modules/%{version}/modulefiles

mv %{buildroot}/cm/local/apps/environment-modules/%{version}/Modules/%{version}/* %{buildroot}/cm/local/apps/environment-modules/%{version}
rm -rf %{buildroot}/cm/local/apps/environment-modules/%{version}/Modules

ln -sf . %{buildroot}/cm/local/apps/environment-modules/%{version}/Modules
ln -sf . %{buildroot}/cm/local/apps/environment-modules/%{version}/default
ln -sf . %{buildroot}/cm/local/apps/environment-modules/%{version}/%{version}

mkdir -p %{buildroot}/etc/profile.d

cp -af rcfiles/modules.sh %{buildroot}/etc/profile.d
cp -af rcfiles/modules.csh %{buildroot}/etc/profile.d

cat etc/global/profile.modules >> %{buildroot}/etc/profile.d/modules.sh
cat etc/global/csh.modules >> %{buildroot}/etc/profile.d/modules.csh

mkdir -p %{buildroot}/cm/shared/modulefiles
cp -a default-modules/default-* %{buildroot}/cm/shared/modulefiles
cp -a default-modules/shared %{buildroot}/cm/local/modulefiles

mv -f modulefiles/* %{buildroot}/cm/local/modulefiles
rm -f %{buildroot}/cm/local/modulefiles/module-cvs
rm -f %{buildroot}/cm/local/modulefiles/modules

rm -f %{buildroot}/cm/local/modulefiles/Makefile*
rm -f %{buildroot}/cm/local/modulefiles/*.in

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/SuSE-release ];
then if ! grep -q ^module /etc/skel/.bashrc; then echo "module load null" >> /etc/skel/.bashrc; fi
else if ! grep -q ^module /etc/skel/.bashrc; then echo "module load gcc" >> /etc/skel/.bashrc; fi
fi
rm -f /cm/local/apps/environment-modules/current
ln -s %{version} /cm/local/apps/environment-modules/current

%post slave
rm -f /cm/local/apps/environment-modules/current
ln -s %{version} /cm/local/apps/environment-modules/current

%files
%defattr(-, root, root, 0755)
/cm/local/apps/environment-modules
%config(noreplace) /cm/local/modulefiles
%config(noreplace) /cm/shared/modulefiles
%config(noreplace)/etc/profile.d/modules.csh
%config(noreplace)/etc/profile.d/modules.sh

%files slave
%defattr(-, root, root, 0755)
/cm/local/apps/environment-modules
%config(noreplace) /cm/local/modulefiles
%config(noreplace)/etc/profile.d/modules.csh
%config(noreplace)/etc/profile.d/modules.sh
