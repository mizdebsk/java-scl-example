%global pkg_name eclipse-welcome
%{?scl:%scl_package %{pkg_name}}

Name:           %{?scl_prefix}%{pkg_name}
Version:	2.1.3
Release:	1.1%{?dist}
Summary:	XXX
License:	XXX
URL:		XXX
BuildArch:      noarch

# tar caf eclipse-welcome-%{version}.tar.xz eclipse-welcome-%{version}
Source0:	eclipse-welcome-%{version}.tar.xz

BuildRequires:	tycho
BuildRequires:	%{scl_prefix_greet}hello-api
BuildRequires:	%{scl_prefix_greet}hello-impl

%description
XXX

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
%mvn_build -j
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles

%changelog
* Thu Nov 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.3-1.1
- SCL-ize package

* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.3-1
- Initial packaging
