Name:           hello
Version:        0.0.1
Release:        1%{?dist}
Summary:        hello
License:        XXX
URL:            XXX
BuildArch:      noarch

# tar caf upstream.tar.xz upstream
Source0:        upstream.tar.xz

BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  lib-sysout

%description
hello

%package api
Summary:        hello-api

%description api
hello-api

%package impl
Summary:        hello-impl

%description impl
hello-impl

%prep
%setup -qn upstream
%mvn_package :hello __noinstall

%build
%mvn_build -s -j

%install
%mvn_install

%files api -f .mfiles-hello-api

%files impl -f .mfiles-hello-impl

%changelog
* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.1-1
- Initial packaging
