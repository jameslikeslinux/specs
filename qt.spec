#
# spec file for package: qt
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%define platform solaris-cc-64
%use qt_64 = qt-base.spec
%endif
%include base.inc
%define platform solaris-cc
%use qt = qt-base.spec

Name:		qt
Version:	%{qt.version}
Summary:	Cross-platform C++ Application Framework
License:	LGPLv2.1/GPLv3
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://qt.nokia.com/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWgmake
BuildRequires:	SUNWdbus-devel
BuildRequires:	SUNWglib2-devel
BuildRequires:	SUNWTiff-devel
BuildRequires:	SUNWjpg-devel
BuildRequires:	SUNWpng-devel
BuildRequires:	SUNWlibmng
BuildRequires:	SUNWzlib
BuildRequires:	SUNWxwplt
BuildRequires:	SUNWxorg-clientlibs
BuildRequires:	SUNWfontconfig
BuildRequires:	SUNWxorg-xkb
BuildRequires:	SUNWgtk2-devel
BuildRequires:	SUNWfreetype2
BuildRequires:	SUNWopenssl-include
BuildRequires:	SUNWopenssl-libraries
Requires:	SUNWdbus
Requires:	SUNWglib2
Requires:	SUNWTiff
Requires:	SUNWjpg
Requires:	SUNWpng
Requires:	SUNWlibmng
Requires:	SUNWzlib
Requires:	SUNWxwplt
Requires:	SUNWxorg-clientlibs
Requires:	SUNWfontconfig
Requires:	SUNWxorg-xkb
Requires:	SUNWgtk2
Requires:	SUNWfreetype2
Requires:	SUNWopenssl

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		qt-interest <qt-interest@trolltech.com>
Meta(info.upstream_url):	http://qt.gitorious.org/qt
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
Qt is a cross-platform C++ application framework. Qt's primary feature is its
rich set of widgets that provide standard GUI functionality. 

%package devel
Summary:	Headers for qt
Requires:	%{name}

%description devel
Qt is a cross-platform C++ application framework. Qt's primary feature is its
rich set of widgets that provide standard GUI functionality.

This package contains the qt development files.

%package doc
Summary:	Documentation for qt
Requires:	%{name}

%description doc
Qt is a cross-platform C++ application framework. Qt's primary feature is its
rich set of widgets that provide standard GUI functionality.

This package contains the qt documentation.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%qt_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%qt.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%qt_64.build -d %{name}-%{version}/%{_arch64}
%endif
%qt.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%qt_64.install -d %{name}-%{version}/%{_arch64}
%endif
%qt.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/qdbus
%{_bindir}/%{_arch64}/qtconfig
%endif
%{_bindir}/qdbus
%{_bindir}/qtconfig
%{_libdir}/*.so.*
%{_libdir}/qt/plugins/accessible
%{_libdir}/qt/plugins/designer/libqt3supportwidgets.so
%{_libdir}/qt/plugins/graphicssystems
%{_libdir}/qt/plugins/iconengines
%{_libdir}/qt/plugins/imageformats
%{_libdir}/qt/plugins/inputmethods
%{_libdir}/qt/plugins/script
%{_libdir}/qt/plugins/sqldrivers
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/*.so.*
%{_libdir}/%{_arch64}/qt/plugins/accessible
%{_libdir}/%{_arch64}/qt/plugins/designer/libqt3supportwidgets.so
%{_libdir}/%{_arch64}/qt/plugins/graphicssystems
%{_libdir}/%{_arch64}/qt/plugins/iconengines
%{_libdir}/%{_arch64}/qt/plugins/imageformats
%{_libdir}/%{_arch64}/qt/plugins/inputmethods
%{_libdir}/%{_arch64}/qt/plugins/script
%{_libdir}/%{_arch64}/qt/plugins/sqldrivers
%endif 
%attr(755,root,sys) %dir %{_datadir}
%{_datadir}/qt

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/assistant
%{_bindir}/%{_arch64}/assistant_adp
%{_bindir}/%{_arch64}/designer
%{_bindir}/%{_arch64}/lconvert
%{_bindir}/%{_arch64}/linguist
%{_bindir}/%{_arch64}/lrelease
%{_bindir}/%{_arch64}/lupdate
%{_bindir}/%{_arch64}/moc
%{_bindir}/%{_arch64}/pixeltool
%{_bindir}/%{_arch64}/qcollectiongenerator
%{_bindir}/%{_arch64}/qdbuscpp2xml
%{_bindir}/%{_arch64}/qdbusviewer
%{_bindir}/%{_arch64}/qdbusxml2cpp
%{_bindir}/%{_arch64}/qdoc3
%{_bindir}/%{_arch64}/qhelpconverter
%{_bindir}/%{_arch64}/qhelpgenerator
%{_bindir}/%{_arch64}/qmake
%{_bindir}/%{_arch64}/qt3to4
%{_bindir}/%{_arch64}/qttracereplay
%{_bindir}/%{_arch64}/rcc
%{_bindir}/%{_arch64}/uic
%{_bindir}/%{_arch64}/uic3
%{_bindir}/%{_arch64}/xmlpatterns
%{_bindir}/%{_arch64}/xmlpatternsvalidator
%endif
%{_bindir}/assistant
%{_bindir}/assistant_adp
%{_bindir}/designer
%{_bindir}/lconvert
%{_bindir}/linguist
%{_bindir}/lrelease
%{_bindir}/lupdate
%{_bindir}/moc
%{_bindir}/pixeltool
%{_bindir}/qcollectiongenerator
%{_bindir}/qdbuscpp2xml
%{_bindir}/qdbusviewer
%{_bindir}/qdbusxml2cpp
%{_bindir}/qdoc3
%{_bindir}/qhelpconverter
%{_bindir}/qhelpgenerator
%{_bindir}/qmake
%{_bindir}/qt3to4
%{_bindir}/qttracereplay
%{_bindir}/rcc
%{_bindir}/uic
%{_bindir}/uic3
%{_bindir}/xmlpatterns
%{_bindir}/xmlpatternsvalidator
%{_includedir}
%{_libdir}/*.{la,prl,so,a}
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*.pc
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/*.{la,prl,so,a}
%attr(755,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*.pc
%endif 

%files doc
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/qtdemo
%endif
%{_bindir}/qtdemo
%defattr(-,root,bin)
%{_libdir}/qt/demos
%{_libdir}/qt/examples
%{_libdir}/qt/plugins/designer/libarthurplugin.so
%{_libdir}/qt/plugins/designer/libcontainerextension.so
%{_libdir}/qt/plugins/designer/libcustomwidgetplugin.so
%{_libdir}/qt/plugins/designer/libtaskmenuextension.so
%{_libdir}/qt/plugins/designer/libworldtimeclockplugin.so
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/qt/demos
%{_libdir}/%{_arch64}/qt/examples
%{_libdir}/%{_arch64}/qt/plugins/designer/libarthurplugin.so
%{_libdir}/%{_arch64}/qt/plugins/designer/libcontainerextension.so
%{_libdir}/%{_arch64}/qt/plugins/designer/libcustomwidgetplugin.so
%{_libdir}/%{_arch64}/qt/plugins/designer/libtaskmenuextension.so
%{_libdir}/%{_arch64}/qt/plugins/designer/libworldtimeclockplugin.so
%endif
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_docdir}
%{_docdir}/qt

%changelog
* Sun May 31 2009 - jlee@thestaticvoid.com
- Initial version
