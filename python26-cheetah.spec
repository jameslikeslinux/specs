#
# spec file for package: python-cheetah
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define python_version 2.6

Name:		python26-cheetah
Version:	2.4.4
Summary:	Cheetah is a template engine and code generation tool.
License:	MIT
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.cheetahtemplate.org/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://pypi.python.org/packages/source/C/Cheetah/Cheetah-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWpython26-setuptools
Requires:	SUNWpython26-setuptools

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            R. Tyler Ballance <cheetahtemplate-discuss@lists.sourceforge.net>
Meta(info.upstream_url):        http://www.cheetahtemplate.org/
Meta(info.classification):	org.opensolaris.category.2008:Development/Python

%description
Cheetah is an open source template engine and code generation tool.  It can be
used standalone or combined with other tools and frameworks. Web development
is its principle use, but Cheetah is very flexible and is also being used to
generate C++ game code, Java, sql, form emails and even Python code.

%prep
%setup -q -n Cheetah-%{version}

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
%{_bindir}/cheetah
%{_bindir}/cheetah-analyze
%{_bindir}/cheetah-compile
%{_libdir}/python%{python_version}/vendor-packages

%changelog
* Wed Apr 6 2011 - jlee@thestaticvoid.com
- Initial version
