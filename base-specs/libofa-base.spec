#
# spec file for package: libofa
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libofa
Version:	0.9.3
Source0:	http://musicip-libofa.googlecode.com/files/libofa-%{version}.tar.gz
Patch0:		libofa-00-examples-include-unistd-header.diff

%prep
%setup -q
%patch0
aclocal-1.9
autoconf
libtoolize --force
automake-1.9

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-static
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
