Name:           lib-sysout
Version:        1.0.0
Release:        2%{?dist}
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

echo "<project><modelVersion>4.0.0</modelVersion><groupId>sysout</groupId><artifactId>sysout</artifactId><version>%{version}</version></project>" >pom.xml
%pom_add_dep commons-io:commons-io

%build
javac -d . -cp $(build-classpath commons-io) %{SOURCE0}
jar cfm sysout.jar %{SOURCE1} org
%mvn_artifact pom.xml sysout.jar

%install
%mvn_install

%files -f .mfiles

%changelog
* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-2
- Add Maven POM

* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-1
- Initial packaging
