#
# spec file for package: libmpdclient
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libmpdclient_64 = libmpdclient-base.spec
%endif
%include base.inc
%use libmpdclient = libmpdclient-base.spec

Name:		libmpdclient
Version:	%{libmpdclient.version}
Summary:	MPD Client Library
License:	BSD
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://mpd.wikia.com/wiki/ClientLib:libmpdclient
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWbtool

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Max Kellermann <max@duempel.org>
Meta(info.upstream_url):	http://mpd.wikia.com/wiki/ClientLib:libmpdclient
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
A stable, documented, asynchronous API library for interfacing MPD in the C,
C++ & Objective C languages.

This package contains the shared library.

%package devel
Summary:	Headers for libmpdclient
Requires:	%{name}

%description devel
A stable, documented, asynchronous API library for interfacing MPD in the C,
C++ & Objective C languages.

This package contains the libmpdclient development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libmpdclient_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libmpdclient.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%libmpdclient_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libmpdclient.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libmpdclient_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libmpdclient.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libmpdclient.so.2.0.1
%{_libdir}/%{_arch64}/libmpdclient.so.2
%endif
%{_libdir}/libmpdclient.so.2.0.1
%{_libdir}/libmpdclient.so.2

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libmpdclient.so
%{_libdir}/%{_arch64}/libmpdclient.la
%attr(755,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/libmpdclient.pc
%endif
%{_libdir}/libmpdclient.so
%{_libdir}/libmpdclient.la
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/libmpdclient.pc
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_datadir}/doc
%{_datadir}/doc/libmpdclient
%{_includedir}/mpd

%changelog
* Tue Dec 28 2010 - jlee@thestaticvoid.com
- Initial version
