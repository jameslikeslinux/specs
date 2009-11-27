#
# spec file for package: libreplaygain
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libreplaygain
Version:	453
Source0:	http://files.musepack.net/source/libreplaygain_r%{version}.tar.gz

%prep
%setup -q -n libreplaygain_r%{version}
mkdir config
aclocal-1.9
autoheader
autoconf
libtoolize
automake-1.9 --add-missing

%build
export CFLAGS="-D__inline=inline %{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-static
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
