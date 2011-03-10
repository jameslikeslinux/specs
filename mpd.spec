#
# spec file for package: mpd
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use mpd_64 = mpd-base.spec
%endif
%include base.inc
%use mpd = mpd-base.spec

Name:		mpd
Version:	%{mpd.version}
Summary:	Music Player Daemon
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://mpd.wikia.com/
SUNW_BaseDir:	/
SUNW_Copyright:	%{name}.copyright

Source0:	mpd.conf
Source1:	mpd.xml

%include default-depend.inc
BuildRequires:	SUNWggrp
BuildRequires:	SUNWgnome-base-libs-devel
BuildRequires:	libao-devel
BuildRequires:	libshout-devel
BuildRequires:	SUNWogg-vorbis-devel
BuildRequires:	SUNWflac-devel
BuildRequires:	SUNWgnome-audio-devel
BuildRequires:	libfaad2-devel
BuildRequires:	musepack-devel
BuildRequires:	wavpack-devel
BuildRequires:	libmad-devel
BuildRequires:	SUNWsqlite3
BuildRequires:	SUNWaudh
BuildRequires:	SUNWcurl
BuildRequires:	libid3tag
BuildRequires:	ffmpeg-devel
Requires:	SUNWgnome-base-libs
Requires:	libao
Requires:	libshout
Requires:	SUNWogg-vorbis
Requires:	SUNWflac
Requires:	SUNWgnome-audio
Requires:	libfaad2
Requires:	musepack
Requires:	wavpack
Requires:	libmad
Requires:	SUNWsqlite3
Requires:	SUNWcurl
Requires:	libid3tag
Requires:	ffmpeg

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Max Kellermann <max@duempel.org>
Meta(info.upstream_url):	http://mpd.wikia.com/
Meta(info.classification):	org.opensolaris.category.2008:Applications/Sound and Video

%description
Music Player Daemon (MPD) is a server that allows remote access for playing
audio files (Ogg-Vorbis, FLAC, MP3, Wave, and AIFF), streams (Ogg-Vorbis, MP3)
and managing playlists. Gapless playback, buffered output, and crossfading
support is also included. The design focus is on integrating a computer into a
stereo system that provides control for music playback over a TCP/IP network.
The goals are to be easy to install and use, to have minimal resource
requirements (it has been reported to run fine on a Pentium 75), and to remain
stable and flexible.

The daemon is controlled through a client which need not run on the same
computer mpd runs on. The separate client and server design allows users to
choose a user interface that best suites their tastes independently of the
underlying daemon (this package) which actually plays music. 

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%mpd_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%mpd.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%mpd_64.build -d %{name}-%{version}/%{_arch64}
%endif
%mpd.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%mpd_64.install -d %{name}-%{version}/%{_arch64}
%endif
%mpd.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/mpd $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec mpd
%endif

mkdir $RPM_BUILD_ROOT%{_sysconfdir}
cp %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/mpd.conf

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/mpd
mkdir $RPM_BUILD_ROOT%{_localstatedir}/lib/mpd/music
mkdir $RPM_BUILD_ROOT%{_localstatedir}/lib/mpd/playlists

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/application
cp %{SOURCE1} $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/application/mpd.xml

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%actions
group groupname="mpd"
user username="mpd" group="mpd" gcos-field="Music Player Daemon User"

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/mpd
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/mpd
%hard %{_bindir}/mpd
%else
%{_bindir}/mpd
%endif
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_datadir}/doc
%{_datadir}/doc/mpd
%{_mandir}/man1/mpd.1
%{_mandir}/man5/mpd.conf.5
%defattr(-,root,sys)
%dir %{_sysconfdir}
%attr(640,root,mpd) %config %{_sysconfdir}/mpd.conf
%dir %{_localstatedir}
%attr(755,root,other) %dir %{_localstatedir}/lib
%attr(755,mpd,mpd) %dir %{_localstatedir}/lib/mpd
%attr(755,mpd,mpd) %dir %{_localstatedir}/lib/mpd/music
%attr(755,mpd,mpd) %dir %{_localstatedir}/lib/mpd/playlists
%dir %{_localstatedir}/svc
%dir %{_localstatedir}/svc/manifest
%dir %{_localstatedir}/svc/manifest/application
%class(manifest) %attr(444,root,sys) %{_localstatedir}/svc/manifest/application/mpd.xml

%changelog
* Tue Feb 15 2011 - jlee@thestaticvoid.com
- Config file owned by root
* Thu Jan 20 2011 - jlee@thestaticvoid.com
- Bump to 0.16.1
- Create mpd user
* Sun Nov 29 2009 - jlee@thestaticvoid.com
- Initial version
