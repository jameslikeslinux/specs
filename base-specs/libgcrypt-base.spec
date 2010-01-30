#
# spec file for package: libgcrypt
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libgcrypt
Version:	1.4.5
Source0:	ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --build=%{build_type} --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --disable-static
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
