#
# spec file for package: python26-qt
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define python_version 2.6

Name:		python26-qt
Version:	4.7
Summary:	Qt bindings for Python
License:	GPLv3
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.riverbankcomputing.co.uk/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://www.riverbankcomputing.co.uk/static/Downloads/PyQt4/PyQt-x11-gpl-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWgmake
BuildRequires:	SUNWPython26
BuildRequires:	SUNWdbus-python26-devel
BuildRequires:	python26-sip
BuildRequires:	qt-devel
Requires:	SUNWPython26
Requires:	SUNWdbus-python26
Requires:	qt

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Riverbank Computing Limited <info@riverbankcomputing.com>
Meta(info.upstream_url):        http://www.riverbankcomputing.co.uk/
Meta(info.classification):	org.opensolaris.category.2008:Development/Python

%description
PyQt is a set of Python bindings for Nokia's Qt application framework and runs
on all platforms supported by Qt including Windows, MacOS/X and Linux.


%prep
%setup -q -n PyQt-x11-gpl-%{version}

%build
python%{python_version} configure.py --confirm-license

# force the compiler to use /usr/include/python2.6/sip.h
# instead of /usr/include/sip.h which ships with Solaris
sed 's@<sip.h>@"/usr/include/python%{python_version}/sip.h"@' QtCore/sipAPIQtCore.h > QtCore/sipAPIQtCore.h.new
mv -f QtCore/sipAPIQtCore.h.new QtCore/sipAPIQtCore.h

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
        CPUS=1
fi

gmake -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
gmake DESTDIR=$RPM_BUILD_ROOT install

# move to vendor-packages
if [ -d $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages ] ; then
	mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages
	mv $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages/* \
		$RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages/
	rmdir $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{_bindir}/pyuic4
%{_bindir}/pyrcc4
%{_bindir}/pylupdate4
%{_libdir}/python%{python_version}/vendor-packages/PyQt4
%{_libdir}/python%{python_version}/vendor-packages/dbus/mainloop/qt.so
%attr(-,root,sys) %dir %{_datadir}
%{_datadir}/sip

%changelog
* Thu Feb 11 2010 - jlee@thestaticvoid.com
- Initial version
