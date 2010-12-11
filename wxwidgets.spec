#
# spec file for package: wxwidgets
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%define extraldflags "-m64"
%use wxwidgets_64 = wxwidgets-base.spec
%endif
%include base.inc
%define extraldflags ""
%use wxwidgets = wxwidgets-base.spec

Name:		wxwidgets
Version:	%{wxwidgets.version}
Summary:	Cross-platform C++ GUI toolkit
License:	wxWindows Licence
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.wxwidgets.org/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires: text/gnu-grep
BuildRequires: developer/build/gnu-make
BuildRequires: library/audio/gstreamer
BuildRequires: library/gnome/gnome-component
BuildRequires: library/graphics/pixman
BuildRequires: x11/library/libxau
BuildRequires: x11/library/libxcomposite
BuildRequires: x11/library/libxcursor
BuildRequires: x11/library/libxdmcp
BuildRequires: x11/library/libxevie
BuildRequires: x11/library/libxi
BuildRequires: x11/library/libxinerama
BuildRequires: x11/library/libxrandr
BuildRequires: x11/library/libxscrnsaver
BuildRequires: x11/library/mesa
Requires: library/audio/gstreamer
Requires: library/gnome/gnome-component
Requires: library/graphics/pixman
Requires: x11/library/libxau
Requires: x11/library/libxcomposite
Requires: x11/library/libxcursor
Requires: x11/library/libxdmcp
Requires: x11/library/libxevie
Requires: x11/library/libxi
Requires: x11/library/libxinerama
Requires: x11/library/libxrandr
Requires: x11/library/libxscrnsaver
Requires: x11/library/mesa

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Robert Roebling <robert@roebling.de>
Meta(info.upstream_url):	http://www.wxwidgets.org/
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
wxWidgets (formerly known as wxWindows) is a class library for C++ providing
GUI components and other facilities on several popular platforms (and some
unpopular ones as well). 

This package contains the shared libraries.

%package devel
Summary:        Headers for wxwidgets
Requires:       %{name}

%description devel
wxWidgets (formerly known as wxWindows) is a class library for C++ providing
GUI components and other facilities on several popular platforms (and some
unpopular ones as well). 

This package contains the wxwidgets development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%wxwidgets_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%wxwidgets.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%wxwidgets_64.build -d %{name}-%{version}/%{_arch64}
%endif
%wxwidgets.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%wxwidgets_64.install -d %{name}-%{version}/%{_arch64}
%endif
%wxwidgets.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libwx_baseu_net-2.8.so.0
%{_libdir}/%{_arch64}/libwx_baseu_xml-2.8.so.0
%{_libdir}/%{_arch64}/libwx_baseu-2.8.so.0
%{_libdir}/%{_arch64}/libwx_gtk2u_adv-2.8.so.0
%{_libdir}/%{_arch64}/libwx_gtk2u_aui-2.8.so.0
%{_libdir}/%{_arch64}/libwx_gtk2u_core-2.8.so.0
%{_libdir}/%{_arch64}/libwx_gtk2u_gl-2.8.so.0
%{_libdir}/%{_arch64}/libwx_gtk2u_html-2.8.so.0
%{_libdir}/%{_arch64}/libwx_gtk2u_qa-2.8.so.0
%{_libdir}/%{_arch64}/libwx_gtk2u_richtext-2.8.so.0
%{_libdir}/%{_arch64}/libwx_gtk2u_stc-2.8.so.0
%{_libdir}/%{_arch64}/libwx_gtk2u_xrc-2.8.so.0
%endif
%{_libdir}/libwx_baseu_net-2.8.so.0
%{_libdir}/libwx_baseu_xml-2.8.so.0
%{_libdir}/libwx_baseu-2.8.so.0
%{_libdir}/libwx_gtk2u_adv-2.8.so.0
%{_libdir}/libwx_gtk2u_aui-2.8.so.0
%{_libdir}/libwx_gtk2u_core-2.8.so.0
%{_libdir}/libwx_gtk2u_gl-2.8.so.0
%{_libdir}/libwx_gtk2u_html-2.8.so.0
%{_libdir}/libwx_gtk2u_qa-2.8.so.0
%{_libdir}/libwx_gtk2u_richtext-2.8.so.0
%{_libdir}/libwx_gtk2u_stc-2.8.so.0
%{_libdir}/libwx_gtk2u_xrc-2.8.so.0

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/wxrc-2.8
%{_bindir}/%{_arch64}/wxrc
%{_bindir}/%{_arch64}/wx-config
%{_libdir}/%{_arch64}/libwx_baseu_net-2.8.so
%{_libdir}/%{_arch64}/libwx_baseu_xml-2.8.so
%{_libdir}/%{_arch64}/libwx_baseu-2.8.so
%{_libdir}/%{_arch64}/libwx_gtk2u_adv-2.8.so
%{_libdir}/%{_arch64}/libwx_gtk2u_aui-2.8.so
%{_libdir}/%{_arch64}/libwx_gtk2u_core-2.8.so
%{_libdir}/%{_arch64}/libwx_gtk2u_gl-2.8.so
%{_libdir}/%{_arch64}/libwx_gtk2u_html-2.8.so
%{_libdir}/%{_arch64}/libwx_gtk2u_qa-2.8.so
%{_libdir}/%{_arch64}/libwx_gtk2u_richtext-2.8.so
%{_libdir}/%{_arch64}/libwx_gtk2u_stc-2.8.so
%{_libdir}/%{_arch64}/libwx_gtk2u_xrc-2.8.so
%{_libdir}/%{_arch64}/wx/config/gtk2-unicode-release-2.8
%{_libdir}/%{_arch64}/wx/include/gtk2-unicode-release-2.8/wx/setup.h
%endif
%{_bindir}/wxrc-2.8
%{_bindir}/wxrc
%{_bindir}/wx-config
%{_libdir}/libwx_baseu_net-2.8.so
%{_libdir}/libwx_baseu_xml-2.8.so
%{_libdir}/libwx_baseu-2.8.so
%{_libdir}/libwx_gtk2u_adv-2.8.so
%{_libdir}/libwx_gtk2u_aui-2.8.so
%{_libdir}/libwx_gtk2u_core-2.8.so
%{_libdir}/libwx_gtk2u_gl-2.8.so
%{_libdir}/libwx_gtk2u_html-2.8.so
%{_libdir}/libwx_gtk2u_qa-2.8.so
%{_libdir}/libwx_gtk2u_richtext-2.8.so
%{_libdir}/libwx_gtk2u_stc-2.8.so
%{_libdir}/libwx_gtk2u_xrc-2.8.so
%{_libdir}/wx/config/gtk2-unicode-release-2.8
%{_libdir}/wx/include/gtk2-unicode-release-2.8/wx/setup.h
%{_includedir}/wx-2.8
%attr(-,root,sys) %dir %{_datadir}
%attr(-,root,other) %dir %{_datadir}/aclocal
%{_datadir}/aclocal/wxwin.m4
%{_datadir}/bakefile/presets/wx.bkl
%{_datadir}/bakefile/presets/wx_unix.bkl
%{_datadir}/bakefile/presets/wx_win32.bkl

%changelog
* Sat Oct 10 2010 - jlee@thestaticvoid.com
- Initial version
