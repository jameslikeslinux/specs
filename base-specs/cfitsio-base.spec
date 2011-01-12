#
# spec file for package: cfitsio
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		cfitsio
Version:	3.25
Source0:	ftp://heasarc.gsfc.nasa.gov/software/fitsio/c/cfitsio3250.tar.gz
Patch0:		cfitsio-00-ldflags.diff

%prep
%setup -q -n %{name}
%patch0
aclocal-1.9
autoconf

%build
export FC=f77
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make
make shared

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT%{_libdir}/libcfitsio.a

%clean
rm -rf $RPM_BUILD_ROOT
