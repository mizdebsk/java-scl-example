%global pkg_name lib-sysout
%{?scl:%scl_package %{pkg_name}}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.0.0
Release:        4.1%{?dist}
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
%{?scl:scl enable %{scl} - <<"EOF"}
%mvn_file : %{pkg_name}

echo "<project><modelVersion>4.0.0</modelVersion><groupId>sysout</groupId><artifactId>sysout</artifactId><version>%{version}</version></project>" >pom.xml
%pom_add_dep commons-io:commons-io
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
javac -source 1.5 -target 1.5 -d . -cp $(build-classpath commons-io) %{SOURCE0}
jar cfm sysout.jar %{SOURCE1} org
%mvn_artifact pom.xml sysout.jar
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles

%changelog
* Thu Nov 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-4.1
- SCL-ize package

* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-3
- Set compiler source/target to 1.5

* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-2
- Add Maven POM

* Wed Nov 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-1
- Initial packaging
