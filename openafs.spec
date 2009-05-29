%include Solaris.inc

%ifarch amd64
%include arch64.inc
%define sysname sunamd64_511
%use openafs_64 = openafs-base.spec
%endif
%include base.inc
%define sysname sunx86_511
%use openafs = openafs-base.spec

Name:		openafs
Version:	%{openafs.version}
Release:	1
Summary:	openafs
License:	GPL
Group:		Applications/Sound and Video
Packager:       James Lee <jlee@thestaticvoid.org>
Vendor:		http://openafs.org/dl/openafs/%{version}/openafs-%{version}-src.tar.bz2
Url:		http://www.openafs.org/
SUNW_Hotline:   %{url}
SUNW_Copyright:	%{name}.copyright
SUNW_Category:  application

%include default-depend.inc

%description
openafs

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64
mkdir %{name}-%{version}/%{_arch64}
%openafs_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%openafs.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64
%openafs_64.build -d %{name}-%{version}/%{_arch64}
%endif
%openafs.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64
%openafs_64.install -d %{name}-%{version}/%{_arch64}

mkdir $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libexecdir}/openafs/buserver $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libexecdir}/openafs/fileserver $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libexecdir}/openafs/kaserver $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libexecdir}/openafs/ptserver $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libexecdir}/openafs/salvager $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libexecdir}/openafs/upclient $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libexecdir}/openafs/upserver $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libexecdir}/openafs/vfsck $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libexecdir}/openafs/vlserver $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libexecdir}/openafs/volserver $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{_arch64}

mkdir -p $RPM_BUILD_ROOT/kernel/fs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/openafs/libafs64.nonfs.o $RPM_BUILD_ROOT/kernel/fs/%{_arch64}/afs
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/openafs
%endif
%openafs.install -d %{name}-%{version}/%{base_arch}

mkdir -p $RPM_BUILD_ROOT/kernel/fs
mv $RPM_BUILD_ROOT%{_libdir}/openafs/libafs.nonfs.o $RPM_BUILD_ROOT/kernel/fs/afs
rm -f $RPM_BUILD_ROOT%{_libdir}/openafs/libafs64.nonfs.o

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
for i in afsmonitor aklog asetkey bos cmdebug compile_et dlog dpass fs klog klog.krb klog.krb5 knfs kpasswd kpwvalid livesys pagsh pagsh.krb pts rxgen scout sys tokens tokens.krb translate_et udebug unlog up xstat_cm_test xstat_fs_test; do
	mv $i %{base_isa}/
	ln -s ../lib/isaexec $i
done

mkdir $RPM_BUILD_ROOT%{_sbindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_sbindir}
for i in afsd backup bosserver bos_util butc copyauth fms fs_conv_sol26 fstrace kadb_check ka-forwarder kas kdb kpwvalid prdb_check pt_util read_tape restorevol rmtsysd rxdebug uss vldb_check vldb_convert voldump volinfo vos vsys; do
	mv $i %{base_isa}/
	ln -s ../lib/isaexec $i
done

mkdir $RPM_BUILD_ROOT%{_libexecdir}/openafs/%{base_isa}
cd $RPM_BUILD_ROOT%{_libexecdir}/openafs
for i in buserver fileserver kaserver ptserver salvager upclient upserver vfsck vlserver volserver; do
	mv $i %{base_isa}/
	ln -s ../../lib/isaexec $i
done
%endif

%files
%defattr(-,root,bin)

%attr(755,root,sys) %dir %{_prefix}

%attr(755,root,sys) %dir /kernel
%attr(755,root,sys) %dir /kernel/fs
%attr(755,root,sys) /kernel/fs/afs

%ifarch amd64 sparcv9
%attr(755,root,sys) %dir /kernel/fs/amd64
%attr(755,root,sys) /kernel/fs/%{_arch64}/afs

%{_bindir}/%{_arch64}/afsmonitor
%{_bindir}/%{_arch64}/aklog
%{_bindir}/%{_arch64}/asetkey
%{_bindir}/%{_arch64}/bos
%{_bindir}/%{_arch64}/cmdebug
%{_bindir}/%{_arch64}/compile_et
%{_bindir}/%{_arch64}/dlog
%{_bindir}/%{_arch64}/dpass
%{_bindir}/%{_arch64}/fs
%{_bindir}/%{_arch64}/klog
%{_bindir}/%{_arch64}/klog.krb
%{_bindir}/%{_arch64}/klog.krb5
%{_bindir}/%{_arch64}/knfs
%{_bindir}/%{_arch64}/kpasswd
%{_bindir}/%{_arch64}/kpwvalid
%{_bindir}/%{_arch64}/livesys
%{_bindir}/%{_arch64}/pagsh
%{_bindir}/%{_arch64}/pagsh.krb
%{_bindir}/%{_arch64}/pts
%{_bindir}/%{_arch64}/rxgen
%{_bindir}/%{_arch64}/scout
%{_bindir}/%{_arch64}/sys
%{_bindir}/%{_arch64}/tokens
%{_bindir}/%{_arch64}/tokens.krb
%{_bindir}/%{_arch64}/translate_et
%{_bindir}/%{_arch64}/udebug
%{_bindir}/%{_arch64}/unlog
%{_bindir}/%{_arch64}/up
%{_bindir}/%{_arch64}/xstat_cm_test
%{_bindir}/%{_arch64}/xstat_fs_test

%{_sbindir}/%{_arch64}/afsd
%{_sbindir}/%{_arch64}/backup
%{_sbindir}/%{_arch64}/bosserver
%{_sbindir}/%{_arch64}/bos_util
%{_sbindir}/%{_arch64}/butc
%{_sbindir}/%{_arch64}/copyauth
%{_sbindir}/%{_arch64}/fms
%{_sbindir}/%{_arch64}/fs_conv_sol26
%{_sbindir}/%{_arch64}/fstrace
%{_sbindir}/%{_arch64}/kadb_check
%{_sbindir}/%{_arch64}/ka-forwarder
%{_sbindir}/%{_arch64}/kas
%{_sbindir}/%{_arch64}/kdb
%{_sbindir}/%{_arch64}/kpwvalid
%{_sbindir}/%{_arch64}/prdb_check
%{_sbindir}/%{_arch64}/pt_util
%{_sbindir}/%{_arch64}/read_tape
%{_sbindir}/%{_arch64}/restorevol
%{_sbindir}/%{_arch64}/rmtsysd
%{_sbindir}/%{_arch64}/rxdebug
%{_sbindir}/%{_arch64}/uss
%{_sbindir}/%{_arch64}/vldb_check
%{_sbindir}/%{_arch64}/vldb_convert
%{_sbindir}/%{_arch64}/voldump
%{_sbindir}/%{_arch64}/volinfo
%{_sbindir}/%{_arch64}/vos
%{_sbindir}/%{_arch64}/vsys

%{_libexecdir}/openafs/%{_arch64}/buserver
%{_libexecdir}/openafs/%{_arch64}/fileserver
%{_libexecdir}/openafs/%{_arch64}/kaserver
%{_libexecdir}/openafs/%{_arch64}/ptserver
%{_libexecdir}/openafs/%{_arch64}/salvager
%{_libexecdir}/openafs/%{_arch64}/upclient
%{_libexecdir}/openafs/%{_arch64}/upserver
%{_libexecdir}/openafs/%{_arch64}/vfsck
%{_libexecdir}/openafs/%{_arch64}/vlserver
%{_libexecdir}/openafs/%{_arch64}/volserver

%{_libdir}/%{_arch64}/afs/libacl.a
%{_libdir}/%{_arch64}/afs/libafsadminutil.a
%{_libdir}/%{_arch64}/afs/libafsint.a
%{_libdir}/%{_arch64}/afs/libafsutil.a
%{_libdir}/%{_arch64}/afs/libaudit.a
%{_libdir}/%{_arch64}/afs/libauth.a
%{_libdir}/%{_arch64}/afs/libauth.krb.a
%{_libdir}/%{_arch64}/afs/libbos.a
%{_libdir}/%{_arch64}/afs/libbosadmin.a
%{_libdir}/%{_arch64}/afs/libbubasics.a
%{_libdir}/%{_arch64}/afs/libbudb.a
%{_libdir}/%{_arch64}/afs/libbutm.a
%{_libdir}/%{_arch64}/afs/libbxdb.a
%{_libdir}/%{_arch64}/afs/libcfgadmin.a
%{_libdir}/%{_arch64}/afs/libclientadmin.a
%{_libdir}/%{_arch64}/afs/libcmd64.a
%{_libdir}/%{_arch64}/afs/libcmd.a
%{_libdir}/%{_arch64}/afs/libcom_err.a
%{_libdir}/%{_arch64}/afs/libdir.a
%{_libdir}/%{_arch64}/afs/libfsprobe.a
%{_libdir}/%{_arch64}/afs/libgtx.a
%{_libdir}/%{_arch64}/afs/libkasadmin.a
%{_libdir}/%{_arch64}/afs/libkauth.a
%{_libdir}/%{_arch64}/afs/libkauth.krb.a
%{_libdir}/%{_arch64}/afs/libnull.a
%{_libdir}/%{_arch64}/afs/libprocmgmt.a
%{_libdir}/%{_arch64}/afs/libprot.a
%{_libdir}/%{_arch64}/afs/libptsadmin.a
%{_libdir}/%{_arch64}/afs/libsys.a
%{_libdir}/%{_arch64}/afs/libusd.a
%{_libdir}/%{_arch64}/afs/libvldb.a
%{_libdir}/%{_arch64}/afs/libvlib.a
%{_libdir}/%{_arch64}/afs/libvolser.a
%{_libdir}/%{_arch64}/afs/libvosadmin.a
%{_libdir}/%{_arch64}/afs/libxstat_cm.a
%{_libdir}/%{_arch64}/afs/libxstat_fs.a
%{_libdir}/%{_arch64}/afs/util.a
%{_libdir}/%{_arch64}/afs/vlib.a
%{_libdir}/%{_arch64}/libafsauthent.a
%{_libdir}/%{_arch64}/libafsauthent.so
%{_libdir}/%{_arch64}/libafsauthent.so.1
%{_libdir}/%{_arch64}/libafsauthent.so.1.0
%{_libdir}/%{_arch64}/libafsrpc.a
%{_libdir}/%{_arch64}/libafsrpc.so
%{_libdir}/%{_arch64}/libafsrpc.so.1
%{_libdir}/%{_arch64}/libafsrpc.so.1.1
%{_libdir}/%{_arch64}/libafssetpag.so
%{_libdir}/%{_arch64}/libafssetpag.so.1
%{_libdir}/%{_arch64}/libafssetpag.so.1.0
%{_libdir}/%{_arch64}/libdes.a
%{_libdir}/%{_arch64}/libjuafs.a
%{_libdir}/%{_arch64}/liblwp.a
%{_libdir}/%{_arch64}/librx.a
%{_libdir}/%{_arch64}/librxkad.a
%{_libdir}/%{_arch64}/librxstat.a
%{_libdir}/%{_arch64}/libuafs.a
%{_libdir}/%{_arch64}/libubik.a
%{_libdir}/%{_arch64}/pam_afs.krb.so.1
%{_libdir}/%{_arch64}/pam_afs.so.1
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/afsmonitor
%{_bindir}/%{base_isa}/aklog
%{_bindir}/%{base_isa}/asetkey
%{_bindir}/%{base_isa}/bos
%{_bindir}/%{base_isa}/cmdebug
%{_bindir}/%{base_isa}/compile_et
%{_bindir}/%{base_isa}/dlog
%{_bindir}/%{base_isa}/dpass
%{_bindir}/%{base_isa}/fs
%{_bindir}/%{base_isa}/klog
%{_bindir}/%{base_isa}/klog.krb
%{_bindir}/%{base_isa}/klog.krb5
%{_bindir}/%{base_isa}/knfs
%{_bindir}/%{base_isa}/kpasswd
%{_bindir}/%{base_isa}/kpwvalid
%{_bindir}/%{base_isa}/livesys
%{_bindir}/%{base_isa}/pagsh
%{_bindir}/%{base_isa}/pagsh.krb
%{_bindir}/%{base_isa}/pts
%{_bindir}/%{base_isa}/rxgen
%{_bindir}/%{base_isa}/scout
%{_bindir}/%{base_isa}/sys
%{_bindir}/%{base_isa}/tokens
%{_bindir}/%{base_isa}/tokens.krb
%{_bindir}/%{base_isa}/translate_et
%{_bindir}/%{base_isa}/udebug
%{_bindir}/%{base_isa}/unlog
%{_bindir}/%{base_isa}/up
%{_bindir}/%{base_isa}/xstat_cm_test
%{_bindir}/%{base_isa}/xstat_fs_test
%hard %{_bindir}/afsmonitor
%hard %{_bindir}/aklog
%hard %{_bindir}/asetkey
%hard %{_bindir}/bos
%hard %{_bindir}/cmdebug
%hard %{_bindir}/compile_et
%hard %{_bindir}/dlog
%hard %{_bindir}/dpass
%hard %{_bindir}/fs
%hard %{_bindir}/klog
%hard %{_bindir}/klog.krb
%hard %{_bindir}/klog.krb5
%hard %{_bindir}/knfs
%hard %{_bindir}/kpasswd
%hard %{_bindir}/kpwvalid
%hard %{_bindir}/livesys
%hard %{_bindir}/pagsh
%hard %{_bindir}/pagsh.krb
%hard %{_bindir}/pts
%hard %{_bindir}/rxgen
%hard %{_bindir}/scout
%hard %{_bindir}/sys
%hard %{_bindir}/tokens
%hard %{_bindir}/tokens.krb
%hard %{_bindir}/translate_et
%hard %{_bindir}/udebug
%hard %{_bindir}/unlog
%hard %{_bindir}/up
%hard %{_bindir}/xstat_cm_test
%hard %{_bindir}/xstat_fs_test

%{_sbindir}/%{base_isa}/afsd
%{_sbindir}/%{base_isa}/backup
%{_sbindir}/%{base_isa}/bosserver
%{_sbindir}/%{base_isa}/bos_util
%{_sbindir}/%{base_isa}/butc
%{_sbindir}/%{base_isa}/copyauth
%{_sbindir}/%{base_isa}/fms
%{_sbindir}/%{base_isa}/fs_conv_sol26
%{_sbindir}/%{base_isa}/fstrace
%{_sbindir}/%{base_isa}/kadb_check
%{_sbindir}/%{base_isa}/ka-forwarder
%{_sbindir}/%{base_isa}/kas
%{_sbindir}/%{base_isa}/kdb
%{_sbindir}/%{base_isa}/kpwvalid
%{_sbindir}/%{base_isa}/prdb_check
%{_sbindir}/%{base_isa}/pt_util
%{_sbindir}/%{base_isa}/read_tape
%{_sbindir}/%{base_isa}/restorevol
%{_sbindir}/%{base_isa}/rmtsysd
%{_sbindir}/%{base_isa}/rxdebug
%{_sbindir}/%{base_isa}/uss
%{_sbindir}/%{base_isa}/vldb_check
%{_sbindir}/%{base_isa}/vldb_convert
%{_sbindir}/%{base_isa}/voldump
%{_sbindir}/%{base_isa}/volinfo
%{_sbindir}/%{base_isa}/vos
%{_sbindir}/%{base_isa}/vsys
%hard %{_sbindir}/afsd
%hard %{_sbindir}/backup
%hard %{_sbindir}/bosserver
%hard %{_sbindir}/bos_util
%hard %{_sbindir}/butc
%hard %{_sbindir}/copyauth
%hard %{_sbindir}/fms
%hard %{_sbindir}/fs_conv_sol26
%hard %{_sbindir}/fstrace
%hard %{_sbindir}/kadb_check
%hard %{_sbindir}/ka-forwarder
%hard %{_sbindir}/kas
%hard %{_sbindir}/kdb
%hard %{_sbindir}/kpwvalid
%hard %{_sbindir}/prdb_check
%hard %{_sbindir}/pt_util
%hard %{_sbindir}/read_tape
%hard %{_sbindir}/restorevol
%hard %{_sbindir}/rmtsysd
%hard %{_sbindir}/rxdebug
%hard %{_sbindir}/uss
%hard %{_sbindir}/vldb_check
%hard %{_sbindir}/vldb_convert
%hard %{_sbindir}/voldump
%hard %{_sbindir}/volinfo
%hard %{_sbindir}/vos
%hard %{_sbindir}/vsys

%{_libexecdir}/openafs/%{base_isa}/buserver
%{_libexecdir}/openafs/%{base_isa}/fileserver
%{_libexecdir}/openafs/%{base_isa}/kaserver
%{_libexecdir}/openafs/%{base_isa}/ptserver
%{_libexecdir}/openafs/%{base_isa}/salvager
%{_libexecdir}/openafs/%{base_isa}/upclient
%{_libexecdir}/openafs/%{base_isa}/upserver
%{_libexecdir}/openafs/%{base_isa}/vfsck
%{_libexecdir}/openafs/%{base_isa}/vlserver
%{_libexecdir}/openafs/%{base_isa}/volserver
%hard %{_libexecdir}/openafs/buserver
%hard %{_libexecdir}/openafs/fileserver
%hard %{_libexecdir}/openafs/kaserver
%hard %{_libexecdir}/openafs/ptserver
%hard %{_libexecdir}/openafs/salvager
%hard %{_libexecdir}/openafs/upclient
%hard %{_libexecdir}/openafs/upserver
%hard %{_libexecdir}/openafs/vfsck
%hard %{_libexecdir}/openafs/vlserver
%hard %{_libexecdir}/openafs/volserver
%else
%{_bindir}/afsmonitor
%{_bindir}/aklog
%{_bindir}/asetkey
%{_bindir}/bos
%{_bindir}/cmdebug
%{_bindir}/compile_et
%{_bindir}/dlog
%{_bindir}/dpass
%{_bindir}/fs
%{_bindir}/klog
%{_bindir}/klog.krb
%{_bindir}/klog.krb5
%{_bindir}/knfs
%{_bindir}/kpasswd
%{_bindir}/kpwvalid
%{_bindir}/livesys
%{_bindir}/pagsh
%{_bindir}/pagsh.krb
%{_bindir}/pts
%{_bindir}/rxgen
%{_bindir}/scout
%{_bindir}/sys
%{_bindir}/tokens
%{_bindir}/tokens.krb
%{_bindir}/translate_et
%{_bindir}/udebug
%{_bindir}/unlog
%{_bindir}/up
%{_bindir}/xstat_cm_test
%{_bindir}/xstat_fs_test

%{_sbindir}/afsd
%{_sbindir}/backup
%{_sbindir}/bosserver
%{_sbindir}/bos_util
%{_sbindir}/butc
%{_sbindir}/copyauth
%{_sbindir}/fms
%{_sbindir}/fs_conv_sol26
%{_sbindir}/fstrace
%{_sbindir}/kadb_check
%{_sbindir}/ka-forwarder
%{_sbindir}/kas
%{_sbindir}/kdb
%{_sbindir}/kpwvalid
%{_sbindir}/prdb_check
%{_sbindir}/pt_util
%{_sbindir}/read_tape
%{_sbindir}/restorevol
%{_sbindir}/rmtsysd
%{_sbindir}/rxdebug
%{_sbindir}/uss
%{_sbindir}/vldb_check
%{_sbindir}/vldb_convert
%{_sbindir}/voldump
%{_sbindir}/volinfo
%{_sbindir}/vos
%{_sbindir}/vsys

%{_libexecdir}/openafs/buserver
%{_libexecdir}/openafs/fileserver
%{_libexecdir}/openafs/kaserver
%{_libexecdir}/openafs/ptserver
%{_libexecdir}/openafs/salvager
%{_libexecdir}/openafs/upclient
%{_libexecdir}/openafs/upserver
%{_libexecdir}/openafs/vfsck
%{_libexecdir}/openafs/vlserver
%{_libexecdir}/openafs/volserver
%endif

%{_libdir}/afs/libacl.a
%{_libdir}/afs/libafsadminutil.a
%{_libdir}/afs/libafsint.a
%{_libdir}/afs/libafsutil.a
%{_libdir}/afs/libaudit.a
%{_libdir}/afs/libauth.a
%{_libdir}/afs/libauth.krb.a
%{_libdir}/afs/libbos.a
%{_libdir}/afs/libbosadmin.a
%{_libdir}/afs/libbubasics.a
%{_libdir}/afs/libbudb.a
%{_libdir}/afs/libbutm.a
%{_libdir}/afs/libbxdb.a
%{_libdir}/afs/libcfgadmin.a
%{_libdir}/afs/libclientadmin.a
%{_libdir}/afs/libcmd64.a
%{_libdir}/afs/libcmd.a
%{_libdir}/afs/libcom_err.a
%{_libdir}/afs/libdir.a
%{_libdir}/afs/libfsprobe.a
%{_libdir}/afs/libgtx.a
%{_libdir}/afs/libkasadmin.a
%{_libdir}/afs/libkauth.a
%{_libdir}/afs/libkauth.krb.a
%{_libdir}/afs/libnull.a
%{_libdir}/afs/libprocmgmt.a
%{_libdir}/afs/libprot.a
%{_libdir}/afs/libptsadmin.a
%{_libdir}/afs/libsys.a
%{_libdir}/afs/libusd.a
%{_libdir}/afs/libvldb.a
%{_libdir}/afs/libvlib.a
%{_libdir}/afs/libvolser.a
%{_libdir}/afs/libvosadmin.a
%{_libdir}/afs/libxstat_cm.a
%{_libdir}/afs/libxstat_fs.a
%{_libdir}/afs/util.a
%{_libdir}/afs/vlib.a
%{_libdir}/libafsauthent.a
%{_libdir}/libafsauthent.so
%{_libdir}/libafsauthent.so.1
%{_libdir}/libafsauthent.so.1.0
%{_libdir}/libafsrpc.a
%{_libdir}/libafsrpc.so
%{_libdir}/libafsrpc.so.1
%{_libdir}/libafsrpc.so.1.1
%{_libdir}/libafssetpag.so
%{_libdir}/libafssetpag.so.1
%{_libdir}/libafssetpag.so.1.0
%{_libdir}/libdes.a
%{_libdir}/libjuafs.a
%{_libdir}/liblwp.a
%{_libdir}/librx.a
%{_libdir}/librxkad.a
%{_libdir}/librxstat.a
%{_libdir}/libuafs.a
%{_libdir}/libubik.a
%{_libdir}/pam_afs.krb.so.1
%{_libdir}/pam_afs.so.1

%{_includedir}/afs/acl.h
%{_includedir}/afs/afs_Admin.h
%{_includedir}/afs/afs_args.h
%{_includedir}/afs/afs_atomlist.h
%{_includedir}/afs/afs_bosAdmin.h
%{_includedir}/afs/afscbint.h
%{_includedir}/afs/afs_cfgAdmin.h
%{_includedir}/afs/afs_clientAdmin.h
%{_includedir}/afs/afs.h
%{_includedir}/afs/afsint.h
%{_includedir}/afs/afs_kasAdmin.h
%{_includedir}/afs/afs_lhash.h
%{_includedir}/afs/afs_ptsAdmin.h
%{_includedir}/afs/afs_stats.h
%{_includedir}/afs/afssyscalls.h
%{_includedir}/afs/afs_sysnames.h
%{_includedir}/afs/afs_utilAdmin.h
%{_includedir}/afs/afsutil.h
%{_includedir}/afs/afsutil_prototypes.h
%{_includedir}/afs/afs_vosAdmin.h
%{_includedir}/afs/assert.h
%{_includedir}/afs/audit.h
%{_includedir}/afs/auth.h
%{_includedir}/afs/bnode.h
%{_includedir}/afs/bosint.h
%{_includedir}/afs/bubasics.h
%{_includedir}/afs/budb_client.h
%{_includedir}/afs/budb_errs.h
%{_includedir}/afs/budb.h
%{_includedir}/afs/bumon.h
%{_includedir}/afs/butc.h
%{_includedir}/afs/butm.h
%{_includedir}/afs/butx.h
%{_includedir}/afs/cellconfig.h
%{_includedir}/afs/cmd.h
%{_includedir}/afs/cnvldb.h
%{_includedir}/afs/com_err.h
%{_includedir}/afs/debug.h
%{_includedir}/afs/dir.h
%{_includedir}/afs/dirpath.h
%{_includedir}/afs/errors.h
%{_includedir}/afs/error_table.h
%{_includedir}/afs/exporter.h
%{_includedir}/afs/fileutil.h
%{_includedir}/afs/fsprobe.h
%{_includedir}/afs/fs_stats.h
%{_includedir}/afs/fssync.h
%{_includedir}/afs/gtxcurseswin.h
%{_includedir}/afs/gtxdumbwin.h
%{_includedir}/afs/gtxframe.h
%{_includedir}/afs/gtxinput.h
%{_includedir}/afs/gtxkeymap.h
%{_includedir}/afs/gtxlightobj.h
%{_includedir}/afs/gtxobjdict.h
%{_includedir}/afs/gtxobjects.h
%{_includedir}/afs/gtxtextcb.h
%{_includedir}/afs/gtxtextobj.h
%{_includedir}/afs/gtxwindows.h
%{_includedir}/afs/gtxX11win.h
%{_includedir}/afs/icl.h
%{_includedir}/afs/ihandle.h
%{_includedir}/afs/kaport.h
%{_includedir}/afs/kauth.h
%{_includedir}/afs/kautils.h
%{_includedir}/afs/keys.h
%{_includedir}/afs/ktc.h
%{_includedir}/afs/ktime.h
%{_includedir}/afs/mit-sipb-cr.h
%{_includedir}/afs/namei_ops.h
%{_includedir}/afs/netutils.h
%{_includedir}/afs/nfsclient.h
%{_includedir}/afs/nfs.h
%{_includedir}/afs/osi_inode.h
%{_includedir}/afs/packages.h
%{_includedir}/afs/param.h
%{_includedir}/afs/partition.h
%{_includedir}/afs/prclient.h
%{_includedir}/afs/prerror.h
%{_includedir}/afs/print.h
%{_includedir}/afs/procmgmt.h
%{_includedir}/afs/prserver.h
%{_includedir}/afs/prs_fs.h
%{_includedir}/afs/ptclient.h
%{_includedir}/afs/pterror.h
%{_includedir}/afs/pthread_glock.h
%{_includedir}/afs/pthread_nosigs.h
%{_includedir}/afs/ptint.h
%{_includedir}/afs/ptserver.h
%{_includedir}/afs/ptuser.h
%{_includedir}/afs/remote.h
%{_includedir}/afs/rxgen_consts.h
%{_includedir}/afs/softsig.h
%{_includedir}/afs/stds.h
%{_includedir}/afs/sysctl.h
%{_includedir}/afs/tcdata.h
%{_includedir}/afs/unified_afs.h
%{_includedir}/afs/usd.h
%{_includedir}/afs/venus.h
%{_includedir}/afs/vice.h
%{_includedir}/afs/viceinode.h
%{_includedir}/afs/vldbint.h
%{_includedir}/afs/vl_opcodes.h
%{_includedir}/afs/vlserver.h
%{_includedir}/afs/vnode.h
%{_includedir}/afs/voldefs.h
%{_includedir}/afs/volint.h
%{_includedir}/afs/volser.h
%{_includedir}/afs/volume.h
%{_includedir}/afs/xfsattrs.h
%{_includedir}/afs/xstat_cm.h
%{_includedir}/afs/xstat_fs.h
%{_includedir}/des_conf.h
%{_includedir}/des.h
%{_includedir}/des_odd.h
%{_includedir}/des_prototypes.h
%{_includedir}/lock.h
%{_includedir}/lwp.h
%{_includedir}/mit-cpyright.h
%{_includedir}/potpourri.h
%{_includedir}/preempt.h
%{_includedir}/rx/fcrypt.h
%{_includedir}/rx/rx_clock.h
%{_includedir}/rx/rx_event.h
%{_includedir}/rx/rx_globals.h
%{_includedir}/rx/rx.h
%{_includedir}/rx/rxkad.h
%{_includedir}/rx/rxkad_prototypes.h
%{_includedir}/rx/rx_lwp.h
%{_includedir}/rx/rx_misc.h
%{_includedir}/rx/rx_multi.h
%{_includedir}/rx/rx_null.h
%{_includedir}/rx/rx_packet.h
%{_includedir}/rx/rx_prototypes.h
%{_includedir}/rx/rx_pthread.h
%{_includedir}/rx/rx_queue.h
%{_includedir}/rx/rxstat.h
%{_includedir}/rx/rx_user.h
%{_includedir}/rx/xdr.h
%{_includedir}/rx/xdr_prototypes.h
%{_includedir}/timer.h
%{_includedir}/ubik.h
%{_includedir}/ubik_int.h

