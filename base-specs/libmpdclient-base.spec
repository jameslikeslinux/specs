#
# spec file for package: libmpdclient
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libmpdclient
Version:	2.3
Source0:	http://downloads.sourceforge.net/project/musicpd/libmpdclient/%{version}/libmpdclient-%{version}.tar.bz2

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
export PKG_CONFIG_LIBDIR="%{_libdir}/pkgconfig"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --disable-static
gmake

%install
gmake DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
