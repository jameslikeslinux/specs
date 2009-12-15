#
# spec file for package: libcuefile
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libcuefile_64 = libcuefile-base.spec
%endif
%include base.inc
%use libcuefile = libcuefile-base.spec

Name:		libcuefile
Version:	%{libcuefile.version}
Summary:	Cue File Library
License:	LGPLv2.1
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.musepack.net/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWbtool

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Svend Sorensen
Meta(info.upstream_url):	http://www.musepack.net/
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
Cue file library from Musepack.

This package contains the shared library.

%package devel
Summary:	Headers for libcuefile
Requires:	%{name}

%description devel
Cue file library from Musepack.

This package contains the libcuefile development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libcuefile_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libcuefile.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%libcuefile_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libcuefile.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libcuefile_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libcuefile.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libcuefile.so
%endif
%{_libdir}/libcuefile.so
        

%files devel
%defattr(-,root,bin)
%{_includedir}/cuetools/cd.h
%{_includedir}/cuetools/cuefile.h
%{_includedir}/cuetools/cdtext.h

%changelog
* Fri Nov 27 2009 - jlee@thestaticvoid.com
- Initial version
