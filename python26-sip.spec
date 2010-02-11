#
# spec file for package: python26-sip
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define python_version 2.6

Name:		python26-sip
Version:	4.10
Summary:	Python/C++ bindings generator 
License:	SIP
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.riverbankcomputing.co.uk/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://www.riverbankcomputing.co.uk/static/Downloads/sip4/sip-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWPython26
Requires:	SUNWPython26

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Riverbank Computing Limited <info@riverbankcomputing.com>
Meta(info.upstream_url):        http://www.riverbankcomputing.co.uk/
Meta(info.classification):	org.opensolaris.category.2008:Development/Python

%description
SIP is a tool for generating bindings for C++ classes with some ideas borrowed
from SWIG, but capable of tighter bindings, because it's specific to C++ and
Python. 

%prep
%setup -q -n sip-%{version}

%build
python%{python_version} configure.py
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

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
%{_bindir}/sip
%{_includedir}/python%{python_version}/sip.h
%{_libdir}/python%{python_version}/vendor-packages/sip.so
%{_libdir}/python%{python_version}/vendor-packages/sipconfig.py
%{_libdir}/python%{python_version}/vendor-packages/sipdistutils.py

%changelog
* Thu Feb 11 2010 - jlee@thestaticvoid.com
- Initial version
