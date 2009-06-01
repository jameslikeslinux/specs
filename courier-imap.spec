#
# spec file for package: courier-imap
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		courier-imap
Version:	4.5.0
Summary:	Courier IMAP Server
License:	GPLv3
Group:		System/Services
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.courier-mta.org/imap/
SUNW_Basedir:	/
SUNW_Copyright: %{name}.copyright

Source0:	http://voxel.dl.sourceforge.net/sourceforge/courier/%{name}-%{version}.tar.bz2
Source1:	courier-imap.xml

%include default-depend.inc
BuildRequires:	bdb
BuildRequires:	SUNWgamin
BuildRequires:	courier-authlib-devel
Requires:	bdb
Requires:	SUNWgamin
Requires:	courier-authlib

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Sam Varshavchik <mrsam@courier-mta.com>
Meta(info.upstream_url):	http://www.courier-mta.org/imap/

%description
The Courier mail transfer agent (MTA) is an integrated mail/groupware server
based on open commodity protocols, such as ESMTP, IMAP, POP3, LDAP, SSL, and
HTTP. Courier provides ESMTP, IMAP, POP3, webmail, and mailing list services
within a single, consistent, framework.

This package provides an IMAP server that accesses email stored in Maildirs
format mailboxes. This server has an extremely small footprint and provides
shared and virtual shared folders. 

%prep
%setup -q
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}/courier-imap --libexecdir=%{_libexecdir}/courier-imap --localstatedir=%{_localstatedir}/lib/courier-imap --datarootdir=%{_datadir}/courier-imap --mandir=%{_mandir} --with-waitfunc=wait3 --with-db=db

%build
gmake

%install
rm -rf $RPM_BUILD_ROOT
gmake DESTDIR=$RPM_BUILD_ROOT install
cp sysconftool $RPM_BUILD_ROOT%{_libexecdir}/courier-imap
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network
cp %{SOURCE1} $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network/courier-imap.xml

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%files
%defattr(-,root,bin)
%attr(755,root,sys) %dir %{_prefix}
%dir %{_bindir}
%{_bindir}/deliverquota
%{_bindir}/maildirmake
%{_bindir}/maildiracl
%{_bindir}/maildirkw
%{_bindir}/couriertls
%{_bindir}/imapd
%{_bindir}/pop3d
%dir %{_libexecdir}
%dir %{_libexecdir}/courier-imap
%{_libexecdir}/courier-imap/imapd-ssl.rc
%{_libexecdir}/courier-imap/sysconftool
%{_libexecdir}/courier-imap/pop3d-ssl.rc
%{_libexecdir}/courier-imap/makedatprog
%{_libexecdir}/courier-imap/couriertcpd
%{_libexecdir}/courier-imap/pop3d.rc
%{_libexecdir}/courier-imap/imapd.rc
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_datadir}/courier-imap
%attr(755,root,other) %{_datadir}/courier-imap/mkpop3dcert
%attr(755,root,other) %{_datadir}/courier-imap/mkimapdcert
%dir %{_mandir}
%dir %{_mandir}/man1
%dir %{_mandir}/man8
%{_mandir}/man1/maildirmake.1
%{_mandir}/man1/maildiracl.1
%{_mandir}/man1/maildirkw.1
%{_mandir}/man1/couriertcpd.1
%{_mandir}/man8/mkimapdcert.8
%{_mandir}/man8/mkpop3dcert.8
%{_mandir}/man8/deliverquota.8
%{_mandir}/man8/imapd.8
%dir %{_sbindir}
%{_sbindir}/sharedindexsplit
%{_sbindir}/mkpop3dcert
%{_sbindir}/imaplogin
%{_sbindir}/mkimapdcert
%{_sbindir}/pop3login
%{_sbindir}/sharedindexinstall
%defattr(-,root,sys)
%dir %{_sysconfdir}
%dir %{_sysconfdir}/courier-imap
%{_sysconfdir}/courier-imap/imapd-ssl.dist
%{_sysconfdir}/courier-imap/imapd.cnf
%{_sysconfdir}/courier-imap/imapd.dist
%{_sysconfdir}/courier-imap/pop3d-ssl.dist
%{_sysconfdir}/courier-imap/pop3d.cnf
%{_sysconfdir}/courier-imap/pop3d.dist
%{_sysconfdir}/courier-imap/quotawarnmsg.example
%dir %{_sysconfdir}/courier-imap/shared
%dir %{_sysconfdir}/courier-imap/shared.tmp
%dir %{_localstatedir}
%attr(755,root,other) %dir %{_localstatedir}/lib
%attr(755,root,other) %dir %{_localstatedir}/lib/courier-imap
%dir %{_localstatedir}/svc
%dir %{_localstatedir}/svc/manifest
%dir %{_localstatedir}/svc/manifest/network
%class(manifest) %attr(444,root,sys) %{_localstatedir}/svc/manifest/network/courier-imap.xml

%changelog
* Sun May 31 2009 - jlee@thestaticvoid.com
- Add header and correct copyright
* Sat May 30 2009 - jlee@thestaticvoid.com
- Initial version
