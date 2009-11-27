#
# spec file for package: libfaad2
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libfaad2
Version:	2.7
Source0:	http://downloads.sourceforge.net/project/faac/faad2-src/faad2-%{version}/faad2-%{version}.tar.bz2
Patch0:		libfaad2-00-define-inline.diff

%prep
%setup -q -n faad2-%{version}
%patch0

%build
export CFLAGS="-I../include %{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --with-mp4v2 --disable-static
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
