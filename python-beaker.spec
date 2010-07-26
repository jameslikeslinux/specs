#
# spec file for package: python-beaker
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define python_version 2.4

Name:		python-beaker
Version:	1.5.4
Summary:	A Session and Caching library with WSGI Middleware
License:	BSD
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://beaker.groovie.org/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://pypi.python.org/packages/source/B/Beaker/Beaker-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWpython-setuptools
Requires:	SUNWpython-setuptools

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Ben Bangert <ben@groovie.org>
Meta(info.upstream_url):        http://beaker.groovie.org/
Meta(info.classification):	org.opensolaris.category.2008:Development/Python

%description
Beaker is a web session and general caching library that includes WSGI
middleware for use in web applications.

As a general caching library, Beaker can handle storing for various times any
Python object that can be pickled with optional back-ends on a fine-grained
basis.

%prep
%setup -q -n Beaker-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

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
%dir %{_libdir}
%dir %{_libdir}/python%{python_version}
%{_libdir}/python%{python_version}/vendor-packages

%changelog
* Sun Jun 25 2010 - jlee@thestaticvoid.com
- Initial version
