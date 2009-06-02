#
# spec file for package: courier-authlib
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		courier-authlib
Version:	0.62.2
Summary:	Courier Authentication Library
License:	GPLv3
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.courier-mta.org/authlib/
SUNW_BaseDir:   /
SUNW_Copyright: %{name}.copyright

Source0:	http://voxel.dl.sourceforge.net/sourceforge/courier/%{name}-%{version}.tar.bz2
Source1:	authdaemond.xml

%include default-depend.inc
BuildRequires:	SUNWexpect
BuildRequires:	bdb
Requires:	SUNWexpect
Requires:	bdb

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Sam Varshavchik <mrsam@courier-mta.com>
Meta(info.upstream_url):	http://www.courier-mta.org/authlib/
Meta(info.classification):	org.opensolaris.category.2008:System/Services

%description
The Courier authentication library provides authentication services for other
Courier applications. 

This package contains authdaemond and shared libraries.

%package devel
Summary:	Headers for courier-authlib
Requires:	%{name}

%description devel
The Courier authentication library provides authentication services for other
Courier applications. 

This package contains the courier-authlib development files.

%prep
%setup -q
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --libexecdir=%{_libexecdir} --with-authdaemonvar=%{_localstatedir}/lib/authdaemon --with-db=db

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
cp sysconftool $RPM_BUILD_ROOT%{_libexecdir}/courier-authlib
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network
cp %{SOURCE1} $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network/authdaemond.xml

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%files
%defattr(-,root,bin)
%attr(755,root,sys) %dir %{_prefix}
%dir %{_bindir}
%{_bindir}/courierauthconfig
%dir %{_libdir}
%dir %{_libdir}/courier-authlib
%{_libdir}/courier-authlib/libauthldap.so.0
%{_libdir}/courier-authlib/libcourierauthsasl.so.0
%{_libdir}/courier-authlib/libcourierauthcommon.so.0
%{_libdir}/courier-authlib/libauthpipe.so.0
%{_libdir}/courier-authlib/sysconftool
%{_libdir}/courier-authlib/authsystem.passwd
%{_libdir}/courier-authlib/libauthpam.so.0
%{_libdir}/courier-authlib/libcourierauth.so.0
%{_libdir}/courier-authlib/makedatprog
%{_libdir}/courier-authlib/authdaemond
%{_libdir}/courier-authlib/libauthuserdb.so.0
%{_libdir}/courier-authlib/libauthcustom.so.0
%{_libdir}/courier-authlib/libcourierauthsaslclient.so.0
%attr(755,root,sys) %dir %{_datadir}
%dir %{_mandir}
%dir %{_mandir}/man1
%dir %{_mandir}/man8
%{_mandir}/man1/courierlogger.1
%{_mandir}/man1/authpasswd.1
%{_mandir}/man1/authtest.1
%{_mandir}/man8/makeuserdb.8
%{_mandir}/man8/userdb.8
%{_mandir}/man8/userdbpw.8
%dir %{_sbindir}
%{_sbindir}/makeuserdb
%{_sbindir}/authdaemond
%{_sbindir}/userdbpw
%{_sbindir}/userdb
%{_sbindir}/authtest
%{_sbindir}/authpasswd
%{_sbindir}/authenumerate
%{_sbindir}/userdb-test-cram-md5
%{_sbindir}/pw2userdb
%{_sbindir}/courierlogger
%defattr(-,root,sys)
%dir %{_sysconfdir}
%dir %{_sysconfdir}/authlib
%{_sysconfdir}/authlib/authdaemonrc.dist
%{_sysconfdir}/authlib/authldaprc.dist
%dir %{_localstatedir}
%attr(755,root,other) %dir %{_localstatedir}/lib
%attr(755,root,other) %dir %{_localstatedir}/lib/authdaemon
%dir %{_localstatedir}/svc
%dir %{_localstatedir}/svc/manifest
%dir %{_localstatedir}/svc/manifest/network
%class(manifest) %attr(444,root,sys) %{_localstatedir}/svc/manifest/network/authdaemond.xml

%files devel
%defattr(-,root,bin)
%attr(755,root,sys) %dir %{_prefix}
%dir %{_libdir}
%dir %{_libdir}/courier-authlib
%{_libdir}/courier-authlib/libauthpipe.a
%{_libdir}/courier-authlib/libauthcustom.a
%{_libdir}/courier-authlib/libauthcustom.so
%{_libdir}/courier-authlib/libauthuserdb.so
%{_libdir}/courier-authlib/libcourierauthsaslclient.a
%{_libdir}/courier-authlib/libcourierauthsaslclient.la
%{_libdir}/courier-authlib/libcourierauthcommon.la
%{_libdir}/courier-authlib/libcourierauthcommon.so
%{_libdir}/courier-authlib/libcourierauthsaslclient.so
%{_libdir}/courier-authlib/libauthuserdb.la
%{_libdir}/courier-authlib/libcourierauthcommon.a
%{_libdir}/courier-authlib/libauthcustom.la
%{_libdir}/courier-authlib/libauthldap.so
%{_libdir}/courier-authlib/libauthpipe.so
%{_libdir}/courier-authlib/libcourierauthsasl.la
%{_libdir}/courier-authlib/libauthpam.so
%{_libdir}/courier-authlib/libauthpam.a
%{_libdir}/courier-authlib/libcourierauth.so
%{_libdir}/courier-authlib/libauthldap.a
%{_libdir}/courier-authlib/libcourierauth.la
%{_libdir}/courier-authlib/libcourierauth.a
%{_libdir}/courier-authlib/libauthpipe.la
%{_libdir}/courier-authlib/libauthpam.la
%{_libdir}/courier-authlib/libcourierauthsasl.so
%{_libdir}/courier-authlib/libauthuserdb.a
%{_libdir}/courier-authlib/libauthldap.la
%{_libdir}/courier-authlib/libcourierauthsasl.a
%dir %{_mandir}
%dir %{_mandir}/man3
%{_mandir}/man3/auth_sasl.3
%{_mandir}/man3/auth_generic.3
%{_mandir}/man3/auth_getoption.3
%{_mandir}/man3/authlib.3
%{_mandir}/man3/auth_passwd.3
%{_mandir}/man3/auth_enumerate.3
%{_mandir}/man3/auth_login.3
%{_mandir}/man3/auth_sasl_ex.3
%{_mandir}/man3/auth_getuserinfo.3
%dir %{_prefix}/include
%{_prefix}/include/courierauth.h
%{_prefix}/include/courierauthdebug.h
%{_prefix}/include/courierauthsasl.h
%{_prefix}/include/courierauthsaslclient.h
%{_prefix}/include/courier_auth_config.h

%changelog
* Sun May 31 2009 - jlee@thestaticvoid.com
- Add header and correct copyright
* Sat May 30 2009 - jlee@thestaticvoid.com
- Initial version
