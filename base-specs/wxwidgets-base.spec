#
# spec file for package: wxwidgets
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		wxwidgets
Version:	2.8.11
Source0:	ftp://ftp.wxwidgets.org/pub/%{version}/wxGTK-%{version}.tar.bz2
#Source0:	ftp://ftp.wxwidgets.org/pub/%{version}/wxWidgets-%{version}.tar.bz2
#Patch0:		wxwidgets-00-solaris.diff

%prep
%setup -q -n wxGTK-%{version}
#%setup -q -n wxWidgets-%{version}
#%patch0 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
	CPUS=1
fi

export CFLAGS="%{optflags} -DwxNEEDS__T"
export CXXFLAGS="%{cxx_optflags} -DwxNEEDS__T"
export LDFLAGS="%{_ldflags} %{extraldflags}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --with-gtk --enable-unicode --with-opengl --enable-graphics_ctx
gmake -j$CPUS

cd contrib/src/stc
gmake -j$CPUS

%install
gmake DESTDIR=$RPM_BUILD_ROOT install

cd contrib/src/stc
gmake DESTDIR=$RPM_BUILD_ROOT install

# remove empty locale dir
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%clean
rm -rf $RPM_BUILD_ROOT
