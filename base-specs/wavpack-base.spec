#
# spec file for package: wavpack
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		wavpack
Version:	4.60.0
Source0:	http://www.wavpack.com/wavpack-%{version}.tar.bz2
Patch0:		wavpack-00-sunproc.diff

%prep
%setup -q
%patch0

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --disable-static
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
