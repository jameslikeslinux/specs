#
# spec file for package: libofa
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libofa_64 = libofa-base.spec
%endif
%include base.inc
%use libofa = libofa-base.spec

Name:		libofa
Version:	%{libofa.version}
Summary:	Library for Acoustic Fingerprinting
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://code.google.com/p/musicip-libofa/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:  SUNWgnu-automake-19
BuildRequires:  SUNWaconf
BuildRequires:  SUNWlibtool
BuildRequires:	SUNWbtool
BuildRequires:	SUNWggrp
BuildRequires:	SUNWfftw3
Requires:	SUNWfftw3

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		adam@musicip.com
Meta(info.upstream_url):	http://code.google.com/p/musicip-libofa/
Meta(info.classification):	org.opensolaris.category.2008:System/Multimedia Libraries

%description
LibOFA (Library Open Fingerprint Architecture) is an open-source audio
fingerprint created and provided by MusicIP (http://www.musicip.com).

This package contains the shared library.

%package devel
Summary:	Headers for libofa
Requires:	%{name}

%description devel
LibOFA (Library Open Fingerprint Architecture) is an open-source audio
fingerprint created and provided by MusicIP (http://www.musicip.com).

This package contains the libofa development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libofa_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libofa.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%libofa_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libofa.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libofa_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libofa.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libofa.so.0
%{_libdir}/%{_arch64}/libofa.so.0.0.0
%endif
%{_libdir}/libofa.so.0
%{_libdir}/libofa.so.0.0.0


%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libofa.so
%{_libdir}/%{_arch64}/libofa.la
%attr(755,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/libofa.pc
%endif
%{_libdir}/libofa.so
%{_libdir}/libofa.la
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/libofa.pc
%{_includedir}/ofa1/ofa.h

%changelog
* Thu Feb 11 2010 - jlee@thestaticvoid.com
- Initial version
