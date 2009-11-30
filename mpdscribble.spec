#
# spec file for package: mpdscribble
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use mpdscribble_64 = mpdscribble-base.spec
%endif
%include base.inc
%use mpdscribble = mpdscribble-base.spec

Name:		mpdscribble
Version:	%{mpdscribble.version}
Summary:	Scrobbler for MPD
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://mpd.wikia.com/wiki/Client:Mpdscribble
SUNW_BaseDir:	/
SUNW_Copyright:	%{name}.copyright

Source0:	mpdscribble.xml

%include default-depend.inc
BuildRequires:	SUNWgnome-base-libs-devel
BuildRequires:	SUNWcurl
Requires:	SUNWgnome-base-libs
Requires:	SUNWcurl

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Max Kellermann <max@duempel.org>
Meta(info.upstream_url):	http://mpd.wikia.com/wiki/Client:Mpdscribble
Meta(info.classification):	org.opensolaris.category.2008:Applications/Sound and Video

%description
mpdscribble is a Music Player Daemon (MPD) client which submits information
about tracks being played to Last.fm (formerly audioscrobbler). 

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%mpdscribble_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%mpdscribble.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%mpdscribble_64.build -d %{name}-%{version}/%{_arch64}
%endif
%mpdscribble.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%mpdscribble_64.install -d %{name}-%{version}/%{_arch64}
%endif
%mpdscribble.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/mpdscribble $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec mpdscribble
%endif

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/mpdscribble

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/application
cp %{SOURCE0} $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/application/mpdscribble.xml

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/mpdscribble
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/mpdscribble
%hard %{_bindir}/mpdscribble
%else
%{_bindir}/mpdscribble
%endif
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_datadir}/doc
%{_datadir}/doc/mpdscribble
%{_mandir}/man1/mpdscribble.1
%defattr(-,root,sys)
%dir %{_sysconfdir}
%attr(640,root,nobody) %config %{_sysconfdir}/mpdscribble.conf
%dir %{_localstatedir}
%attr(755,root,root) %dir %{_localstatedir}/cache
%attr(700,nobody,nobody) %dir %{_localstatedir}/cache/mpdscribble
%dir %{_localstatedir}/svc
%dir %{_localstatedir}/svc/manifest
%dir %{_localstatedir}/svc/manifest/application
%class(manifest) %attr(444,root,sys) %{_localstatedir}/svc/manifest/application/mpdscribble.xml

%changelog
* Sun Nov 29 2009 - jlee@thestaticvoid.com
- Initial version
