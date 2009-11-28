#
# spec file for package: libmpcdec
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libmpcdec
Version:	435
Source0:	http://files.musepack.net/source/musepack_src_r%{version}.tar.gz
Patch0:		libmpcdec-00-mpcgain-ldflags.diff
Patch1:		libmpcdec-01-include-string-header.diff

%prep
%setup -q -n musepack_src_r%{version}
%patch0
%patch1
mkdir config
aclocal-1.9
autoheader
autoconf
libtoolize
automake-1.9 --add-missing

%build
export CFLAGS="%{optflags} -D__inline=inline"
export LDFLAGS="%{_ldflags} -lm"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --disable-static
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
