#
# spec file for package: libshout
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libshout_64 = libshout-base.spec
%endif
%include base.inc
%use libshout = libshout-base.spec

Name:		libshout
Version:	%{libshout.version}
Summary:	MP3/Ogg Vorbis Broadcast Streaming Library 
License:	LGPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.icecast.org/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWgnu-automake-19
BuildRequires:	SUNWaconf
BuildRequires:	SUNWlibtool
BuildRequires:	SUNWogg-vorbis-devel
Requires:	SUNWogg-vorbis

# Solaris doesn't package 64-bit versions of the following libraries
#BuildRequires:	SUNWlibtheora
#BuildRequires:	SUNWspeex
#Requires:	SUNWlibtheora
#Requires:	SUNWspeex

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Icecast Team <team@icecast.org>
Meta(info.upstream_url):	http://www.icecast.org/
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
A library for communicating with and sending data to Icecast and Icecast 2
streaming audio servers. It handles the socket connection, the timing of the
data transmission, and prevents bad data from getting to the server. 

This package contains the shared library.

%package devel
Summary:	Headers for libshout
Requires:	%{name}

%description devel
A library for communicating with and sending data to Icecast and Icecast 2
streaming audio servers. It handles the socket connection, the timing of the
data transmission, and prevents bad data from getting to the server. 

This package contains the libshout development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libshout_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libshout.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%libshout_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libshout.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libshout_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libshout.install -d %{name}-%{version}/%{base_arch}

# remove empty bin directory
rm -rf $RPM_BUILD_ROOT%{_bindir}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libshout.so.3
%{_libdir}/%{_arch64}/libshout.so.3.2.0
%endif
%{_libdir}/libshout.so.3
%{_libdir}/libshout.so.3.2.0

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libshout.la
%{_libdir}/%{_arch64}/libshout.so
%attr(755,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/shout.pc
%endif
%{_libdir}/libshout.la
%{_libdir}/libshout.so
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/shout.pc
%{_includedir}/shout/shout.h
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_docdir}
%{_docdir}/libshout/README
%{_docdir}/libshout/example.c
%{_docdir}/libshout/COPYING
%{_docdir}/libshout/nonblocking.c
%{_docdir}/libshout/NEWS
%attr(755,root,other) %dir %{_datadir}/aclocal
%{_datadir}/aclocal/shout.m4

%changelog
* Sun Nov 29 2009 - jlee@thestaticvoid.com
- Initial version
