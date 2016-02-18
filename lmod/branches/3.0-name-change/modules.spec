%define cvosrelease %(svn info | grep URL | sed s/'.*\\/'//g)
%define releasetag cvos3.0
%define release %(svn info | grep Revision | sed s/'Revision: '//g)_%{releasetag}
%define name env-modules
%define version 3.1.6
%define cvosdir /cvos/conf
%define project modules

Summary: Environment Modules
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://dev.clustervision.com/src/modules/modules-3.1.6.tar.gz
License: GPL
Group: Utilities/Shell
URL: http://modules.sourceforge.net
Packager: Martijn de Vries <martijn@clustervision.com>
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Patch: destdir.patch
Patch1: rcfiles.patch
Patch2: default-modules.patch
AutoReq: 0

%description
The Modules package provides for the dynamic modification of a user's
environment via modulefiles.  

%package slave
Summary: Environment Modules initialization scripts
Group: Utilities/Shell

%description slave
The Modules package provides for the dynamic modification of a user's
environment via modulefiles.  

%prep
%setup -n modules-%{version}
%patch -p 1
%patch1 -p 1
%patch2 -p 1

%build
./configure --prefix=/usr/local/Cluster-Apps/environment-modules-%{version}/ \
            --with-module-path=/usr/local/Cluster-Config/modulefiles \
            --with-split-size=960 \
            --without-x \
            --with-tcl-include=/usr/include \
            --with-tcl-libraries=/usr/lib
make

%install
mkdir -p %{buildroot}/usr/local/Cluster-Apps/
mkdir -p %{buildroot}/usr/local/Cluster-Config/
make DESTDIR=%{buildroot} install

ln -sf . %{buildroot}/usr/local/Cluster-Apps/environment-modules-%{version}/%{version}

cat << EOF > %{buildroot}/usr/local/Cluster-Apps/environment-modules-%{version}/init/.modulespath
/usr/local/Cluster-Apps/environment-modules-$VERSION/modulefiles
/usr/local/Cluster-Config/modulefiles
EOF

#if [ -f /etc/SuSE-release ]; then
  mkdir -p %{buildroot}%{cvosdir}/etc/profile.d
  cp -af etc/global/profile.modules %{buildroot}%{cvosdir}/etc/profile.d/modules.sh
  cp -af etc/global/csh.modules %{buildroot}%{cvosdir}/etc/profile.d/modules.csh
  cp -af rcfiles/bash.bashrc.local %{buildroot}%{cvosdir}/etc
  cp -af rcfiles/csh.cshrc.local %{buildroot}%{cvosdir}/etc
#fi

cp -a default-modules/* %{buildroot}/usr/local/Cluster-Config/modulefiles
mv -f modulefiles/* %{buildroot}/usr/local/Cluster-Config/modulefiles
rm %{buildroot}/usr/local/Cluster-Config/modulefiles/*.in

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -e %{cvosdir}/../FRESH ] ; then
  cp -f %{cvosdir}/etc/profile.d/modules.sh /etc/profile.d/modules.sh
  cp -f %{cvosdir}/etc/profile.d/modules.csh /etc/profile.d/modules.csh
  cp -f %{cvosdir}/etc/bash.bashrc.local /etc/bash.bashrc.local
  cp -f %{cvosdir}/etc/csh.cshrc.local /etc/csh.cshrc.local
else
  echo "New configfiles available for %{project} in %{cvosdir}"
fi

%post slave
if [ -e %{cvosdir}/../FRESH ] ; then
  cp -f %{cvosdir}/etc/profile.d/modules.sh /etc/profile.d/modules.sh
  cp -f %{cvosdir}/etc/profile.d/modules.csh /etc/profile.d/modules.csh
  cp -f %{cvosdir}/etc/bash.bashrc.local /etc/bash.bashrc.local
  cp -f %{cvosdir}/etc/csh.cshrc.local /etc/csh.cshrc.local
else
  echo "New configfiles available for %{project} in %{cvosdir}"
fi

%files
%defattr(-, root, root, 0755)
/usr/local/Cluster-Apps/environment-modules-%{version}
/usr/local/Cluster-Config/modulefiles
%{cvosdir}

%files slave
%defattr(-, root, root, 0755)
%{cvosdir}
