%{!?scl_name_base:%global scl_name_base welcome}
%{!?scl_name_version:%global scl_name_version 2}
%{!?scl:%global scl %{scl_name_base}%{scl_name_version}}
%global scl_vendor mizdebsk
%scl_package %scl

Name:      %{scl_name}
Version:   1
Release:   4%{?dist}
Summary:   XXX
License:   XXX
URL:       XXX
BuildArch: noarch

BuildRequires: scl-utils
BuildRequires: javapackages-tools

# List everything in the SCL here so that installation of only the metapackage brings in
# everything we need
Requires: %{scl_name}-runtime = %{version}-%{release}

%description
Meta-package that will install everything needed to use the %{scl}
Software Collection.

%package   runtime
Summary:   Runtime scripts for the %{scl} Software Collection
Requires:  scl-utils

%description runtime
Essential runtime scripts for working with the %{scl} Software
Collection.

%package   build
Summary:   Build configuration the %{scl} Software Collection
Requires:  scl-utils-build
Requires:  %{scl_name}-runtime = %{version}-%{release}
Requires:  %{scl_prefix_greet}scldevel

%description build
Essential build configuration macros for building the %{scl}
Software Collection.

%package scldevel
Summary:    Package shipping development files for %scl
Requires:   %{scl_name}-runtime = %{version}-%{release}
Requires:   %{scl_prefix_greet}scldevel

%description scldevel
Package shipping development files, especially useful for development of
packages depending on %scl Software Collection.

%prep
%setup -q -c -T

%build
# Enable collection script
cat <<EOF >enable
. scl_source enable %{scl_greet}
# General variables
export PATH=%{_bindir}\${PATH:+:\${PATH}}
export MANPATH=%{_mandir}:\${MANPATH}
export INFOPATH=%{_infodir}\${INFOPATH:+:\${INFOPATH}}

# Needed by Java Packages Tools to locate java.conf
export JAVACONFDIRS="%{_sysconfdir}/java:\${JAVACONFDIRS:-/etc/java}"

# Required by XMvn to locate its configuration files
export XDG_CONFIG_DIRS="%{_sysconfdir}/xdg:\${XDG_CONFIG_DIRS:-/etc/xdg}"

# Required to locate shared libs inside the collection
export LD_LIBRARY_PATH="%{_prefix}/lib:%{_prefix}/lib64${LD_LIBRARY_PATH:+:\$LD_LIBRARY_PATH}"
EOF

# Java configuration
cat <<EOF >java.conf
JAVA_LIBDIR=%{_javadir}
JNI_LIBDIR=%{_jnidir}
JVM_ROOT=%{_jvmdir}
EOF

# Eclipse configuration
cat <<EOF >eclipse.conf
eclipse.root=%{_libdir}/eclipse
eclipse.dropins.noarch=%{_datadir}/eclipse/dropins
eclipse.dropins.archful=%{_libdir}/eclipse/dropins
eclipse.bundles=%{_javadir},%{_jnidir},%{_javadir}-1.8.0,%{_jnidir}-1.8.0,%{_javadir}-1.7.0,%{_jnidir}-1.7.0,%{_javadir}-1.6.0,%{_jnidir}-1.6.0,%{_javadir}-1.5.0,%{_jnidir}-1.5.0
scl.namespace=%{?scl}
scl.root=%{?_scl_root}
EOF

# XMvn configuration
cat <<EOF >configuration.xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <resolverSettings>
    <metadataRepositories>
      <repository>%{_scl_root}/usr/share/maven-metadata</repository>
    </metadataRepositories>
    <prefixes>
      <prefix>%{_scl_root}</prefix>
    </prefixes>
  </resolverSettings>
  <installerSettings>
    <metadataDir>opt/%{scl_vendor}/%{scl}/root/usr/share/maven-metadata</metadataDir>
  </installerSettings>
  <repositories>
    <repository>
      <id>%{scl}-resolve</id>
      <type>compound</type>
      <properties>
        <prefix>opt/%{scl_vendor}/%{scl}/root</prefix>
        <namespace>%{scl}</namespace>
      </properties>
      <configuration>
        <repositories>
          <repository>base-resolve</repository>
        </repositories>
      </configuration>
    </repository>
    <repository>
      <id>resolve-system</id>
      <type>compound</type>
      <properties>
        <prefix>/</prefix>
      </properties>
      <configuration>
        <repositories>
          <repository>%{scl}-resolve</repository>
          <repository>%{scl_greet}-resolve</repository>
          <repository>base-resolve</repository>
        </repositories>
      </configuration>
    </repository>
    <repository>
      <id>install</id>
      <type>compound</type>
      <properties>
        <prefix>opt/%{scl_vendor}/%{scl}/root</prefix>
        <namespace>%{scl}</namespace>
      </properties>
      <configuration>
        <repositories>
          <repository>base-install</repository>
        </repositories>
      </configuration>
    </repository>
    <repository>
      <id>install-raw-pom</id>
      <type>compound</type>
      <properties>
        <prefix>opt/%{scl_vendor}/%{scl}/root</prefix>
        <namespace>%{scl}</namespace>
      </properties>
      <configuration>
        <repositories>
          <repository>base-raw-pom</repository>
        </repositories>
      </configuration>
    </repository>
    <repository>
      <id>install-effective-pom</id>
      <type>compound</type>
      <properties>
        <prefix>opt/%{scl_vendor}/%{scl}/root</prefix>
        <namespace>%{scl}</namespace>
      </properties>
      <configuration>
        <repositories>
          <repository>base-effective-pom</repository>
        </repositories>
      </configuration>
    </repository>
  </repositories>
</configuration>
EOF

%install
%{scl_install}

cat <<EOF >%{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel
%%scl_welcome %scl
%%scl_prefix_welcome %scl_prefix
EOF

install -d -m 755 %{buildroot}%{_scl_scripts}
install -p -m 755 enable %{buildroot}%{_scl_scripts}/

install -d -m 755 %{buildroot}%{_sysconfdir}/java
install -p -m 644 java.conf %{buildroot}%{_sysconfdir}/java/
install -p -m 644 eclipse.conf %{buildroot}%{_sysconfdir}/java/

install -d -m 755 %{buildroot}%{_sysconfdir}/xdg/xmvn
install -p -m 644 configuration.xml %{buildroot}%{_sysconfdir}/xdg/xmvn/

# Misc other directories we should also own
install -d -m 755 %{buildroot}%{_jnidir}
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_javadocdir}
install -d -m 755 %{buildroot}%{_datadir}/appdata
install -d -m 755 %{buildroot}%{_datadir}/maven-effective-poms
install -d -m 755 %{buildroot}%{_datadir}/maven-fragments
install -d -m 755 %{buildroot}%{_datadir}/maven-metadata
install -d -m 755 %{buildroot}%{_datadir}/maven-poms
install -d -m 755 %{buildroot}%{_libdir}/eclipse/features
install -d -m 755 %{buildroot}%{_libdir}/eclipse/plugins
install -d -m 755 %{buildroot}%{_libdir}/eclipse/dropins
install -d -m 755 %{buildroot}%{_datadir}/eclipse/dropins

%files
# The base package is empty because it is a meta-package whose sole purpose
# is to install the whole software collection

%files runtime -f filesystem
%{scl_files}
%{_sysconfdir}
%dir %{_javadir}
%dir %{_javadocdir}
%dir %{_datadir}/appdata
%dir %{_datadir}/maven-effective-poms
%dir %{_datadir}/maven-fragments
%dir %{_datadir}/maven-metadata
%dir %{_datadir}/maven-poms
%dir %{_libdir}/eclipse
%dir %{_libdir}/eclipse/features
%dir %{_libdir}/eclipse/plugins
%dir %{_libdir}/eclipse/dropins
%dir %{_datadir}/eclipse
%dir %{_datadir}/eclipse/dropins

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

%changelog
* Thu Dec  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-4
- Install eclipse-filesystem directories

* Thu Dec  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-3
- Generate and install eclipse.conf

* Thu Nov 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-2
- Fix requires on greet1-scldevel

* Thu Nov 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-1
- Initial packaging
