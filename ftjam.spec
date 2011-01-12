#
# spec file for package: ftjam
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		ftjam
Version:	2.5.2
Summary:	Jam Building Tool
License:	Jam
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.freetype.org/jam/
SUNW_BaseDir:   %{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://downloads.sourceforge.net/project/freetype/ftjam/%{version}/ftjam-%{version}.tar.bz2

%include default-depend.inc
BuildRequires:	SUNWgcc432
BuildRequires:	SUNWgmake

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Jam Mailing List <jamming@perforce.com>
Meta(info.upstream_url):	http://www.freetype.org/jam/
Meta(info.classification):	org.opensolaris.category.2008:Development/System

%description
Jam is a small open-source build tool that can be used as a replacement for
Make. Even though Jam is a lot simpler to use than Make, it is far more
powerful and easy to master. It already works on a large variety of platforms
(Unix, Windows, OS/2, VMS, MacOS, BeOS, etc.), it is trivial to port, and its
design is sufficiently clear to allow any average programmer to extend it with
advanced features at will.

%prep
%setup -q
CC=gcc-4.3.2 ./configure --prefix=%{_prefix}

%build
gmake

%install
rm -rf $RPM_BUILD_ROOT
gmake DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %{_bindir}
%{_bindir}/jam

%changelog
* Thu Apr 22 2010 - jlee@thestaticvoid.com
- Initial version
