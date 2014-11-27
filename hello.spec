%global pkg_name hello
%{?scl:%scl_package %{pkg_name}}

Name:           %{?scl_prefix}%{pkg_name}
Version:        0.0.1
Release:        1.1%{?dist}
Summary:        hello
License:        XXX
URL:            XXX
BuildArch:      noarch

# tar caf upstream.tar.xz upstream
Source0:        upstream.tar.xz

BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  %{?scl_prefix}lib-sysout

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
%{?scl:scl enable %{scl} - <<"EOF"}
%mvn_package :hello __noinstall
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
%mvn_build -s -j
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
%mvn_install
%{?scl:EOF}

%files api -f .mfiles-hello-api

%files impl -f .mfiles-hello-impl

%changelog
* Thu Nov 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.1-1.1
- SCL-ize package

* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.1-1
- Initial packaging
