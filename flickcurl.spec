#
# spec file for package: flickcurl
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use flickcurl_64 = flickcurl-base.spec
%endif
%include base.inc
%use flickcurl = flickcurl-base.spec

Name:		flickcurl
Version:	%{flickcurl.version}
Summary:	Cross Platform Audio Library
License:	LGPLv2.1/GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://librdf.org/flickcurl/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWcurl
BuildRequires:	SUNWlxml-devel
BuildRequires:	SUNWraptor-devel
Requires:	SUNWcurl
Requires:	SUNWlxml
Requires:	SUNWraptor

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Dave Beckett <dave@dajobe.org>
Meta(info.upstream_url):	https://github.com/dajobe/flickcurl
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
Flickcurl is a C library for the Flickr API, handling creating the requests,
signing, token management, calling the API, marshalling request parameters and
decoding responses. It uses libcurl to call the REST web service and libxml2
to manipulate the XML responses. Flickcurl supports all of the API (see
Flickcurl API coverage for details) including the functions for photo/video
uploading, browsing, searching, adding and editing comments, groups, notes,
photosets, categories, activity, blogs, favorites, places, tags, machine tags,
institutions, pandas and photo/video metadata. It also includes a program
flickrdf to turn photo metadata, tags, machine tags and places into an RDF
triples description. 

This package contains the shared library.

%package devel
Summary:	Headers for flickcurl
Requires:	%{name}

%description devel
Flickcurl is a C library for the Flickr API, handling creating the requests,
signing, token management, calling the API, marshalling request parameters and
decoding responses. It uses libcurl to call the REST web service and libxml2
to manipulate the XML responses. Flickcurl supports all of the API (see
Flickcurl API coverage for details) including the functions for photo/video
uploading, browsing, searching, adding and editing comments, groups, notes,
photosets, categories, activity, blogs, favorites, places, tags, machine tags,
institutions, pandas and photo/video metadata. It also includes a program
flickrdf to turn photo metadata, tags, machine tags and places into an RDF
triples description. 

This package contains the flickcurl development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%flickcurl_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%flickcurl.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%flickcurl_64.build -d %{name}-%{version}/%{_arch64}
%endif
%flickcurl.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%flickcurl_64.install -d %{name}-%{version}/%{_arch64}
%endif
%flickcurl.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/flickcurl $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/flickrdf $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec flickcurl
ln -s ../lib/isaexec flickrdf
%endif

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/flickcurl
%{_bindir}/%{_arch64}/flickrdf
%{_libdir}/%{_arch64}/libflickcurl.so.0
%{_libdir}/%{_arch64}/libflickcurl.so.0.0.0
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/flickcurl
%{_bindir}/%{base_isa}/flickrdf
%hard %{_bindir}/flickcurl
%hard %{_bindir}/flickrdf
%else
%{_bindir}/flickcurl
%{_bindir}/flickrdf
%endif
%{_libdir}/libflickcurl.so.0
%{_libdir}/libflickcurl.so.0.0.0
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}/man1/flickcurl.1
%{_mandir}/man1/flickrdf.1


%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/flickcurl-config
%{_libdir}/%{_arch64}/libflickcurl.so
%{_libdir}/%{_arch64}/libflickcurl.la
%attr(755,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/flickcurl.pc
%endif
%{_bindir}/flickcurl-config
%{_libdir}/libflickcurl.so
%{_libdir}/libflickcurl.la
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/flickcurl.pc
%{_includedir}/flickcurl.h
%attr(755,root,sys) %dir %{_datadir}
%{_datadir}/gtk-doc/html/flickcurl
%{_mandir}/man1/flickcurl-config.1

%changelog
* Thu Mar 10 2011 - jlee@thestaticvoid.com
- Initial version
