#
# spec file for package: lensfun
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use lensfun_64 = lensfun-base.spec
%endif
%include base.inc
%use lensfun = lensfun-base.spec

Name:		lensfun
Version:	%{lensfun.version}
Summary:	Lens Correction Library
License:	LGPLv3/CC-BY-SA
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://lensfun.berlios.de/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWgmake
BuildRequires:	SUNWdoxygen
BuildRequires:	SUNWglib2-devel
Requires:	SUNWglib2

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Andrew Zabolotny <zap@homelink.ru>
Meta(info.upstream_url):	http://lensfun.berlios.de/
Meta(info.classification):	org.opensolaris.category.2008:System/Multimedia Libraries

%description
The lensfun library not only provides a way to read the database and search
for specific things in it, but also provides a set of algorithms for
correcting images based on detailed knowledge of lens properties. Right now
lensfun is designed to correct distortion, transversal (also known as lateral)
chromatic aberrations, vignetting and colour contribution of the lens (e.g.
when sometimes people says one lens gives "yellowish" images and another, say,
"bluish"). 

This package contains the shared library.

%package devel
Summary:        Headers for lensfun
Requires:       %{name}

%description devel
The lensfun library not only provides a way to read the database and search
for specific things in it, but also provides a set of algorithms for
correcting images based on detailed knowledge of lens properties. Right now
lensfun is designed to correct distortion, transversal (also known as lateral)
chromatic aberrations, vignetting and colour contribution of the lens (e.g.
when sometimes people says one lens gives "yellowish" images and another, say,
"bluish"). 

This package contains the lensfun development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%lensfun_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%lensfun.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%lensfun_64.build -d %{name}-%{version}/%{_arch64}
%endif
%lensfun.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%lensfun_64.install -d %{name}-%{version}/%{_arch64}
%endif
%lensfun.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/liblensfun.so.0.2.5
%{_libdir}/%{_arch64}/liblensfun.so.0
%endif
%{_libdir}/liblensfun.so.0.2.5
%{_libdir}/liblensfun.so.0
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_docdir}
%{_docdir}/lensfun-%{version}/README
%{_docdir}/lensfun-%{version}/lgpl-3.0.txt
%{_docdir}/lensfun-%{version}/gpl-3.0.txt
%{_docdir}/lensfun-%{version}/cc-by-sa-3.0.txt
%{_datadir}/lensfun/6x6.xml
%{_datadir}/lensfun/compact-canon.xml
%{_datadir}/lensfun/compact-casio.xml
%{_datadir}/lensfun/compact-fujifilm.xml
%{_datadir}/lensfun/compact-kodak.xml
%{_datadir}/lensfun/compact-konica-minolta.xml
%{_datadir}/lensfun/compact-leica.xml
%{_datadir}/lensfun/compact-nikon.xml
%{_datadir}/lensfun/compact-olympus.xml
%{_datadir}/lensfun/compact-panasonic.xml
%{_datadir}/lensfun/compact-pentax.xml
%{_datadir}/lensfun/compact-ricoh.xml
%{_datadir}/lensfun/compact-sigma.xml
%{_datadir}/lensfun/compact-sony.xml
%{_datadir}/lensfun/generic.xml
%{_datadir}/lensfun/rf-leica.xml
%{_datadir}/lensfun/slr-canon.xml
%{_datadir}/lensfun/slr-contax.xml
%{_datadir}/lensfun/slr-hasselblad.xml
%{_datadir}/lensfun/slr-konica-minolta.xml
%{_datadir}/lensfun/slr-nikon.xml
%{_datadir}/lensfun/slr-olympus.xml
%{_datadir}/lensfun/slr-panasonic.xml
%{_datadir}/lensfun/slr-pentax.xml
%{_datadir}/lensfun/slr-samsung.xml
%{_datadir}/lensfun/slr-schneider.xml
%{_datadir}/lensfun/slr-sigma.xml
%{_datadir}/lensfun/slr-sony.xml
%{_datadir}/lensfun/slr-tamron.xml
%{_datadir}/lensfun/slr-tokina.xml
%{_datadir}/lensfun/slr-ussr.xml

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/liblensfun.so
%attr(-,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/lensfun.pc
%endif
%{_libdir}/liblensfun.so
%attr(-,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/lensfun.pc
%{_includedir}/lensfun.h
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_docdir}
%{_docdir}/lensfun-%{version}/manual

%changelog
* Wed Apr 28 2010 - jlee@thestaticvoid.com
- Initial version
