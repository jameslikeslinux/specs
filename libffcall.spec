#
# spec file for package: libffcall
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%ifarch amd64
%define makeargs CPU=x86_64
%else
%define makeargs CPU=sparc64
%endif
%use libffcall_64 = libffcall-base.spec
%endif
%include base.inc
%define makeargs
%use libffcall = libffcall-base.spec

Name:		libffcall
Version:	%{libffcall.version}
Summary:	Foreign Function Call Libraries
License:	GPLv2
Group:		System/Libraries
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.gnu.org/software/libffcall/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Bruno Haible <bruno@clisp.org>
Meta(info.upstream_url):	http://www.gnu.org/software/libffcall/

%description
A collection of four libraries which can be used to build foreign function call
interfaces in embedded interpreters.

This package contains the shared library.

%package devel
Summary:	Headers for libffcall
Group:		Libraries
Requires:	%{name}

%description devel
A collection of four libraries which can be used to build foreign function call
interfaces in embedded interpreters.

This package contains the libffcall development files. 

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libffcall_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libffcall.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
export CC="gcc -m64"
%libffcall_64.build -d %{name}-%{version}/%{_arch64}
%endif
export CC="gcc"
%libffcall.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libffcall_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libffcall.install -d %{name}-%{version}/%{base_arch}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/libffcall
mv $RPM_BUILD_ROOT%{_datadir}/html $RPM_BUILD_ROOT%{_datadir}/doc/libffcall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libavcall.so.0
%{_libdir}/%{_arch64}/libavcall.so.0.0.0
%{_libdir}/%{_arch64}/libcallback.so.0
%{_libdir}/%{_arch64}/libcallback.so.0.0.0
%endif
%{_libdir}/libavcall.so.0
%{_libdir}/libavcall.so.0.0.0
%{_libdir}/libcallback.so.0
%{_libdir}/libcallback.so.0.0.0

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libavcall.a
%{_libdir}/%{_arch64}/libavcall.la
%{_libdir}/%{_arch64}/libavcall.so
%{_libdir}/%{_arch64}/libcallback.a
%{_libdir}/%{_arch64}/libcallback.la
%{_libdir}/%{_arch64}/libcallback.so
%{_libdir}/%{_arch64}/libtrampoline.a
%{_libdir}/%{_arch64}/libvacall.a
%endif
%{_libdir}/libavcall.a
%{_libdir}/libavcall.la
%{_libdir}/libavcall.so
%{_libdir}/libcallback.a
%{_libdir}/libcallback.la
%{_libdir}/libcallback.so
%{_libdir}/libtrampoline.a
%{_libdir}/libvacall.a
%{_includedir}/avcall.h
%{_includedir}/vacall.h
%{_includedir}/trampoline.h
%{_includedir}/vacall_r.h
%{_includedir}/trampoline_r.h
%{_includedir}/callback.h
%{_mandir}/man3/avcall.3
%{_mandir}/man3/callback.3
%{_mandir}/man3/trampoline.3
%{_mandir}/man3/trampoline_r.3
%{_mandir}/man3/vacall.3
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_datadir}/doc
%{_datadir}/doc/libffcall/html/callback.html
%{_datadir}/doc/libffcall/html/vacall.html
%{_datadir}/doc/libffcall/html/trampoline_r.html
%{_datadir}/doc/libffcall/html/trampoline.html
%{_datadir}/doc/libffcall/html/avcall.html

%changelog
* Sun May 31 2009 - jlee@thestaticvoid.com
- Add header and correct copyright
* Sat May 30 2009 - jlee@thestaticvoid.com
- export CC=gcc
* Fri May 29 2009 - jlee@thestaticvoid.com
- Initial version
