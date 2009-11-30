#
# spec file for package: mpd
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		mpd
Version:	0.15.6
Source0:	http://downloads.sourceforge.net/project/musicpd/mpd/%{version}/mpd-%{version}.tar.bz2

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{cxx_optflags}"
export LDFLAGS="%{_ldflags}"
export MAD_CFLAGS="-I/usr/include"
export MAD_LIBS="-L%{_libdir} -lmad"
export PKG_CONFIG_LIBDIR="%{_libdir}/pkgconfig"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --with-zeroconf=no
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
