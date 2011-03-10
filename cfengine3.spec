#
# spec file for package: cfengine
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		cfengine3
Version:	3.1.2
Summary:	Cfengine 3
License:	GPLv3
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.cfengine.org/
SUNW_Basedir:	/
SUNW_Copyright: %{name}.copyright

Source0:	http://www.cfengine.org/tarballs/cfengine-%{version}.tar.gz
Source1:	cfengine3.xml

%include default-depend.inc
BuildRequires:	bdb
BuildRequires:	SUNWopenssl-include
BuildRequires:	SUNWflexlex
BuildRequires:	SUNWbison
BuildRequires:	SUNWpcre
Requires:	bdb
Requires:	SUNWopenssl-libraries
Requires:	SUNWpcre

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Cfengine Community <help-cfengine@cfengine.org>
Meta(info.upstream_url):	http://www.cfengine.org/
Meta(info.classification):	org.opensolaris.category.2008:System/Administration and Configuration

%description
The main purpose of cfengine is to allow the system administrator to create a
single central file which will define how every host on a network should be
configured.

It takes a while to set up cfengine for a network (especially an already
existing network), but once that is done you will wonder how you ever lived
without it! 

%prep
%setup -q -n cfengine-%{version}
./configure --prefix=%{_prefix}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_libdir}

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cfengine/bin
cd $RPM_BUILD_ROOT%{_localstatedir}/cfengine/bin
for i in cf-execd cf-key cf-monitord cf-serverd cf-promises cf-runagent cf-know cf-report cf-agent; do
	ln -sf %{_sbindir}/$i .
done

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/application
cp %{SOURCE1} $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/application/cfengine3.xml

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%files
%defattr(-,root,bin)
%attr(755,root,sys) %dir %{_prefix}
%dir %{_sbindir}
%{_sbindir}/cf-execd
%{_sbindir}/cf-key
%{_sbindir}/cf-monitord
%{_sbindir}/cf-serverd
%{_sbindir}/cf-promises
%{_sbindir}/cf-runagent
%{_sbindir}/cf-know
%{_sbindir}/cf-report
%{_sbindir}/cf-agent
%attr(755,root,sys) %dir %{_datadir}
%dir %{_mandir}
%dir %{_mandir}/man8
%{_mandir}/man8/cf-runagent.8
%{_mandir}/man8/cf-monitord.8
%{_mandir}/man8/cf-know.8
%{_mandir}/man8/cf-execd.8
%{_mandir}/man8/cf-report.8
%{_mandir}/man8/cf-key.8
%{_mandir}/man8/cf-promises.8
%{_mandir}/man8/cf-serverd.8
%{_mandir}/man8/cf-agent.8
%attr(755,root,other) %dir %{_docdir}
%{_docdir}/cfengine
%{_localstatedir}/cfengine/bin/cf-*
%class(manifest) %attr(444,root,sys) %{_localstatedir}/svc/manifest/application/cfengine3.xml

%changelog
* Wed Jan 12 2011 - jlee@thestaticvoid.com
- Bump to version 3.1.2
* Thu Jun 17 2010 - jlee@thestaticvoid.com
- Bump to version 3.0.5
* Thu Feb 17 2010 - jlee@thestaticvoid.com
- Bump to version 3.0.3
* Wed Dec 16 2009 - jlee@thestaticvoid.com
- Initial version
