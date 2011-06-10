Summary: Cantiere helper tasks to build RPM from .spec files
Name: cantiere
Version: 1.0.0.Beta1+1.c4bb9a7
Release: %(echo ${BUILD_NUMBER:-1})
License: LGPL
Group: Development/Tools
URL: https://github.com/stormgrind/cantiere
Source: https://github.com/stormgrind/cantiere/tarball/f9cfc5b
Patch: https://github.com/AncientLeGrey/cantiere/compare/f9cfc5b...c4bb9a7.patch
Distribution: Centos 5
Packager: https://github.com/AncientLeGrey
Vendor: http://www.jboss.org/stormgrind
BuildArch: noarch
BuildRoot: %{_topdir}/tmp

Requires: rpm-build
Requires: repoview >= 0.6.5
Requires: createrepo

%define target /usr/lib/%{name}

%description
Cantiere helper tasks to build RPM from .spec files

%prep
%setup -n stormgrind-cantiere-f9cfc5b
%patch -p1

%install
install -d %{buildroot}/%{target}
chmod -x extras/sign-rpms
cp -R * %{buildroot}/%{target}

%clean
rm -Rf %{buildroot}

%files
%{target}

%changelog
* Fri Jun 10 2011 https://github.com/AncientLeGrey - 1.0.0.Beta1+1.c4bb9a7-1
- Adjust version number to make yum happy
* Fri Jun 10 2011 https://github.com/AncientLeGrey - 1.0.0.Beta1+c4bb9a7-1
- Include patches f9cfc5b...c4bb9a7, Requires repoview
* Fri May 29 2011 https://github.com/AncientLeGrey - 1.0.0.Beta1+f9cfc5b-1
- Initial revision
