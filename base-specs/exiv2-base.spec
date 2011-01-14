#
# spec file for package: exiv2
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		exiv2
Version:	0.21
Source0:	http://www.exiv2.org/exiv2-%{version}.tar.gz
Patch0:		exiv2-00-sunstudio.diff

%prep
%setup -q
%patch0 -p1

%build
export CXX=/opt/sunstudio12.1/bin/CC
export CFLAGS="%{optflags}"
export CXXFLAGS="%{cxx_optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --disable-dependency-tracking --disable-visibility --disable-static

# Makefiles seem broken...make install performs a compilation regardless
#gmake

%install
gmake DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT%{_libdir}/libexiv2.la

%clean
rm -rf $RPM_BUILD_ROOT
