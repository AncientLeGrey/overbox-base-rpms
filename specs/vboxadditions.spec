Summary: VirtualBox guest additions installer
Name: vboxadditions
Version: 4.0.8
Release: %(echo ${BUILD_NUMBER:-1})
License: GPL2
Group: Applications/System
URL: http://www.virtualbox.org/
Source0: http://download.virtualbox.org/virtualbox/%{version}/VBoxGuestAdditions_%{version}.iso
Source1: %{name}/vboxinstall
Distribution: Centos 5
Packager: https://github.com/AncientLeGrey
Vendor: Oracle
BuildArch: noarch
BuildRoot: %{_topdir}/tmp

Requires: gcc
Requires: make
Requires: bzip2
Requires: kernel-devel

%description
Installs the VirtualBox guest additions
Installation is done in a first-boot-service.
So you can quickly update to the newest kernel in your kickstart file before
the guest additions are installed.
A shutdown is performed afterwards!

%prep
%setup -c -T

%install
mkdir -p %{buildroot}/opt/VBoxLinuxAdditions
sudo mount -o loop %{SOURCE0} /mnt
install -D /mnt/VBoxLinuxAdditions.run %{buildroot}/opt/VBoxLinuxAdditions/VBoxLinuxAdditions.run
sudo umount /mnt
install -D %{SOURCE1} %{buildroot}/etc/init.d/vboxinstall

%clean
rm -Rf %{buildroot}

%post
chkconfig --add vboxinstall
chkconfig vboxinstall on

%files
%defattr(755,root,root)
/opt/VBoxLinuxAdditions/VBoxLinuxAdditions.run
/etc/init.d/vboxinstall

%changelog
* Fri May 29 2011 https://github.com/AncientLeGrey - 4.0.8-1
- Initial revision
