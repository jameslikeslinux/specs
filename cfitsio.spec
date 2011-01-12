#
# spec file for package: cfitsio
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use cfitsio_64 = cfitsio-base.spec
%endif
%include base.inc
%use cfitsio = cfitsio-base.spec

Name:		cfitsio
Version:	%{cfitsio.version}
Summary:	A FITS File Subroutine Library
License:	Public Domain
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://heasarc.nasa.gov/docs/software/fitsio/fitsio.html
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWggrp
BuildRequires:  SUNWaconf

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		William D. Pence <pence@milkyway.gsfc.nasa.gov>
Meta(info.upstream_url):	http://heasarc.nasa.gov/docs/software/fitsio/fitsio.html
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
CFITSIO is a library of C and Fortran subroutines for reading and writing data
files in FITS (Flexible Image Transport System) data format. CFITSIO provides
simple high-level routines for reading and writing FITS files that insulate
the programmer from the internal complexities of the FITS format. CFITSIO also
provides many advanced features for manipulating and filtering the information
in FITS files. 

This package contains the shared library.

%package devel
Summary:	Headers for cfitsio
Requires:	%{name}

%description devel
CFITSIO is a library of C and Fortran subroutines for reading and writing data
files in FITS (Flexible Image Transport System) data format. CFITSIO provides
simple high-level routines for reading and writing FITS files that insulate
the programmer from the internal complexities of the FITS format. CFITSIO also
provides many advanced features for manipulating and filtering the information
in FITS files. 

This package contains the cfitsio development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%cfitsio_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%cfitsio.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%cfitsio_64.build -d %{name}-%{version}/%{_arch64}
%endif
%cfitsio.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%cfitsio_64.install -d %{name}-%{version}/%{_arch64}
%endif
%cfitsio.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libcfitsio.so
%endif
%{_libdir}/libcfitsio.so

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/pkgconfig/cfitsio.pc
%endif
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/cfitsio.pc
%{_includedir}/fitsio.h
%{_includedir}/fitsio2.h
%{_includedir}/longnam.h
%{_includedir}/drvrsmem.h

%changelog
* Wed Jan 12 2011 - jlee@thestaticvoid.com
- Bump to verison 3.25
* Fri Apr 23 2010 - jlee@thestaticvoid.com
- Initial version
