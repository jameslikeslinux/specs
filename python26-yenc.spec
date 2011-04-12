#
# spec file for package: python-yenc
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define python_version 2.6

Name:		python26-yenc
Version:	0.3
Summary:	yEnc module for Python
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.golug.it/yenc.html
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://www.golug.it/pub/yenc/yenc-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWpython26-setuptools
Requires:	SUNWpython26-setuptools

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Alessandro Duca <alessandro.duca@gmail.com>
Meta(info.upstream_url):        http://www.yenctemplate.org/
Meta(info.classification):	org.opensolaris.category.2008:Development/Python

%description
A fairly simple Python module, it provide only raw yEnc encoding/decoding with
builitin crc32 calculation. 

%prep
%setup -q -n yenc-%{version}

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
%{_libdir}/python%{python_version}/vendor-packages

%changelog
* Wed Apr 6 2011 - jlee@thestaticvoid.com
- Initial version
