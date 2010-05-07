#
# spec file for package: openafs
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch i386
%define sysname sunx86_511
%endif

Name:		openafs
Version:	1.4.12
Summary:	AFS Distributed Filesystem
License:	IPL
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.openafs.org/
SUNW_BaseDir:   %{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://www.openafs.org/dl/openafs/%{version}/openafs-%{version}-src.tar.bz2
Patch0:		openafs-00-lbolt.diff

%include default-depend.inc
BuildRequires:	SUNWggrp

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		OpenAFS <openafs-gatekeepers@openafs.org>
Meta(info.upstream_url):	http://www.openafs.org/
Meta(info.classification):	org.opensolaris.category.2008:System/File System

%description
AFS is a distributed filesystem allowing cross-platform sharing of files among
multiple computers. Facilities are provided for access control, authentication,
backup and administrative management.

%prep
%setup -q
%patch0

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --libexecdir=%{_libdir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --with-afs-sysname=%{sysname} --with-krb5-conf=/usr/bin/krb5-config --enable-namei-fileserver
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_prefix}/kernel/fs/%{_arch64}
mv $RPM_BUILD_ROOT%{_libdir}/openafs/libafs.nonfs.o $RPM_BUILD_ROOT%{_prefix}/kernel/fs/afs
mv $RPM_BUILD_ROOT%{_libdir}/openafs/libafs64.nonfs.o $RPM_BUILD_ROOT%{_prefix}/kernel/fs/%{_arch64}/afs
rm $RPM_BUILD_ROOT%{_libdir}/openafs/libafs*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{_bindir}/sys
%{_bindir}/afs_compile_et
%{_bindir}/rxgen
%{_bindir}/pagsh
%{_bindir}/pagsh.krb
%{_bindir}/udebug
%{_bindir}/pts
%{_bindir}/klog
%{_bindir}/klog.krb
%{_bindir}/knfs
%{_bindir}/kpasswd
%{_bindir}/kpwvalid
%{_bindir}/restorevol
%{_bindir}/bos
%{_bindir}/unlog
%{_bindir}/tokens
%{_bindir}/tokens.krb
%{_bindir}/scout
%{_bindir}/livesys
%{_bindir}/fs
%{_bindir}/up
%{_bindir}/cmdebug
%{_bindir}/xstat_fs_test
%{_bindir}/xstat_cm_test
%{_bindir}/afsmonitor
%{_bindir}/aklog
%{_bindir}/klog.krb5
%{_bindir}/asetkey
%{_bindir}/translate_et
%{_sbindir}/rmtsysd
%{_sbindir}/pt_util
%{_sbindir}/prdb_check
%{_sbindir}/kas
%{_sbindir}/kpwvalid
%{_sbindir}/kadb_check
%{_sbindir}/kdb
%{_sbindir}/ka-forwarder
%{_sbindir}/afsd
%{_sbindir}/vsys
%{_sbindir}/volinfo
%{_sbindir}/fssync-debug
%{_sbindir}/vldb_convert
%{_sbindir}/vldb_check
%{_sbindir}/state_analyzer
%{_sbindir}/voldump
%{_sbindir}/vos
%{_sbindir}/uss
%{_sbindir}/backup
%{_sbindir}/read_tape
%{_sbindir}/bosserver
%{_sbindir}/bos_util
%{_sbindir}/butc
%{_sbindir}/fms
%{_sbindir}/fstrace
%{_sbindir}/kdump
%{_sbindir}/rxdebug
%{_sbindir}/fs_conv_sol26
%{_libdir}/openafs/ptserver
%{_libdir}/openafs/kaserver
%{_libdir}/openafs/salvager
%{_libdir}/openafs/vlserver
%{_libdir}/openafs/fileserver
%{_libdir}/openafs/buserver
%{_libdir}/openafs/volserver
%{_libdir}/openafs/upserver
%{_libdir}/openafs/upclient
%{_libdir}/afs/libprocmgmt.a
%{_libdir}/afs/util.a
%{_libdir}/afs/libafsutil.a
%{_libdir}/afs/libcom_err.a
%{_libdir}/afs/libcmd.a
%{_libdir}/afs/libcmd64.a
%{_libdir}/afs/libafsint.a
%{_libdir}/afs/libaudit.a
%{_libdir}/afs/libauth.a
%{_libdir}/afs/libauth.krb.a
%{_libdir}/afs/libsys.a
%{_libdir}/afs/libprot.a
%{_libdir}/afs/libacl.a
%{_libdir}/afs/libkauth.a
%{_libdir}/afs/libkauth.krb.a
%{_libdir}/afs/libbubasics.a
%{_libdir}/afs/libusd.a
%{_libdir}/afs/libdir.a
%{_libdir}/afs/vlib.a
%{_libdir}/afs/libvlib.a
%{_libdir}/afs/libvldb.a
%{_libdir}/afs/libvolser.a
%{_libdir}/afs/libbutm.a
%{_libdir}/afs/libbudb.a
%{_libdir}/afs/libbxdb.a
%{_libdir}/afs/libbos.a
%{_libdir}/afs/libgtx.a
%{_libdir}/afs/libfsprobe.a
%{_libdir}/afs/libxstat_fs.a
%{_libdir}/afs/libxstat_cm.a
%{_libdir}/libdes.a
%{_libdir}/liblwp.a
%{_libdir}/librx.a
%{_libdir}/librxstat.a
%{_libdir}/librxkad.a
%{_libdir}/libubik.a
%{_libdir}/libafsrpc.a
%{_libdir}/libafsauthent.a
%{_libdir}/libuafs.a
%{_libdir}/libjuafs.a
%{_libdir}/libafsrpc.so.1.1
%{_libdir}/libafsrpc.so
%{_libdir}/libafsrpc.so.1
%{_libdir}/libafsrpc_pic.a
%{_libdir}/libafsauthent.so.1.1
%{_libdir}/libafsauthent.so
%{_libdir}/libafsauthent.so.1
%{_libdir}/libafsauthent_pic.a
%{_libdir}/libkopenafs.a
%{_libdir}/libkopenafs.so.1.0
%{_libdir}/libkopenafs.so
%{_libdir}/libkopenafs.so.1
%{_libdir}/pam_afs.so.1
%{_libdir}/pam_afs.krb.so.1
%{_includedir}/afs/param.h
%{_includedir}/afs/stds.h
%{_includedir}/afs/afs_sysnames.h
%{_includedir}/afs/afs_args.h
%{_includedir}/afs/icl.h
%{_includedir}/afs/venus.h
%{_includedir}/afs/vioc.h
%{_includedir}/afs/debug.h
%{_includedir}/afs/procmgmt.h
%{_includedir}/afs/dirpath.h
%{_includedir}/afs/pthread_nosigs.h
%{_includedir}/afs/assert.h
%{_includedir}/afs/errors.h
%{_includedir}/afs/vice.h
%{_includedir}/afs/remote.h
%{_includedir}/afs/ktime.h
%{_includedir}/afs/fileutil.h
%{_includedir}/afs/netutils.h
%{_includedir}/afs/packages.h
%{_includedir}/afs/afsutil.h
%{_includedir}/afs/afsutil_prototypes.h
%{_includedir}/afs/pthread_glock.h
%{_includedir}/afs/afs_atomlist.h
%{_includedir}/afs/afs_lhash.h
%{_includedir}/afs/softsig.h
%{_includedir}/afs/com_err.h
%{_includedir}/afs/error_table.h
%{_includedir}/afs/mit-sipb-cr.h
%{_includedir}/afs/cmd.h
%{_includedir}/afs/afs.h
%{_includedir}/afs/afs_consts.h
%{_includedir}/afs/afs_stats.h
%{_includedir}/afs/exporter.h
%{_includedir}/afs/nfsclient.h
%{_includedir}/afs/osi_inode.h
%{_includedir}/afs/sysctl.h
%{_includedir}/afs/unified_afs.h
%{_includedir}/afs/rxgen_consts.h
%{_includedir}/afs/afsint.h
%{_includedir}/afs/afscbint.h
%{_includedir}/afs/pagcb.h
%{_includedir}/afs/audit.h
%{_includedir}/afs/keys.h
%{_includedir}/afs/cellconfig.h
%{_includedir}/afs/auth.h
%{_includedir}/afs/ktc.h
%{_includedir}/afs/afssyscalls.h
%{_includedir}/afs/xfsattrs.h
%{_includedir}/afs/prclient.h
%{_includedir}/afs/prerror.h
%{_includedir}/afs/print.h
%{_includedir}/afs/prserver.h
%{_includedir}/afs/ptclient.h
%{_includedir}/afs/ptuser.h
%{_includedir}/afs/pterror.h
%{_includedir}/afs/ptint.h
%{_includedir}/afs/ptserver.h
%{_includedir}/afs/acl.h
%{_includedir}/afs/prs_fs.h
%{_includedir}/afs/kautils.h
%{_includedir}/afs/kauth.h
%{_includedir}/afs/kaport.h
%{_includedir}/afs/bumon.h
%{_includedir}/afs/butc.h
%{_includedir}/afs/bubasics.h
%{_includedir}/afs/tcdata.h
%{_includedir}/afs/butm.h
%{_includedir}/afs/butx.h
%{_includedir}/afs/usd.h
%{_includedir}/afs/dir.h
%{_includedir}/afs/nfs.h
%{_includedir}/afs/vnode.h
%{_includedir}/afs/vnode_inline.h
%{_includedir}/afs/viceinode.h
%{_includedir}/afs/volume.h
%{_includedir}/afs/volume_inline.h
%{_includedir}/afs/voldefs.h
%{_includedir}/afs/partition.h
%{_includedir}/afs/fssync.h
%{_includedir}/afs/salvsync.h
%{_includedir}/afs/daemon_com.h
%{_includedir}/afs/ihandle.h
%{_includedir}/afs/namei_ops.h
%{_includedir}/afs/vl_opcodes.h
%{_includedir}/afs/vlserver.h
%{_includedir}/afs/vldbint.h
%{_includedir}/afs/cnvldb.h
%{_includedir}/afs/fs_stats.h
%{_includedir}/afs/volser.h
%{_includedir}/afs/volint.h
%{_includedir}/afs/vsutils_prototypes.h
%{_includedir}/afs/budb.h
%{_includedir}/afs/budb_errs.h
%{_includedir}/afs/budb_client.h
%{_includedir}/afs/bosint.h
%{_includedir}/afs/bnode.h
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
%{_includedir}/afs/fsprobe.h
%{_includedir}/afs/xstat_fs.h
%{_includedir}/afs/xstat_cm.h
%{_includedir}/rx/rx_packet.h
%{_includedir}/rx/rx_prototypes.h
%{_includedir}/rx/rx.h
%{_includedir}/rx/rx_user.h
%{_includedir}/rx/rx_event.h
%{_includedir}/rx/rx_queue.h
%{_includedir}/rx/rx_globals.h
%{_includedir}/rx/rx_clock.h
%{_includedir}/rx/rx_multi.h
%{_includedir}/rx/rx_pthread.h
%{_includedir}/rx/rx_lwp.h
%{_includedir}/rx/rx_misc.h
%{_includedir}/rx/rx_null.h
%{_includedir}/rx/xdr.h
%{_includedir}/rx/xdr_prototypes.h
%{_includedir}/rx/rxstat.h
%{_includedir}/rx/fcrypt.h
%{_includedir}/rx/rxkad.h
%{_includedir}/rx/rxkad_prototypes.h
%{_includedir}/des.h
%{_includedir}/des_prototypes.h
%{_includedir}/des_conf.h
%{_includedir}/mit-cpyright.h
%{_includedir}/des_odd.h
%{_includedir}/potpourri.h
%{_includedir}/lock.h
%{_includedir}/lwp.h
%{_includedir}/preempt.h
%{_includedir}/timer.h
%{_includedir}/ubik.h
%{_includedir}/ubik_int.h
%{_includedir}/kopenafs.h
%attr(-,root,sys) %dir %{_datadir}
%{_datadir}/openafs/C/afszcm.cat
%attr(-,root,sys) %{_prefix}/kernel/fs/afs
%attr(-,root,sys) %{_prefix}/kernel/fs/%{_arch64}/afs

%changelog
* Tue May 4 2010 - jlee@thestaticvoid.com
- Initial version
