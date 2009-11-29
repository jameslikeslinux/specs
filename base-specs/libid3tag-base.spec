#
# spec file for package: libid3tag
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libid3tag
Version:	0.15.1.2
Source0:	ftp://ftp.mars.org/pub/mpeg/libid3tag-0.15.1b.tar.gz

%prep
%setup -q -n libid3tag-0.15.1b

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-static
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
