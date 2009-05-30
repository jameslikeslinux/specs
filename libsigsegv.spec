%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use libsigsegv_64 = libsigsegv-base.spec
%endif
%include base.inc
%use libsigsegv = libsigsegv-base.spec

Name:		libsigsegv
Version:	%{libsigsegv.version}
Summary:	Library for Handling Page Faults and Stack Overflows
License:	GPLv2
Group:		Libraries
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
URL:		http://libsigsegv.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Bruno Haible <bruno@clisp.org>
Meta(info.upstream_url):	http://libsigsegv.sourceforge.net/

%description
GNU libsigsegv is a library that allows handling page faults in a portable
way. It is used e.g. for generational garbage collectors and stack overflow
handlers. 

This package contains the shared library.

%package devel
Summary:	Headers for libsigsegv
Group:		Libraries
Requires:	%{name}

%description devel
GNU libsigsegv is a library that allows handling page faults in a portable
way. It is used e.g. for generational garbage collectors and stack overflow
handlers. 

This package contains the libsigsegv development files. 

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libsigsegv_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libsigsegv.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%libsigsegv_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libsigsegv.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libsigsegv_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libsigsegv.install -d %{name}-%{version}/%{base_arch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libsigsegv.so.0
%{_libdir}/%{_arch64}/libsigsegv.so.0.0.0
%endif
%{_libdir}/libsigsegv.so.0
%{_libdir}/libsigsegv.so.0.0.0

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libsigsegv.a
%{_libdir}/%{_arch64}/libsigsegv.la
%{_libdir}/%{_arch64}/libsigsegv.so
%endif
%{_libdir}/libsigsegv.a
%{_libdir}/libsigsegv.la
%{_libdir}/libsigsegv.so
%{_includedir}/sigsegv.h

%changelog
* Fri May 29 2009 - jlee@thestaticvoid.com
- Initial version
