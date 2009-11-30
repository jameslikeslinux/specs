#
# spec file for package: mpdscribble
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		mpdscribble
Version:	0.18.1
Source0:	http://downloads.sourceforge.net/project/musicpd/mpdscribble/%{version}/mpdscribble-%{version}.tar.bz2

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
export PKG_CONFIG_LIBDIR="%{_libdir}/pkgconfig"
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --bindir=%{_bindir}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
