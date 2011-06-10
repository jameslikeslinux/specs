#
# spec file for package: wpa_supplicant
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc
%include base.inc

Name:		wpa_supplicant
Version:	0.7.3.20110609
Summary:	WPA/WPA2/IEEE 802.1X Supplicant
License:	BSD
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://hostap.epitest.fi/wpa_supplicant/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
SUNW_Pkg:	wpasupplicant

Source0:	https://download.github.com/MrStaticVoid-hostap-solaris-1-0-g1f0faba.tar.gz

%include default-depend.inc
BuildRequires:	SUNWgmake
BuildRequires:	SUNWopenssl-include
BuildRequires:	SUNWopenssl-libraries
Requires:	SUNWopenssl-libraries

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Jouni Malinen <j@w1.fi>
Meta(info.upstream_url):	http://hostap.epitest.fi/wpa_supplicant/
Meta(info.classification):	org.opensolaris.category.2008:System/Services

%description
wpa_supplicant is a WPA Supplicant with support for WPA and WPA2 (IEEE 802.11i
/ RSN). It is suitable for both desktop/laptop computers and embedded systems.
Supplicant is the IEEE 802.1X/WPA component that is used in the client
stations. It implements key negotiation with a WPA Authenticator and it
controls the roaming and IEEE 802.11 authentication/association of the wlan
driver.

%prep
%setup -q -n MrStaticVoid-hostap-9d398db
cd wpa_supplicant
cat > .config << EOF
CONFIG_DRIVER_SOLARIS=y
CONFIG_DRIVER_WIRED=y
CC=cc
CFLAGS=-features=extensions -g -I../src -I../src/utils
LIBS += -lsocket -ldlpi -lnsl
LIBS_c += -lsocket
CONFIG_IEEE8021X_EAPOL=y
CONFIG_EAP_MD5=y
CONFIG_EAP_MSCHAPV2=y
CONFIG_EAP_TLS=y
CONFIG_EAP_PEAP=y
CONFIG_EAP_TTLS=y
CONFIG_EAP_GTC=y
CONFIG_EAP_OTP=y
CONFIG_EAP_LEAP=y
CONFIG_PKCS12=y
CONFIG_SMARTCARD=y
CONFIG_CTRL_IFACE=y
CONFIG_BACKEND=file
CONFIG_PEERKEY=y
CONFIG_DEBUG_SYSLOG=y
CONFIG_DEBUG_SYSLOG_FACILITY=LOG_DAEMON
EOF

%build
cd wpa_supplicant
gmake

%install
cd wpa_supplicant
rm -rf $RPM_BUILD_ROOT
gmake DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_sbindir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{_sbindir}/wpa_supplicant
%{_sbindir}/wpa_passphrase
%{_sbindir}/wpa_cli

%changelog
* Thu Jun 09 2011 - jlee@thestaticvoid.com
- Initial version
