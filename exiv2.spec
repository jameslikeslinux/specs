#
# spec file for package: exiv2
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use exiv2_64 = exiv2-base.spec
%endif
%include base.inc
%use exiv2 = exiv2-base.spec

Name:		exiv2
Version:	%{exiv2.version}
Summary:	Image Metadata Library and Tools
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.exiv2.org/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	sunstudio12u1
BuildRequires:  SUNWggrp
BuildRequires:	SUNWgmake
BuildRequires:	SUNWzlib
BuildRequires:	SUNWlexpt
Requires:	SUNWzlib
Requires:	SUNWlexpt

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Andreas Huggel <ahuggel@gmx.net>
Meta(info.upstream_url):	http://www.exiv2.org/
Meta(info.classification):	org.opensolaris.category.2008:Applications/Graphics and Imaging

%description
Exiv2 is a C++ library and a command line utility to manage image metadata.
It provides fast and easy read and write access to the Exif, IPTC and XMP
metadata of images in various formats.

This package contains the shared libraries and executables.

%package devel
Summary:        Headers for exiv2
Requires:       %{name}

%description devel
Exiv2 is a C++ library and a command line utility to manage image metadata.
It provides fast and easy read and write access to the Exif, IPTC and XMP
metadata of images in various formats.

This package contains the exiv2 development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%exiv2_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%exiv2.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%exiv2_64.build -d %{name}-%{version}/%{_arch64}
%endif
%exiv2.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%exiv2_64.install -d %{name}-%{version}/%{_arch64}
%endif
%exiv2.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/exiv2 $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec exiv2
%endif

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/exiv2
%{_libdir}/%{_arch64}/libexiv2.so.10.0.1
%{_libdir}/%{_arch64}/libexiv2.so.10
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/exiv2
%hard %{_bindir}/exiv2
%else
%{_bindir}/exiv2
%endif
%{_libdir}/libexiv2.so.10.0.1
%{_libdir}/libexiv2.so.10
%attr(755,root,sys) %dir %{_datadir}
%dir %{_mandir}
%dir %{_mandir}/man1
%{_mandir}/man1/exiv2.1
%attr(-,root,other) %{_datadir}/locale

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libexiv2.so
%attr(-,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/exiv2.pc
%endif
%{_libdir}/libexiv2.so
%attr(-,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/exiv2.pc
%{_includedir}/exiv2/exv_conf.h
%{_includedir}/exiv2/basicio.hpp
%{_includedir}/exiv2/bmpimage.hpp
%{_includedir}/exiv2/convert.hpp
%{_includedir}/exiv2/cr2image.hpp
%{_includedir}/exiv2/crwimage.hpp
%{_includedir}/exiv2/datasets.hpp
%{_includedir}/exiv2/easyaccess.hpp
%{_includedir}/exiv2/error.hpp
%{_includedir}/exiv2/exif.hpp
%{_includedir}/exiv2/exiv2.hpp
%{_includedir}/exiv2/futils.hpp
%{_includedir}/exiv2/gifimage.hpp
%{_includedir}/exiv2/image.hpp
%{_includedir}/exiv2/iptc.hpp
%{_includedir}/exiv2/jp2image.hpp
%{_includedir}/exiv2/jpgimage.hpp
%{_includedir}/exiv2/metadatum.hpp
%{_includedir}/exiv2/mrwimage.hpp
%{_includedir}/exiv2/orfimage.hpp
%{_includedir}/exiv2/pgfimage.hpp
%{_includedir}/exiv2/pngimage.hpp
%{_includedir}/exiv2/preview.hpp
%{_includedir}/exiv2/properties.hpp
%{_includedir}/exiv2/psdimage.hpp
%{_includedir}/exiv2/rafimage.hpp
%{_includedir}/exiv2/rw2image.hpp
%{_includedir}/exiv2/tags.hpp
%{_includedir}/exiv2/tgaimage.hpp
%{_includedir}/exiv2/tiffimage.hpp
%{_includedir}/exiv2/types.hpp
%{_includedir}/exiv2/value.hpp
%{_includedir}/exiv2/version.hpp
%{_includedir}/exiv2/xmp.hpp
%{_includedir}/exiv2/xmpsidecar.hpp

%changelog
* Sat Mar 12 2011 - jlee@thestaticvoid.com
- Bump to version 0.21.1
* Fri Jan 14 2011 - jlee@thestaticvoid.com
- Bump to version 0.21
* Fri Apr 24 2010 - jlee@thestaticvoid.com
- Initial version
