#
# spec file for package: sshfs
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		sshfs
Version:	2.2
Summary:	SSH Filesystem
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://fuse.sourceforge.net/sshfs.html
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://downloads.sourceforge.net/project/fuse/sshfs-fuse/%{version}/sshfs-fuse-%{version}.tar.gz
Patch0:		sshfs-00-configure.diff

%include default-depend.inc
BuildRequires:	SUNWlibfuse
Requires:	SUNWlibfuse
Requires:	SUNWsshu

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            fuse-sshfs@lists.sourceforge.net
Meta(info.upstream_url):        http://fuse.sourceforge.net/sshfs.html
Meta(info.classification):	org.opensolaris.category.2008:System/File System

%description
This is a filesystem client based on the SSH File Transfer Protocol. Since most
SSH servers already support this protocol it is very easy to set up: i.e. on
the server side there's nothing to do.  On the client side mounting the
filesystem is as easy as logging into the server with ssh.

%prep
%setup -q -n sshfs-fuse-%{version}
%patch0
autoconf

%build
export CFLAGS="%{optflags} -I/usr/include/fuse -D_FILE_OFFSET_BITS=64"
export LDFLAGS="%{_ldflags} -lfuse -lsocket"
./configure --prefix=%{_prefix} --bindir=%{_bindir} 
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{_bindir}/sshfs
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}/man1/sshfs.1

%changelog
* Mon Jan 24 2011 - jlee@thestaticvoid.com
- Initial version
