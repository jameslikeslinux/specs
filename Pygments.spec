%include Solaris.inc

%define python_version 2.4

Name:		Pygments
Version:	1.0
Summary:	Pygments is a syntax highlighting package written in Python
License:	BSD
Group:		Development/Python
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://pygments.org/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://pypi.python.org/packages/source/P/Pygments/%{name}-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWpython-setuptools
Requires:	SUNWpython-setuptools

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Georg Brandl <georg@python.org>
Meta(info.upstream_url):        http://pygments.org/

%description
Pygments aims to be a generic syntax highlighter for general use in all kinds
of software such as forum systems, wikis or other applications that need to
prettify source code. 

%prep
%setup -q

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
%dir %{_bindir}
%{_bindir}/pygmentize
%dir %{_libdir}
%dir %{_libdir}/python%{python_version}
%{_libdir}/python%{python_version}/vendor-packages

%changelog
* Fri May 31 2009 - jlee@thestaticvoid.com
- Initial version
