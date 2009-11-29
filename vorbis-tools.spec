#
# spec file for package: vorbis-tools
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use vorbis_tools_64 = vorbis-tools-base.spec
%endif
%include base.inc
%use vorbis_tools = vorbis-tools-base.spec

Name:		vorbis-tools
Version:	%{vorbis_tools.version}
Summary:	Vorbis Audio Encoder and Utilities
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.vorbis.com/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWbtool
BuildRequires:	SUNWggrp
BuildRequires:	SUNWgnome-common-devel
BuildRequires:	SUNWcurl
BuildRequires:	SUNWflac-devel
BuildRequires:	SUNWogg-vorbis-devel
BuildRequires:	SUNWspeex-devel
BuildRequires:	libao-devel
Requires:	SUNWcurl
Requires:	SUNWflac
Requires:	SUNWogg-vorbis
Requires:	SUNWspeex
Requires:	libao

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Xiph.org <vorbis@xiph.org>
Meta(info.upstream_url):	http://xiph.org/vorbis/
Meta(info.classification):	org.opensolaris.category.2008:Applications/Sound and Video

%description
vorbis-tools contains oggenc (an encoder) and ogg123 (a playback tool).
It also has vorbiscomment (to add comments to Vorbis files), ogginfo (to
give all useful information about an Ogg file, including streams in it),
oggdec (a simple command line decoder), and vcut (which allows you to 
cut up Vorbis files).

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%vorbis_tools_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%vorbis_tools.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%vorbis_tools_64.build -d %{name}-%{version}/%{_arch64}
%endif
%vorbis_tools.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%vorbis_tools_64.install -d %{name}-%{version}/%{_arch64}
%endif
%vorbis_tools.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/ogg123 $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/oggenc $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/ogginfo $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/vorbiscomment $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/oggdec $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec ogg123
ln -s ../lib/isaexec oggenc
ln -s ../lib/isaexec ogginfo
ln -s ../lib/isaexec vorbiscomment
ln -s ../lib/isaexec oggdec
%endif

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/vorbiscomment
%{_bindir}/%{_arch64}/oggdec
%{_bindir}/%{_arch64}/ogginfo
%{_bindir}/%{_arch64}/oggenc
%{_bindir}/%{_arch64}/ogg123
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/ogg123
%{_bindir}/%{base_isa}/oggenc
%{_bindir}/%{base_isa}/ogginfo
%{_bindir}/%{base_isa}/vorbiscomment
%{_bindir}/%{base_isa}/oggdec
%hard %{_bindir}/ogg123
%hard %{_bindir}/oggenc
%hard %{_bindir}/ogginfo
%hard %{_bindir}/vorbiscomment
%hard %{_bindir}/oggdec
%else
%{_bindir}/ogg123
%{_bindir}/oggenc
%{_bindir}/ogginfo
%{_bindir}/vorbiscomment
%{_bindir}/oggdec
%endif
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}/man1/oggdec.1
%{_mandir}/man1/ogg123.1
%{_mandir}/man1/ogginfo.1
%{_mandir}/man1/oggenc.1
%{_mandir}/man1/vorbiscomment.1
%attr(755,root,other) %dir %{_docdir}
%{_docdir}/vorbis-tools-1.2.0/ogg123rc-example
%attr(755,root,other) %dir %{_datadir}/locale
%attr(755,root,other) %dir %{_datadir}/locale/cs
%attr(755,root,other) %dir %{_datadir}/locale/cs/LC_MESSAGES
%{_datadir}/locale/cs/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/nl
%attr(755,root,other) %dir %{_datadir}/locale/nl/LC_MESSAGES
%{_datadir}/locale/nl/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/fr
%attr(755,root,other) %dir %{_datadir}/locale/fr/LC_MESSAGES
%{_datadir}/locale/fr/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/hr
%attr(755,root,other) %dir %{_datadir}/locale/hr/LC_MESSAGES
%{_datadir}/locale/hr/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/hu
%attr(755,root,other) %dir %{_datadir}/locale/hu/LC_MESSAGES
%{_datadir}/locale/hu/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/es
%attr(755,root,other) %dir %{_datadir}/locale/es/LC_MESSAGES
%{_datadir}/locale/es/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/ro
%attr(755,root,other) %dir %{_datadir}/locale/ro/LC_MESSAGES
%{_datadir}/locale/ro/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/da
%attr(755,root,other) %dir %{_datadir}/locale/da/LC_MESSAGES
%{_datadir}/locale/da/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/be
%attr(755,root,other) %dir %{_datadir}/locale/be/LC_MESSAGES
%{_datadir}/locale/be/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/uk
%attr(755,root,other) %dir %{_datadir}/locale/uk/LC_MESSAGES
%{_datadir}/locale/uk/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/ru
%attr(755,root,other) %dir %{_datadir}/locale/ru/LC_MESSAGES
%{_datadir}/locale/ru/LC_MESSAGES/vorbis-tools.mo
%attr(755,root,other) %dir %{_datadir}/locale/sv
%attr(755,root,other) %dir %{_datadir}/locale/sv/LC_MESSAGES
%{_datadir}/locale/sv/LC_MESSAGES/vorbis-tools.mo

%changelog
* Sun May 31 2009 - jlee@thestaticvoid.com
- Add header and correct copyright
* Fri May 29 2009 - jlee@thestaticvoid.com
- Initial version
