#
# spec file for package: libmad
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libmad
Version:	0.15.1.2
Source0:	ftp://ftp.mars.org/pub/mpeg/libmad-0.15.1b.tar.gz

# Create mad.pc
# http://www.mars.org/pipermail/mad-dev/2004-August/001066.html
Patch0:		libmad-00-pkg-config.diff

%prep
%setup -q -n libmad-0.15.1b
%patch0 -p1
aclocal-1.9
autoheader
autoconf
libtoolize --force
touch NEWS AUTHORS ChangeLog
automake-1.9 --add-missing

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-static
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
