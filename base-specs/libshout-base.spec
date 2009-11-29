#
# spec file for package: libshout
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libshout
Version:	2.2.2
Source0:	http://downloads.us.xiph.org/releases/libshout/libshout-%{version}.tar.gz

# Add possibility to disable theora and speex support
# https://trac.xiph.org/ticket/1162
Patch0:		libshout-00-automagic.diff

%prep
%setup -q
%patch0 -p1
aclocal-1.9 -I m4
autoheader
autoconf
libtoolize --force
automake-1.9 --add-missing

%build
export XIPH_CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-static --disable-theora --disable-speex
make CFLAGS="%{optflags}" LDFLAGS="%{_ldflags}" 

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
