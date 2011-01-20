#
# spec file for package: gtkimageview
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use gtkimageview_64 = gtkimageview-base.spec
%endif
%include base.inc
%use gtkimageview = gtkimageview-base.spec

Name:		gtkimageview
Version:	%{gtkimageview.version}
Summary:	GtkImageView
License:	LGPLv2.1
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://trac.bjourne.webfactional.com/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWgmake
BuildRequires:	SUNWggrp
BuildRequires:	SUNWgtk2-devel
BuildRequires:  SUNWgnome-common-devel
Requires:	SUNWgtk2

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Björn Lindqvist <bjourne@gmail.com>
Meta(info.upstream_url):	http://trac.bjourne.webfactional.com/
Meta(info.classification):	org.opensolaris.category.2008:Development/GNOME and GTK+

%description
GtkImageView is a simple image viewer widget for GTK. Similar to the image
viewer panes in gThumb or Eye of Gnome. It makes writing image viewing and
editing applications easy.

This package contains the shared library.

%package devel
Summary:	Headers for gtkimageview
Requires:	%{name}

%description devel
GtkImageView is a simple image viewer widget for GTK. Similar to the image
viewer panes in gThumb or Eye of Gnome. It makes writing image viewing and
editing applications easy.

This package contains the gtkimageview development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%gtkimageview_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%gtkimageview.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%gtkimageview_64.build -d %{name}-%{version}/%{_arch64}
%endif
%gtkimageview.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%gtkimageview_64.install -d %{name}-%{version}/%{_arch64}
%endif
%gtkimageview.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libgtkimageview.so.0
%{_libdir}/%{_arch64}/libgtkimageview.so.0.0.0
%endif
%{_libdir}/libgtkimageview.so.0
%{_libdir}/libgtkimageview.so.0.0.0

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libgtkimageview.la
%{_libdir}/%{_arch64}/libgtkimageview.so
%attr(755,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/gtkimageview.pc
%endif
%{_libdir}/libgtkimageview.la
%{_libdir}/libgtkimageview.so
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/gtkimageview.pc
%{_includedir}/gtkimageview/gdkpixbufdrawcache.h
%{_includedir}/gtkimageview/gtkimageview.h
%{_includedir}/gtkimageview/gtkanimview.h
%{_includedir}/gtkimageview/gtkiimagetool.h
%{_includedir}/gtkimageview/gtkimagescrollwin.h
%{_includedir}/gtkimageview/gtkimagetooldragger.h
%{_includedir}/gtkimageview/gtkimagetoolpainter.h
%{_includedir}/gtkimageview/gtkimagetoolselector.h
%{_includedir}/gtkimageview/gtkimagenav.h
%{_includedir}/gtkimageview/gtkzooms.h
%{_includedir}/gtkimageview/cursors.h
%{_includedir}/gtkimageview/mouse_handler.h
%{_includedir}/gtkimageview/utils.h
%{_includedir}/gtkimageview/gtkimageview-typebuiltins.h
%attr(755,root,sys) %dir %{_datadir}
%{_datadir}/gtk-doc/html/gtkimageview

%changelog
* Thu Apr 29 2010 - jlee@thestaticvoid.com
- Initial version
