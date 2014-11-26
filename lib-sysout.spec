Name:           lib-sysout
Version:        1.0.0
Release:        1%{?dist}
Summary:        lib-sysout
License:        XXX
URL:            XXX
BuildArch:      noarch

Source0:        SystemOutputter.java
Source1:        MANIFEST.MF

BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  apache-commons-io

%description
lib-sysout

%prep
%setup -qcT
%mvn_file : %{name}

%build
javac -d . -cp $(build-classpath commons-io) %{SOURCE0}
jar cfm sysout.jar %{SOURCE1} org
%mvn_artifact sysout:sysout:%{version} sysout.jar

%install
%mvn_install

%files -f .mfiles

%changelog
* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-1
- Initial packaging
