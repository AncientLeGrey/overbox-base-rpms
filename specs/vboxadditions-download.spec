Summary: VirtualBox guest additions downloader and installer
Name: vboxadditions-download
Version: 4.0.8
Release: %(echo ${BUILD_NUMBER:-1})
License: GPL2
Group: Applications/System
URL: http://www.virtualbox.org/
Source: %{name}/vboxinstall-download
Distribution: Centos 5
Packager: https://github.com/AncientLeGrey
Vendor: Oracle
BuildArch: noarch
BuildRoot: %{_topdir}/tmp

Requires: gcc
Requires: wget
Requires: make
Requires: bzip2
Requires: kernel-devel

Provides: vboxadditions

%description
Downloads and installs the VirtualBox guest additions.
Installation is done in a first-boot-service.
So you can quickly update to the newest kernel in your kickstart file before
the guest additions are installed.
A shutdown is performed afterwards!

%prep
%setup -c -T

%install
mkdir -p %{buildroot}/opt/VBoxLinuxAdditions
install -D %{SOURCE0} %{buildroot}/etc/init.d/vboxinstall-download

%clean
rm -Rf %{buildroot}

%post
chkconfig --add vboxinstall-download
chkconfig vboxinstall-download on

%files
%defattr(755,root,root)
/etc/init.d/vboxinstall-download
%dir /opt/VBoxLinuxAdditions

%changelog
* Fri May 29 2011 https://github.com/AncientLeGrey - 4.0.8-1
- Initial revision
