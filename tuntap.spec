#
# spec file for package: tuntap
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

#
# Until pkgbuild supports generic actions,
#
#   driver name=tun
#   driver name=tap
#
# must be added to ~/packages/PKGMAPS/manifests/tuntap.manifest
# and ~/packages/PKGMAPS/scripts/tuntap_ips.sh called manually.
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%define configopts ""
%use tuntap_64 = tuntap-base.spec
%endif
%include base.inc
%define configopts "--disable-64bit"
%use tuntap = tuntap-base.spec

Name:		tuntap
Version:	%{tuntap.version}
Summary:	TAP driver for Solaris used for OpenVPN
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.whiteboard.ne.jp/~admin2/tuntap/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Kazuyoshi <admin2@whiteboard.ne.jp>
Meta(info.upstream_url):	http://www.whiteboard.ne.jp/~admin2/tuntap/
Meta(info.classification):	org.opensolaris.category.2008:Drivers/Networking

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%tuntap_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%tuntap.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%tuntap_64.build -d %{name}-%{version}/%{_arch64}
%endif
%tuntap.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%tuntap_64.install -d %{name}-%{version}/%{_arch64}
%endif
%tuntap.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,sys)
/usr/kernel
%defattr(-,root,bin)
/usr/include

%changelog
* Thu Jan 28 2010 - jlee@thestaticvoid.com
- Initial version
