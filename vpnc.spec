#
# spec file for package: vpnc
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		vpnc
Version:	0.5.3
Summary:	Client for Cisco VPN Concentrator
License:	GPLv2/BSD
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.unix-ag.uni-kl.de/~massar/vpnc/
SUNW_Basedir:	/
SUNW_Copyright: %{name}.copyright

Source0:	http://www.unix-ag.uni-kl.de/~massar/vpnc/vpnc-%{version}.tar.gz
Source1:	http://git.infradead.org/users/dwmw2/vpnc-scripts.git/blob_plain/HEAD:/vpnc-script
Patch0:		vpnc-00-openlog.diff

%include default-depend.inc
BuildRequires:	SUNWgcc
BuildRequires:	SUNWgmake
BuildRequires:	SUNWgnu-coreutils
BuildRequires:	SUNWopenssl-include
BuildRequires:	libgcrypt-devel
Requires:	SUNWopenssl-libraries
Requires:	libgcrypt
Requires:	tuntap

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Maurice Massar <vpnc@unix-ag.uni-kl.de>
Meta(info.upstream_url):	http://www.unix-ag.uni-kl.de/~massar/vpnc/
Meta(info.classification):	org.opensolaris.category.2008:Applications/Internet

%description
vpnc is a VPN client compatible with cisco3000 VPN Concentrator (also known as
Cisco's EasyVPN equipment). vpnc runs entirely in userspace and does not
require kernel modules except of the tun driver to communicate with the network
layer.

It supports most of the features needed to establish connection to the VPN
concentrator: MD5 and SHA1 hashes, 3DES and AES ciphers, PFS and various IKE DH
group settings. 

%prep
%setup -q
%patch0

# Compile with OpenSSL support for handling certificates
# and force using ginstall instead of install
sed 's/^#\(OPENSSL.*\)/\1/; s/install/ginstall/g' Makefile > Makefile.new
mv -f Makefile.new Makefile

%build
gmake PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
gmake PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT ginstall

# Install a vpnc-script which supports Solaris
# from http://www.infradead.org/openconnect.html
cp %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/vpnc/vpnc-script

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%attr(-,root,sys) %dir %{_prefix}
%{_bindir}/cisco-decrypt
%{_bindir}/pcf2vpnc
%{_sbindir}/vpnc
%{_sbindir}/vpnc-disconnect
%attr(-,root,sys) %dir %{_datadir}
%attr(-,root,other) %dir %{_docdir}
%{_docdir}/vpnc/COPYING
%{_mandir}/man1/cisco-decrypt.1
%{_mandir}/man1/pcf2vpnc.1
%{_mandir}/man8/vpnc.8
%defattr(-,root,sys)
%{_sysconfdir}/vpnc/default.conf
%{_sysconfdir}/vpnc/vpnc-script

%changelog
* Fri Jan 29 2010 - jlee@thestaticvoid.com
- Initial version
