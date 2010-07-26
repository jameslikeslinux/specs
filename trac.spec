#
# spec file for package: trac
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define python_version 2.4

Name:           trac
Version:        0.12
Summary:        Trac Integrated SCM & Project Management
License:        BSD
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:            http://trac.edgewall.org/
SUNW_Basedir:	/
SUNW_Copyright: %{name}.copyright

Source0:        ftp://ftp.edgewall.org/pub/trac/Trac-%{version}.tar.gz
Source1:	tracd.xml

%include default-depend.inc
BuildRequires:	SUNWpython-setuptools
Requires:	SUNWpython-setuptools
Requires:	SUNWsvn-python 
Requires:	SUNWpysqlite
Requires:	python-genshi
Requires:	python-pygments

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Edgewall Software <trac-dev@googlegroups.com>
Meta(info.upstream_url):        http://trac.edgewall.org/
Meta(info.classification):	org.opensolaris.category.2008:Development/Python

%description
Trac is an enhanced wiki and issue tracking system for software development
projects.

%prep
%setup -q -n Trac-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/trac
cp -R cgi-bin $RPM_BUILD_ROOT%{_datadir}/trac
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network
cp %{SOURCE1} $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network/tracd.xml
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/trac

# move to vendor-packages
if [ -d $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages ] ; then
	mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages
	mv $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages/* \
		$RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages/
	rmdir $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages
fi

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%files
%defattr(-,root,bin)
%attr(755,root,sys) %dir %{_prefix}
%dir %{_bindir}
%{_bindir}/tracd
%{_bindir}/trac-admin
%dir %{_libdir}
%dir %{_libdir}/python%{python_version}
%{_libdir}/python%{python_version}/vendor-packages
%attr(755,root,sys) %dir %{_datadir}
%attr(-,root,other) %{_datadir}/trac
%dir %{_localstatedir}
%dir %{_localstatedir}/trac
%dir %{_localstatedir}/svc
%dir %{_localstatedir}/svc/manifest
%dir %{_localstatedir}/svc/manifest/network
%class(manifest) %attr(444,root,sys) %{_localstatedir}/svc/manifest/network/tracd.xml

%changelog
* Fri Jul 23 2010 - jlee@thestaticvoid.com
- Bump to version 0.12
* Sun May 31 2009 - jlee@thestaticvoid.com
- Add header
* Sun May 31 2009 - jlee@thestaticvoid.com
- Change name from Trac to trac
* Sun May 31 2009 - jlee@thestaticvoid.com
- Add Pygments requirement for syntax highlighting.
* Sat May 30 2009 - jlee@thestaticvoid.com
- Initial version
