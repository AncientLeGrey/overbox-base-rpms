Summary: Creates the Vagrant user
Name: vagrant-boxification
Version: 0.0.1
Release: %(echo ${BUILD_NUMBER:-1})
License: MIT
Group: Development/Tools
URL: http://vagrantup.com/
Source: https://github.com/mitchellh/vagrant/raw/master/keys/vagrant.pub
Distribution: Centos 5
Packager: https://github.com/AncientLeGrey
Vendor: AncientLeGrey
BuildArch: noarch
BuildRoot: %{_topdir}/tmp

Requires: sed
Requires: sudo
Requires: grep
Requires: which
Requires: rvm-ruby
Requires: vboxadditions

%define rubie ruby-1.8.7
%define vagrant_user vagrant
%define vagrant_password vagrant

%description
Install this rpm to turn a virtual machine into a vagrant box.
- Installs ruby-1.8.7 via rvm
- Creates vagrant user (sudoer!)
  Login with https://github.com/mitchellh/vagrant/tree/master/keys
- Installs chef an puppet
- Pulls in dependencies needen by vagrant

%prep
%setup -c -T

%install
install -D %{SOURCE0} %{buildroot}/home/%{vagrant_user}/.ssh/authorized_keys

%clean
rm -Rf %{buildroot}

%pre
gpasswd -a root rvm
groupadd admin
useradd -G admin,rvm %{vagrant_user}
echo "%{vagrant_password}" | passwd --stdin %{vagrant_user}
echo 'export PATH=$PATH:/usr/sbin:/sbin' >> ~%{vagrant_user}/.bashrc
sed -i 's/Defaults    requiretty/# Defaults    requiretty/g;$a%admin  ALL=(ALL)       NOPASSWD: ALL' /etc/sudoers
rvm install %{rubie}
rvm use %{rubie} --default
rvm gem install chef puppet --no-ri --no-rdoc

%files
%defattr(755,%{vagrant_user},%{vagrant_user})
%dir /home/%{vagrant_user}/.ssh
%defattr(644,%{vagrant_user},%{vagrant_user})
/home/%{vagrant_user}/.ssh/authorized_keys

%changelog
* Fri May 29 2011 https://github.com/AncientLeGrey - 0.0.1-1
- Initial revision
