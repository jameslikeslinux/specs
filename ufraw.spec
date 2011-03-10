#
# spec file for package: ufraw
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		ufraw
Version:	0.18
Summary:	Unidentified Flying Raw
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://ufraw.sourceforge.net/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://downloads.sourceforge.net/project/ufraw/ufraw/ufraw-%{version}/ufraw-%{version}.tar.gz
Patch0:		ufraw-00-dcraw-openmp.diff

%include default-depend.inc
BuildRequires:	SUNWgtk2-devel
BuildRequires:	SUNWlcms
BuildRequires:	SUNWgnome-img-editor-devel
BuildRequires:	SUNWTiff-devel
BuildRequires:	SUNWjpg-devel
BuildRequires:	SUNWpng-devel
BuildRequires:	cfitsio-devel
BuildRequires:	exiv2-devel
BuildRequires:	SUNWzlib
BuildRequires:	SUNWbzip
BuildRequires:	gtkimageview-devel
BuildRequires:	lensfun-devel
Requires:	SUNWgtk2
Requires:	SUNWlcms
Requires:	SUNWgnome-img-editor
Requires:	SUNWTiff
Requires:	SUNWjpg
Requires:	SUNWpng
Requires:	cfitsio
Requires:	exiv2
Requires:	SUNWzlib
Requires:	SUNWbzip
Requires:	gtkimageview
Requires:	lensfun

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Udi Fuchs <udifuchs@gmail.com>
Meta(info.upstream_url):	http://ufraw.sourceforge.net/
Meta(info.classification):	org.opensolaris.category.2008:Applications/Graphics and Imaging

%description
UFRaw is a utility to read and manipulate raw images from digital cameras.
It can be used by itself or as a GIMP or CinePaint plug-in.
It reads raw images using Dave Coffin's raw conversion utility DCRaw.
It supports basic color management using Little CMS, allowing the user to
apply color profiles.

%prep
%setup -q
%patch0

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{_bindir}/ufraw
%{_bindir}/ufraw-batch
%{_libdir}/gimp/2.0/plug-ins/ufraw-gimp
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}/man1/ufraw.1
%attr(755,root,other) %dir %{_datadir}/pixmaps
%{_datadir}/pixmaps/ufraw.png
%attr(-,root,other) %{_datadir}/locale

%changelog
* Thu Mar 10 2011 - jlee@thestaticvoid.com
- Bump to 0.18
* Fri Apr 30 2010 - jlee@thestaticvoid.com
- Initial version
