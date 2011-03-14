#
# spec file for package: darktable
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		darktable
Version:	0.8
Summary:	Darktable Photo Workflow Software
License:	GPLv3
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://darktable.sourceforge.net/
SUNW_Basedir:	/
SUNW_Copyright: %{name}.copyright

Source0:	http://downloads.sourceforge.net/project/darktable/darktable/%{version}/darktable-%{version}.tar.gz
Patch0:		darktable-00-sun-studio.diff

%include default-depend.inc
BuildRequires:	SUNWgit
BuildRequires:	SUNWcmake
BuildRequires:	SUNWgmake
BuildRequires:	SUNWgnu-gettext
BuildRequires:	SUNWperl584usr
BuildRequires:	SUNWgtk2-devel
BuildRequires:	SUNWlibglade-devel
BuildRequires:	SUNWlxml-devel
BuildRequires:	SUNWgnome-config-devel
#BuildRequires:	SUNWgnome-camera-devel
BuildRequires:	lensfun-devel
BuildRequires:	SUNWglib2-devel
BuildRequires:	SUNWfreetype2
BuildRequires:	SUNWcairo-devel
BuildRequires:	SUNWpango-devel
BuildRequires:	SUNWlibrsvg-devel
BuildRequires:	SUNWsqlite3
BuildRequires:	exiv2-devel
BuildRequires:	SUNWcurl
BuildRequires:	SUNWzlib
BuildRequires:	SUNWpng-devel
BuildRequires:	SUNWjpg-devel
BuildRequires:	SUNWTiff-devel
BuildRequires:	SUNWopenexr
BuildRequires:	lcms2-devel
BuildRequires:	flickcurl-devel
BuildRequires:	SUNWgnome-libs-devel

Requires:	SUNWgtk2
Requires:	SUNWlibglade
Requires:	SUNWlxml
Requires:	SUNWgnome-config
#Requires:	SUNWgnome-camera
Requires:	lensfun
Requires:	SUNWglib2
Requires:	SUNWfreetype2
Requires:	SUNWcairo
Requires:	SUNWpango
Requires:	SUNWlibrsvg
Requires:	SUNWsqlite3
Requires:	exiv2
Requires:	SUNWcurl
Requires:	SUNWzlib
Requires:	SUNWpng
Requires:	SUNWjpg
Requires:	SUNWTiff
Requires:	SUNWopenexr
Requires:	lcms2
Requires:	flickcurl
Requires:	SUNWgnome-libs

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Johannes Hanika <hanatos@gmail.com>
Meta(info.upstream_url):        http://darktable.sourceforge.net/
Meta(info.classification):	org.opensolaris.category.2008:Applications/Graphics and Imaging

%description
darktable is a photography workflow application: a virtual lighttable and
darkroom for photographers: it manages your digital negatives in a database
and lets you view them through a zoomable lighttable. it also enables you to
develop raw images and enhance them.

%prep
#rm -rf darktable
#git clone git://darktable.git.sf.net/gitroot/darktable/darktable
#cd darktable
%setup
%patch0 -p1

%build
#cd darktable
mkdir build
cd build
PATH=/usr/perl5/bin:$PATH CFLAGS="-g" CXXFLAGS="-g" cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DINSTALL_IOP_EXPERIMENTAL=On -DINSTALL_IOP_LEGACY=Off -DOpenMP_C_FLAGS=-xopenmp -DOpenMP_CXX_FLAGS=-xopenmp -DDONT_INSTALL_GCONF_SCHEMAS=On -DUSE_CAMERA_SUPPORT=Off ..
gmake

%install
rm -rf $RPM_BUILD_ROOT
#cd darktable/build
cd build

# Solaris cmake has a bug which defines CMAKE_INSTALL_PREFIX to
# something weird like "./sfw_build".  We need to set the variable
# even if it is defined.
grep -v "IF(NOT DEFINED CMAKE_INSTALL_PREFIX)" cmake_install.cmake > cmake_install.cmake.new
mv -f cmake_install.cmake.new cmake_install.cmake

gmake DESTDIR=$RPM_BUILD_ROOT install

# Solaris doesn't support SHM
rm -f $RPM_BUILD_ROOT%{_bindir}/darktable-faster

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%attr(755,root,sys) %dir %{_prefix}
%{_bindir}/darktable
%{_libdir}/darktable
%attr(755,root,sys) %dir %{_datadir}
%{_datadir}/darktable
%attr(-,root,other) %{_datadir}/locale
%{_mandir}/man1/darktable.1
%attr(-,root,other) %dir %{_datadir}/applications
%{_datadir}/applications/darktable.desktop
%attr(-,root,other) %dir %{_docdir}
%{_docdir}/darktable/AUTHORS
%{_docdir}/darktable/LICENSE
%{_docdir}/darktable/TRANSLATORS
%{_docdir}/darktable/README
%attr(-,root,other) %{_datadir}/icons
%defattr(-,root,sys)
%ips_tag(restart_fmri="svc:/application/desktop-cache/gconf-cache:default") %{_sysconfdir}/gconf/schemas/darktable.schemas

%changelog
* Fri Mar 11 2011 - jlee@thestaticvoid.com
- Initial version
