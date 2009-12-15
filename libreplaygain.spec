#
# spec file for package: libreplaygain
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libreplaygain_64 = libreplaygain-base.spec
%endif
%include base.inc
%use libreplaygain = libreplaygain-base.spec

Name:		libreplaygain
Version:	%{libreplaygain.version}
Summary:	Replay Gain Library
License:	LGPLv2.1
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.musepack.net/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWbtool
BuildRequires:	SUNWgnu-automake-19
BuildRequires:	SUNWaconf
BuildRequires:	SUNWlibtool
BuildRequires:	SUNWggrp

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Glen Sawyer <mp3gain@hotmail.com>
Meta(info.upstream_url):	http://www.musepack.net/
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
Replay Gain library from Musepack.

This package contains the shared library.

%package devel
Summary:	Headers for libreplaygain
Requires:	%{name}

%description devel
Replay Gain library from Musepack.

This package contains the libreplaygain development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libreplaygain_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libreplaygain.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%libreplaygain_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libreplaygain.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libreplaygain_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libreplaygain.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libreplaygain.so.1.0.0
%{_libdir}/%{_arch64}/libreplaygain.so.1
%endif
%{_libdir}/libreplaygain.so.1.0.0
%{_libdir}/libreplaygain.so.1

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libreplaygain.so
%{_libdir}/%{_arch64}/libreplaygain.la
%endif
%{_libdir}/libreplaygain.so
%{_libdir}/libreplaygain.la
%{_includedir}/replaygain/gain_analysis.h

%changelog
* Fri Nov 27 2009 - jlee@thestaticvoid.com
- Initial version
