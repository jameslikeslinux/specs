#
# spec file for package: lensfun
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		lensfun
Version:	0.2.5
Source0:	http://download.berlios.de/lensfun/lensfun-%{version}.tar.bz2
Patch0:		lensfun-00-install.diff
Patch1:		lensfun-01-sunstudio.diff

%prep
%setup -q

# GNU make is 'gmake' on solaris
sed 's/make --version/gmake --version/g' configure > configure.new
mv -f configure.new configure
chmod +x configure

# build system assumes GNU install which is ginstall on solaris
%patch0

%patch1

%build
export LD=$CXX
export CFLAGS="%{optflags}"
export CXXFLAGS="%{cxx_optflags} -xarch=sse2"
export LDFLAGS="%{cxx_optflags} %{_ldflags} -G -lCstd -lCrun -lc"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --vectorization=SSE,SSE2

# build all but makedep and examples
rm -rf tools/makedep
gmake AUTODEP=0 libs data docs

%install
gmake DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
