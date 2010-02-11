#
# spec file for package: qt
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		qt
Version:	4.6.1
Source0:	http://get.qt.nokia.com/qt/source/%{name}-everywhere-opensource-src-%{version}.tar.gz
Patch0:		qt-00-qtconcurrent-map-explicit-type.diff
#Patch1:	qt-00-sunstudio-gstreamer.diff

%prep
%setup -q -n %{name}-everywhere-opensource-src-%{version}
%patch0
#%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
	CPUS=1
fi

# phonon disabled for lack of 64-bit gtstreamer
echo "yes" | ./configure -platform %{platform} \
			 -opensource \
			 -prefix %{_prefix} \
			 -bindir %{_bindir} \
			 -libdir %{_libdir} \
			 -docdir %{_datadir}/doc/qt \
			 -headerdir %{_prefix}/include \
			 -plugindir %{_libdir}/qt/plugins \
			 -datadir %{_datadir}/qt \
			 -translationdir %{_datadir}/qt/translations \
			 -sysconfdir %{_sysconfdir}/qt \
			 -examplesdir %{_libdir}/qt/examples \
			 -demosdir %{_libdir}/qt/demos \
			 -no-phonon \
			 -no-gstreamer \
			 -lCrun
gmake -j$CPUS

%install
gmake INSTALL_ROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
