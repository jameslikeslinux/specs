%include Solaris.inc

Name:		cyrus-sasl
Version:	2.1.23
Summary:	Simple Authentication and Security Layer
License:	CMU
Group:		System/Services
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://cyrusimap.web.cmu.edu/
SUNW_Basedir:	/
SUNW_Copyright: %{name}.copyright

Source0:	ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/%{name}-%{version}.tar.gz
Source1:	saslauthd.xml
Patch0:		cyrus-sasl-00-auth_getpwent.diff

%include default-depend.inc
BuildRequires:	SUNWopenssl-include
BuildRequires:	SUNWopenssl-libraries
BuildRequires:	bdb
Requires:	SUNWopenssl-libraries
Requires:	bdb

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		CMU <cyrus-bugs+@andrew.cmu.edu>
Meta(info.upstream_url):	http://asg.web.cmu.edu/sasl/

%description
SASL is the Simple Authentication and Security Layer, a method for adding
authentication support to connection-based protocols. To use SASL, a protocol
includes a command for identifying and authenticating a user to a server and
for optionally negotiating protection of subsequent protocol interactions. If
its use is negotiated, a security layer is inserted between the protocol and
the connection. See RFC 2222 for more information. 

%package devel
Summary:	Headers for cyrus-sasl
Group:		System/Services
Requires:	%{name}

%description devel
SASL is the Simple Authentication and Security Layer, a method for adding
authentication support to connection-based protocols. To use SASL, a protocol
includes a command for identifying and authenticating a user to a server and
for optionally negotiating protection of subsequent protocol interactions. If
its use is negotiated, a security layer is inserted between the protocol and
the connection. See RFC 2222 for more information. 

This package contains the cyrus-sasl development files.

%prep
%setup -q
%patch0
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --mandir=%{_mandir} --with-configdir=%{_sysconfdir}/sasl2 --with-dbpath=%{_sysconfdir}/sasl2/sasldb2 --with-saslauthd=%{_localstatedir}/lib/sasl2 --with-plugindir=%{_libdir}/sasl2 --enable-login

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sasl2
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/sasl2
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network
cp %{SOURCE1} $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network/saslauthd.xml

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%files
%defattr(-,root,bin)
%attr(755,root,sys) %dir /usr
%dir %{_libdir}
%dir %{_libdir}/sasl2
%{_libdir}/sasl2/libotp.so.2
%{_libdir}/sasl2/libsasldb.so.2
%{_libdir}/sasl2/libanonymous.so.2
%{_libdir}/sasl2/libdigestmd5.so.2
%{_libdir}/sasl2/libotp.so.2.0.23
%{_libdir}/sasl2/libgssapiv2.so.2
%{_libdir}/sasl2/libplain.so.2
%{_libdir}/sasl2/libgssapiv2.so.2.0.23
%{_libdir}/sasl2/libsasldb.so.2.0.23
%{_libdir}/sasl2/libplain.so.2.0.23
%{_libdir}/sasl2/libcrammd5.so.2
%{_libdir}/sasl2/libanonymous.so.2.0.23
%{_libdir}/sasl2/libdigestmd5.so.2.0.23
%{_libdir}/sasl2/libcrammd5.so.2.0.23
%{_libdir}/sasl2/liblogin.so.2.0.23
%{_libdir}/sasl2/liblogin.so.2
%{_libdir}/libsasl2.so.2
%{_libdir}/libsasl2.so.2.0.23
%attr(755,root,sys) %dir %{_datadir}
%dir %{_mandir}
%dir %{_mandir}/man8
%{_mandir}/man8/sasldblistusers2.8
%{_mandir}/man8/saslauthd.8
%{_mandir}/man8/saslpasswd2.8
%{_mandir}/man8/pluginviewer.8
%dir %{_sbindir}
%{_sbindir}/saslpasswd2
%{_sbindir}/saslauthd
%{_sbindir}/sasldblistusers2
%{_sbindir}/testsaslauthd
%{_sbindir}/pluginviewer
%defattr(-,root,sys)
%dir %{_sysconfdir}
%dir %{_sysconfdir}/sasl2
%dir %{_localstatedir}
%attr(755,root,other) %dir %{_localstatedir}/lib
%attr(755,root,other) %dir %{_localstatedir}/lib/sasl2
%dir %{_localstatedir}/svc
%dir %{_localstatedir}/svc/manifest
%dir %{_localstatedir}/svc/manifest/network
%class(manifest) %attr(444,root,sys) %{_localstatedir}/svc/manifest/network/saslauthd.xml

%files devel
%defattr(-,root,bin)
%attr(755,root,sys) %dir /usr
%dir %{_libdir}
%dir %{_libdir}/sasl2
%{_libdir}/sasl2/libcrammd5.la
%{_libdir}/sasl2/libplain.so
%{_libdir}/sasl2/libotp.la
%{_libdir}/sasl2/libdigestmd5.so
%{_libdir}/sasl2/libdigestmd5.la
%{_libdir}/sasl2/libplain.la
%{_libdir}/sasl2/libotp.so
%{_libdir}/sasl2/libcrammd5.so
%{_libdir}/sasl2/libsasldb.so
%{_libdir}/sasl2/libgssapiv2.la
%{_libdir}/sasl2/libanonymous.so
%{_libdir}/sasl2/libgssapiv2.so
%{_libdir}/sasl2/libanonymous.la
%{_libdir}/sasl2/libsasldb.la
%{_libdir}/sasl2/liblogin.so
%{_libdir}/sasl2/liblogin.la
%{_libdir}/libsasl2.so
%{_libdir}/libsasl2.la
%dir %{_mandir}
%dir %{_mandir}/man3
%{_mandir}/man3/sasl_errstring.3
%{_mandir}/man3/sasl_chalprompt_t.3
%{_mandir}/man3/sasl_encode.3
%{_mandir}/man3/sasl_server_start.3
%{_mandir}/man3/sasl_setpass.3
%{_mandir}/man3/sasl_getopt_t.3
%{_mandir}/man3/sasl_global_listmech.3
%{_mandir}/man3/sasl_auxprop_request.3
%{_mandir}/man3/sasl_canon_user_t.3
%{_mandir}/man3/sasl_checkapop.3
%{_mandir}/man3/sasl_decode.3
%{_mandir}/man3/sasl_client_new.3
%{_mandir}/man3/sasl_encodev.3
%{_mandir}/man3/sasl_server_init.3
%{_mandir}/man3/sasl_errdetail.3
%{_mandir}/man3/sasl_checkpass.3
%{_mandir}/man3/sasl_server_new.3
%{_mandir}/man3/sasl_getsecret_t.3
%{_mandir}/man3/sasl_done.3
%{_mandir}/man3/sasl_getrealm_t.3
%{_mandir}/man3/sasl_getsimple_t.3
%{_mandir}/man3/sasl_server_userdb_setpass_t.3
%{_mandir}/man3/sasl_client_init.3
%{_mandir}/man3/sasl_verifyfile_t.3
%{_mandir}/man3/sasl_authorize_t.3
%{_mandir}/man3/sasl_auxprop_getctx.3
%{_mandir}/man3/sasl.3
%{_mandir}/man3/sasl_auxprop.3
%{_mandir}/man3/sasl_idle.3
%{_mandir}/man3/sasl_getpath_t.3
%{_mandir}/man3/sasl_listmech.3
%{_mandir}/man3/sasl_user_exists.3
%{_mandir}/man3/sasl_client_start.3
%{_mandir}/man3/sasl_server_step.3
%{_mandir}/man3/sasl_callbacks.3
%{_mandir}/man3/sasl_dispose.3
%{_mandir}/man3/sasl_getconfpath_t.3
%{_mandir}/man3/sasl_server_userdb_checkpass_t.3
%{_mandir}/man3/sasl_log_t.3
%{_mandir}/man3/sasl_client_step.3
%{_mandir}/man3/sasl_errors.3
%{_mandir}/man3/sasl_getprop.3
%{_mandir}/man3/sasl_setprop.3
%dir %{_prefix}/include
%dir %{_prefix}/include/sasl
%{_prefix}/include/sasl/saslplug.h
%{_prefix}/include/sasl/md5.h
%{_prefix}/include/sasl/prop.h
%{_prefix}/include/sasl/md5global.h
%{_prefix}/include/sasl/sasl.h
%{_prefix}/include/sasl/saslutil.h
%{_prefix}/include/sasl/hmac-md5.h

%changelog
* Fri May 31 2009 - jlee@thestaticvoid.com
- Initial version
