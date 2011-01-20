#
# spec file for package: libao
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libao
Version:	1.0.0
Source0:	http://downloads.xiph.org/releases/ao/libao-1.0.0.tar.gz

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
