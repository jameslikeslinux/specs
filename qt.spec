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
Url:		http://www.qtsoftware.com/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc

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

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
for i in *; do
	if [ -f $i ]; then
	        mv $i %{base_isa}
	        ln -s ../lib/isaexec $i
	fi
done
%endif

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/assistant
%{_bindir}/%{_arch64}/assistant_adp
%{_bindir}/%{_arch64}/designer
%{_bindir}/%{_arch64}/lconvert
%{_bindir}/%{_arch64}/linguist
%{_bindir}/%{_arch64}/pixeltool
%{_bindir}/%{_arch64}/qcollectiongenerator
%{_bindir}/%{_arch64}/qdbus
%{_bindir}/%{_arch64}/qdbusviewer
%{_bindir}/%{_arch64}/qhelpconverter
%{_bindir}/%{_arch64}/qhelpgenerator
%{_bindir}/%{_arch64}/qmake
%{_bindir}/%{_arch64}/qtconfig
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/assistant
%{_bindir}/%{base_isa}/assistant_adp
%{_bindir}/%{base_isa}/designer
%{_bindir}/%{base_isa}/lconvert
%{_bindir}/%{base_isa}/linguist
%{_bindir}/%{base_isa}/pixeltool
%{_bindir}/%{base_isa}/qcollectiongenerator
%{_bindir}/%{base_isa}/qdbus
%{_bindir}/%{base_isa}/qdbusviewer
%{_bindir}/%{base_isa}/qhelpconverter
%{_bindir}/%{base_isa}/qhelpgenerator
%{_bindir}/%{base_isa}/qmake
%{_bindir}/%{base_isa}/qtconfig
%hard %{_bindir}/assistant
%hard %{_bindir}/assistant_adp
%hard %{_bindir}/designer
%hard %{_bindir}/lconvert
%hard %{_bindir}/linguist
%hard %{_bindir}/pixeltool
%hard %{_bindir}/qcollectiongenerator
%hard %{_bindir}/qdbus
%hard %{_bindir}/qdbusviewer
%hard %{_bindir}/qhelpconverter
%hard %{_bindir}/qhelpgenerator
%hard %{_bindir}/qmake
%hard %{_bindir}/qtconfig
%else
%{_bindir}/assistant
%{_bindir}/assistant_adp
%{_bindir}/designer
%{_bindir}/lconvert
%{_bindir}/linguist
%{_bindir}/pixeltool
%{_bindir}/qcollectiongenerator
%{_bindir}/qdbus
%{_bindir}/qdbusviewer
%{_bindir}/qhelpconverter
%{_bindir}/qhelpgenerator
%{_bindir}/qmake
%{_bindir}/qtconfig
%endif
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
%{_bindir}/%{_arch64}/lrelease
%{_bindir}/%{_arch64}/lupdate
%{_bindir}/%{_arch64}/moc
%{_bindir}/%{_arch64}/qdbuscpp2xml
%{_bindir}/%{_arch64}/qdbusxml2cpp
%{_bindir}/%{_arch64}/qt3to4
%{_bindir}/%{_arch64}/rcc
%{_bindir}/%{_arch64}/uic
%{_bindir}/%{_arch64}/uic3
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/lrelease
%{_bindir}/%{base_isa}/lupdate
%{_bindir}/%{base_isa}/moc
%{_bindir}/%{base_isa}/qdbuscpp2xml
%{_bindir}/%{base_isa}/qdbusxml2cpp
%{_bindir}/%{base_isa}/qt3to4
%{_bindir}/%{base_isa}/rcc
%{_bindir}/%{base_isa}/uic
%{_bindir}/%{base_isa}/uic3
%hard %{_bindir}/lrelease
%hard %{_bindir}/lupdate
%hard %{_bindir}/moc
%hard %{_bindir}/qdbuscpp2xml
%hard %{_bindir}/qdbusxml2cpp
%hard %{_bindir}/qt3to4
%hard %{_bindir}/rcc
%hard %{_bindir}/uic
%hard %{_bindir}/uic3
%else
%{_bindir}/lrelease
%{_bindir}/lupdate
%{_bindir}/moc
%{_bindir}/qdbuscpp2xml
%{_bindir}/qdbusxml2cpp
%{_bindir}/qt3to4
%{_bindir}/rcc
%{_bindir}/uic
%{_bindir}/uic3
%endif
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
%if %can_isaexec
%{_bindir}/%{base_isa}/qtdemo
%hard %{_bindir}/qtdemo
%else
%{_bindir}/qtdemo
%endif
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
