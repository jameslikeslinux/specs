#
# spec file for package: postfix
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		postfix
Version:	2.8.3
Summary:	Postfix MTA
License:	IBM Public License v1.0
Distribution:	OpenSolaris
Vendor:		OpenSolaris Community
Url:		http://www.postfix.org/
SUNW_Basedir:	/
SUNW_Copyright: %{name}.copyright

Source0:	ftp://postfix.cloud9.net/official/%{name}-%{version}.tar.gz
Source1:	smtp-postfix.xml
Source2:	aliases
Patch0:		postfix-00-nisplus.diff

%include default-depend.inc
BuildRequires:	bdb
BuildRequires:	cyrus-sasl
BuildRequires:	SUNWopenssl-include
BuildRequires:	SUNWopenssl-libraries
Requires:	bdb
Requires:	cyrus-sasl
Requires:	SUNWopenssl-libraries
Conflicts:	SUNWsndm

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Wietse Venema <wietse@porcupine.org>
Meta(info.upstream_url):        http://www.postfix.org/
Meta(info.classification):      org.opensolaris.category.2008:System/Services

%description
Postfix is Wietse Venema's mail transport agent that started life as an
alternative to the widely-used Sendmail program. Postfix attempts to be fast,
easy to administer, and secure, while at the same time being sendmail
compatible enough to not upset existing users. Thus, the outside has a
sendmail-ish flavor, but the inside is completely different. 

%prep
%setup -q
%patch0
make makefiles CC=cc CCARGS='-DDEF_COMMAND_DIR=\"%{_sbindir}\" -DDEF_CONFIG_DIR=\"%{_sysconfdir}/postfix\" -DDEF_DAEMON_DIR=\"%{_libdir}/postfix\" -DDEF_DATA_DIR=\"%{_localstatedir}/lib/postfix\" -DDEF_MAILQ_PATH=\"%{_bindir}/mailq\" -DDEF_HTML_DIR=\"no\" -DDEF_MANPAGE_DIR=\"%{_mandir}\" -DDEF_NEWALIAS_PATH=\"%{_sbindir}/newaliases\" -DDEF_QUEUE_DIR=\"%{_localstatedir}/spool/postfix\" -DDEF_README_DIR=\"no\" -DUSE_SASL_AUTH -DUSE_CYRUS_SASL -I/usr/include/sasl -DUSE_TLS -DHAS_DB' AUXLIBS="-lsasl2 -lssl -lcrypto -ldb"

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make non-interactive-package install_root=$RPM_BUILD_ROOT mail_owner=smmsp setgid_group=mail
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network
cp %{SOURCE1} $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network/smtp-postfix.xml

cd $RPM_BUILD_ROOT%{_sbindir}
ln -s ../lib/sendmail .

cd $RPM_BUILD_ROOT%{_sysconfdir}
mkdir mail
cp %{SOURCE2} mail/aliases
ln -s mail/aliases aliases

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%files
%defattr(-,root,bin)
%attr(755,root,sys) %dir %{_prefix}
%dir %{_bindir}
%{_bindir}/mailq
%dir %{_libdir}
%{_libdir}/sendmail
%dir %{_libdir}/postfix
%{_libdir}/postfix/anvil
%{_libdir}/postfix/bounce
%{_libdir}/postfix/cleanup
%{_libdir}/postfix/discard
%{_libdir}/postfix/error
%{_libdir}/postfix/flush
%{_libdir}/postfix/lmtp
%{_libdir}/postfix/local
%{_libdir}/postfix/master
%{_libdir}/postfix/nqmgr
%{_libdir}/postfix/oqmgr
%{_libdir}/postfix/pickup
%{_libdir}/postfix/pipe
%{_libdir}/postfix/proxymap
%{_libdir}/postfix/qmgr
%{_libdir}/postfix/qmqpd
%{_libdir}/postfix/scache
%{_libdir}/postfix/showq
%{_libdir}/postfix/smtp
%{_libdir}/postfix/smtpd
%{_libdir}/postfix/spawn
%{_libdir}/postfix/tlsmgr
%{_libdir}/postfix/trivial-rewrite
%{_libdir}/postfix/verify
%{_libdir}/postfix/virtual
%{_libdir}/postfix/post-install
%{_libdir}/postfix/postfix-files
%{_libdir}/postfix/postfix-wrapper
%{_libdir}/postfix/postmulti-script
%{_libdir}/postfix/master.cf
%{_libdir}/postfix/postfix-script
%{_libdir}/postfix/main.cf
%{_libdir}/postfix/dnsblog
%{_libdir}/postfix/tlsproxy
%{_libdir}/postfix/postscreen
%dir %{_sbindir}
%{_sbindir}/newaliases
%{_sbindir}/postalias
%{_sbindir}/postcat
%{_sbindir}/postconf
%attr(2755,root,mail) %{_sbindir}/postdrop
%{_sbindir}/postfix
%{_sbindir}/postkick
%{_sbindir}/postlock
%{_sbindir}/postlog
%{_sbindir}/postmap
%{_sbindir}/postmulti
%attr(2755,root,mail) %{_sbindir}/postqueue
%{_sbindir}/postsuper
%hard %{_sbindir}/sendmail
%attr(755,root,sys) %dir %{_datadir}
%dir %{_mandir}
%dir %{_mandir}/man1
%{_mandir}/man1/mailq.1
%{_mandir}/man1/newaliases.1
%{_mandir}/man1/postalias.1
%{_mandir}/man1/postcat.1
%{_mandir}/man1/postconf.1
%{_mandir}/man1/postdrop.1
%{_mandir}/man1/postfix.1
%{_mandir}/man1/postkick.1
%{_mandir}/man1/postlock.1
%{_mandir}/man1/postlog.1
%{_mandir}/man1/postmap.1
%{_mandir}/man1/postmulti.1
%{_mandir}/man1/postqueue.1
%{_mandir}/man1/postsuper.1
%{_mandir}/man1/sendmail.1
%dir %{_mandir}/man5
%{_mandir}/man5/access.5
%{_mandir}/man5/aliases.5
%{_mandir}/man5/body_checks.5
%{_mandir}/man5/bounce.5
%{_mandir}/man5/canonical.5
%{_mandir}/man5/cidr_table.5
%{_mandir}/man5/generic.5
%{_mandir}/man5/header_checks.5
%{_mandir}/man5/ldap_table.5
%{_mandir}/man5/master.5
%{_mandir}/man5/mysql_table.5
%{_mandir}/man5/nisplus_table.5
%{_mandir}/man5/pcre_table.5
%{_mandir}/man5/pgsql_table.5
%{_mandir}/man5/postconf.5
%{_mandir}/man5/postfix-wrapper.5
%{_mandir}/man5/regexp_table.5
%{_mandir}/man5/relocated.5
%{_mandir}/man5/tcp_table.5
%{_mandir}/man5/transport.5
%{_mandir}/man5/virtual.5
%{_mandir}/man5/sqlite_table.5
%dir %{_mandir}/man8
%{_mandir}/man8/anvil.8
%{_mandir}/man8/bounce.8
%{_mandir}/man8/cleanup.8
%{_mandir}/man8/defer.8
%{_mandir}/man8/discard.8
%{_mandir}/man8/error.8
%{_mandir}/man8/flush.8
%{_mandir}/man8/lmtp.8
%{_mandir}/man8/local.8
%{_mandir}/man8/master.8
%{_mandir}/man8/oqmgr.8
%{_mandir}/man8/pickup.8
%{_mandir}/man8/pipe.8
%{_mandir}/man8/proxymap.8
%{_mandir}/man8/qmgr.8
%{_mandir}/man8/qmqpd.8
%{_mandir}/man8/scache.8
%{_mandir}/man8/showq.8
%{_mandir}/man8/smtp.8
%{_mandir}/man8/smtpd.8
%{_mandir}/man8/spawn.8
%{_mandir}/man8/tlsmgr.8
%{_mandir}/man8/trace.8
%{_mandir}/man8/trivial-rewrite.8
%{_mandir}/man8/verify.8
%{_mandir}/man8/virtual.8
%{_mandir}/man8/postscreen.8
%{_mandir}/man8/tlsproxy.8
%{_mandir}/man8/dnsblog.8
%defattr(-,root,sys)
%dir %{_sysconfdir}
%{_sysconfdir}/aliases
%config %{_sysconfdir}/mail/aliases
%dir %{_sysconfdir}/postfix
%{_sysconfdir}/postfix/LICENSE
%{_sysconfdir}/postfix/TLS_LICENSE
%{_sysconfdir}/postfix/access
%{_sysconfdir}/postfix/aliases
%{_sysconfdir}/postfix/bounce.cf.default
%{_sysconfdir}/postfix/canonical
%{_sysconfdir}/postfix/generic
%{_sysconfdir}/postfix/header_checks
%config %{_sysconfdir}/postfix/main.cf
%{_sysconfdir}/postfix/main.cf.default
%{_sysconfdir}/postfix/makedefs.out
%config %{_sysconfdir}/postfix/master.cf
%{_sysconfdir}/postfix/relocated
%{_sysconfdir}/postfix/transport
%{_sysconfdir}/postfix/virtual
%dir %{_localstatedir}
%attr(755,root,other) %dir %{_localstatedir}/lib
%attr(700,smmsp,other) %dir %{_localstatedir}/lib/postfix
%attr(755,root,bin) %dir %{_localstatedir}/spool
%attr(755,root,bin) %dir %{_localstatedir}/spool/postfix
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/active
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/bounce
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/corrupt
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/defer
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/deferred
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/flush
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/hold
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/incoming
%attr(730,smmsp,mail) %dir %{_localstatedir}/spool/postfix/maildrop
%attr(755,root,bin) %dir %{_localstatedir}/spool/postfix/pid
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/private
%attr(710,smmsp,mail) %dir %{_localstatedir}/spool/postfix/public
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/saved
%attr(700,smmsp,bin) %dir %{_localstatedir}/spool/postfix/trace
%dir %{_localstatedir}/svc
%dir %{_localstatedir}/svc/manifest
%dir %{_localstatedir}/svc/manifest/network
%class(manifest) %attr(444,root,sys) %{_localstatedir}/svc/manifest/network/smtp-postfix.xml

%changelog
* Thu May 26 2011 - jlee@thestaticvoid.com
- Bump to 2.8.3
* Fri Jun 19 2009 - jlee@thestaticvoid.com
- Initial version
