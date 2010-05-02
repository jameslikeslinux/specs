#
# spec file for package: gtkimageview
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		gtkimageview
Version:	1.6.4
Source0:	http://trac.bjourne.webfactional.com/chrome/common/releases/gtkimageview-%{version}.tar.gz
Patch0:		gtkimageview-00-cflags.diff
Patch1:		gtkimageview-01-gtkiimagetool-void.diff

%prep
%setup -q
%patch0
%patch1

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-static
gmake

%install
gmake DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
