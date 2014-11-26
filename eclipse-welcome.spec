Name:		eclipse-welcome
Version:	2.1.3
Release:	1%{?dist}
Summary:	XXX
License:	XXX
URL:		XXX
BuildArch:      noarch

# tar caf eclipse-welcome-%{version}.tar.xz eclipse-welcome-%{version}
Source0:	eclipse-welcome-%{version}.tar.xz

BuildRequires:	tycho
BuildRequires:	hello-api
BuildRequires:	hello-impl

%description
XXX

%prep
%setup -q

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - error: line 8: Empty tag: Source0:
- Initial packaging

* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com>
- 
