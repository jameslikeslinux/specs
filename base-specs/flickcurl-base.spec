#
# spec file for package: flickcurl
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		flickcurl
Version:	1.20
Source0:	http://download.dajobe.org/flickcurl/flickcurl-%{version}.tar.gz

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --disable-static
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
