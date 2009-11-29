#
# spec file for package: libmad
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libmad_64 = libmad-base.spec
%endif
%include base.inc
%use libmad = libmad-base.spec

Name:		libmad
Version:	%{libmad.version}
Summary:	MPEG Audio Decoder Library
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.underbit.com/products/mad/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWgnu-automake-19
BuildRequires:	SUNWaconf
BuildRequires:	SUNWlibtool
BuildRequires:	SUNWggrp

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Robert Leslie <rob@underbit.com>
Meta(info.upstream_url):	http://www.underbit.com/products/mad/
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1 and the
MPEG-2 extension to lower sampling frequencies, as well as the de facto MPEG
2.5 format. All three audio layers — Layer I, Layer II, and Layer III (i.e.
MP3) — are fully implemented.

This package contains the shared library.

%package devel
Summary:	Headers for libmad
Requires:	%{name}

%description devel
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1 and the
MPEG-2 extension to lower sampling frequencies, as well as the de facto MPEG
2.5 format. All three audio layers — Layer I, Layer II, and Layer III (i.e.
MP3) — are fully implemented.

This package contains the libmad development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libmad_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libmad.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%libmad_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libmad.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libmad_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libmad.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libmad.so.0
%{_libdir}/%{_arch64}/libmad.so.0.2.1
%endif
%{_libdir}/libmad.so.0
%{_libdir}/libmad.so.0.2.1

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libmad.la
%{_libdir}/%{_arch64}/libmad.so
%attr(755,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/mad.pc
%endif
%{_libdir}/libmad.la
%{_libdir}/libmad.so
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/mad.pc
%{_includedir}/mad.h

%changelog
* Sun Nov 29 2009 - jlee@thestaticvoid.com
- Initial version
