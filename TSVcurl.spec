%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use curl_64 = curl.spec
%endif
%include base.inc
%use curl = curl.spec

Name:		TSVcurl
Version:	%{curl.version}
Summary:	Command Line Tool for Transferring Files
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
Requires:	SUNWlibsasl
Requires:	SUNWopenssl-libraries
Requires:	SUNWpr
Requires:	SUNWtls
Requires:	SUNWzlib

%description
curl is a client to get documents/files from servers, using any of the
supported protocols. The command is designed to work without user
interaction or any kind of interactivity.

curl offers a busload of useful tricks like proxy support, user
authentication, ftp upload, HTTP post, file transfer resume and more.

This package contains the shared library.

%package devel
Summary:	Headers for curl
Requires:	%{name}

%description devel
curl is a client to get documents/files from servers, using any of the
supported protocols. The command is designed to work without user
interaction or any kind of interactivity.

curl offers a busload of useful tricks like proxy support, user
authentication, ftp upload, HTTP post, file transfer resume and more.

This package contains the curl development files. 

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%curl_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%curl.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%curl_64.build -d %{name}-%{version}/%{_arch64}
%endif
%curl.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%curl_64.install -d %{name}-%{version}/%{_arch64}
%endif
%curl.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/curl $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/curl-config $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec curl
ln -s ../lib/isaexec curl-config
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/curl
%{_libdir}/%{_arch64}/libcurl.so.4
%{_libdir}/%{_arch64}/libcurl.so.4.1.0
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/curl
%hard %{_bindir}/curl
%else
%{_bindir}/curl
%endif
%{_libdir}/libcurl.so.4
%{_libdir}/libcurl.so.4.1.0
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}/man1/curl.1

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/curl-config
%attr(755,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/libcurl.pc
%{_libdir}/%{_arch64}/libcurl.a
%{_libdir}/%{_arch64}/libcurl.so
%{_libdir}/%{_arch64}/libcurl.la
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/curl-config
%hard %{_bindir}/curl-config
%else
%{_bindir}/curl-config
%endif
%{_libdir}/libcurl.so
%{_libdir}/libcurl.la
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/libcurl.pc
%{_libdir}/libcurl.a
%{_includedir}/curl/curlbuild.h
%{_includedir}/curl/stdcheaders.h
%{_includedir}/curl/types.h
%{_includedir}/curl/curl.h
%{_includedir}/curl/curlver.h
%{_includedir}/curl/typecheck-gcc.h
%{_includedir}/curl/curlrules.h
%{_includedir}/curl/multi.h
%{_includedir}/curl/mprintf.h
%{_includedir}/curl/easy.h
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}/man1/curl-config.1
%{_mandir}/man3/libcurl-tutorial.3
%{_mandir}/man3/curl_version_info.3
%{_mandir}/man3/curl_multi_fdset.3
%{_mandir}/man3/curl_multi_remove_handle.3
%{_mandir}/man3/curl_easy_cleanup.3
%{_mandir}/man3/curl_multi_setopt.3
%{_mandir}/man3/curl_getenv.3
%{_mandir}/man3/curl_share_init.3
%{_mandir}/man3/curl_easy_recv.3
%{_mandir}/man3/curl_escape.3
%{_mandir}/man3/curl_easy_pause.3
%{_mandir}/man3/curl_formget.3
%{_mandir}/man3/libcurl-share.3
%{_mandir}/man3/curl_version.3
%{_mandir}/man3/curl_easy_setopt.3
%{_mandir}/man3/curl_multi_add_handle.3
%{_mandir}/man3/curl_multi_info_read.3
%{_mandir}/man3/curl_share_strerror.3
%{_mandir}/man3/curl_share_setopt.3
%{_mandir}/man3/curl_easy_send.3
%{_mandir}/man3/curl_easy_perform.3
%{_mandir}/man3/curl_share_cleanup.3
%{_mandir}/man3/curl_mprintf.3
%{_mandir}/man3/curl_formfree.3
%{_mandir}/man3/curl_easy_getinfo.3
%{_mandir}/man3/curl_global_init.3
%{_mandir}/man3/libcurl-easy.3
%{_mandir}/man3/curl_unescape.3
%{_mandir}/man3/curl_slist_free_all.3
%{_mandir}/man3/curl_easy_reset.3
%{_mandir}/man3/curl_global_init_mem.3
%{_mandir}/man3/libcurl-multi.3
%{_mandir}/man3/libcurl.3
%{_mandir}/man3/curl_easy_duphandle.3
%{_mandir}/man3/curl_multi_strerror.3
%{_mandir}/man3/curl_global_cleanup.3
%{_mandir}/man3/curl_strequal.3
%{_mandir}/man3/curl_multi_perform.3
%{_mandir}/man3/curl_slist_append.3
%{_mandir}/man3/curl_free.3
%{_mandir}/man3/curl_multi_socket.3
%{_mandir}/man3/curl_formadd.3
%{_mandir}/man3/curl_multi_assign.3
%{_mandir}/man3/curl_easy_escape.3
%{_mandir}/man3/curl_easy_strerror.3
%{_mandir}/man3/curl_multi_timeout.3
%{_mandir}/man3/curl_multi_cleanup.3
%{_mandir}/man3/curl_getdate.3
%{_mandir}/man3/curl_multi_init.3
%{_mandir}/man3/curl_easy_unescape.3
%{_mandir}/man3/curl_easy_init.3
%{_mandir}/man3/libcurl-errors.3
