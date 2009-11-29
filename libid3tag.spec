#
# spec file for package: libid3tag
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libid3tag_64 = libid3tag-base.spec
%endif
%include base.inc
%use libid3tag = libid3tag-base.spec

Name:		libid3tag
Version:	%{libid3tag.version}
Summary:	ID3 Tag Library
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.underbit.com/products/mad/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Robert Leslie <rob@underbit.com>
Meta(info.upstream_url):	http://www.underbit.com/products/mad/
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
ID3 tag manipulation library with full support for reading ID3v1, ID3v1.1,
ID3v2.2, ID3v2.3, and ID3v2.4 tags, as well as support for writing ID3v1,
ID3v1.1, and ID3v2.4 tags.

This package contains the shared library.

%package devel
Summary:	Headers for libid3tag
Requires:	%{name}

%description devel
ID3 tag manipulation library with full support for reading ID3v1, ID3v1.1,
ID3v2.2, ID3v2.3, and ID3v2.4 tags, as well as support for writing ID3v1,
ID3v1.1, and ID3v2.4 tags.

This package contains the libid3tag development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libid3tag_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libid3tag.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%libid3tag_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libid3tag.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libid3tag_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libid3tag.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libid3tag.so.0
%{_libdir}/%{_arch64}/libid3tag.so.0.3.0
%endif
%{_libdir}/libid3tag.so.0
%{_libdir}/libid3tag.so.0.3.0

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libid3tag.la
%{_libdir}/%{_arch64}/libid3tag.so
%endif
%{_libdir}/libid3tag.la
%{_libdir}/libid3tag.so
%{_includedir}/id3tag.h

%changelog
* Sun Nov 29 2009 - jlee@thestaticvoid.com
- Initial version
