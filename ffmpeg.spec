#
# spec file for package: ffmpeg
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%define optflags "-m64"
%use ffmpeg_64 = ffmpeg-base.spec
%endif
%include base.inc
%define optflags ""
%use ffmpeg = ffmpeg-base.spec

Name:		ffmpeg
Version:	%{ffmpeg.version}
Summary:	FFmpeg
License:	LGPLv2.1/GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://ffmpeg.org/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWgcc
BuildRequires:	SUNWgawk
BuildRequires:	SUNWgsed
BuildRequires:	SUNWggrp
BuildRequires:	SUNWgnu-coreutils
BuildRequires:	SUNWperl584usr
BuildRequires:	SUNWtexi
BuildRequires:	SUNWaudh
BuildRequires:	SUNWlibsdl-devel
BuildRequires:	SUNWmlib
BuildRequires:	libfaad2-devel
BuildRequires:	SUNWspeex-devel
BuildRequires:	SUNWlibtheora-devel
BuildRequires:	SUNWogg-vorbis-devel
BuildRequires:	SUNWzlib
BuildRequires:	SUNWbzip
Requires:	SUNWlibsdl
Requires:	SUNWmlib
Requires:	libfaad2
Requires:	SUNWspeex
Requires:	SUNWlibtheora
Requires:	SUNWogg-vorbis
Requires:	SUNWzlib
Requires:	SUNWbzip

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Michael Niedermayer <michaelni@gmx.at>
Meta(info.upstream_url):	http://ffmpeg.org/
Meta(info.classification):	org.opensolaris.category.2008:Applications/Sound and Video

%description
FFmpeg is a complete, cross-platform solution to record, convert and stream
audio and video. It includes libavcodec - the leading audio/video codec
library.

This package contains the shared libraries and executables.

%package devel
Summary:	Headers for ffmpeg
Requires:	%{name}

%description devel
FFmpeg is a complete, cross-platform solution to record, convert and stream
audio and video. It includes libavcodec - the leading audio/video codec
library.

This package contains the ffmpeg development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%ffmpeg_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%ffmpeg.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%ffmpeg_64.build -d %{name}-%{version}/%{_arch64}
%endif
%ffmpeg.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%ffmpeg_64.install -d %{name}-%{version}/%{_arch64}
%endif
%ffmpeg.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/ffmpeg $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/ffplay $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/ffserver $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec ffmpeg
ln -s ../lib/isaexec ffplay
ln -s ../lib/isaexec ffserver
%endif

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/ffmpeg
%{_bindir}/%{_arch64}/ffplay
%{_bindir}/%{_arch64}/ffserver
%{_libdir}/%{_arch64}/libavcodec.so.52
%{_libdir}/%{_arch64}/libavcodec.so.52.53.0
%{_libdir}/%{_arch64}/libavdevice.so.52
%{_libdir}/%{_arch64}/libavdevice.so.52.2.0
%{_libdir}/%{_arch64}/libavfilter.so.1
%{_libdir}/%{_arch64}/libavfilter.so.1.17.0
%{_libdir}/%{_arch64}/libavformat.so.52
%{_libdir}/%{_arch64}/libavformat.so.52.52.0
%{_libdir}/%{_arch64}/libavutil.so.50
%{_libdir}/%{_arch64}/libavutil.so.50.9.0
%{_libdir}/%{_arch64}/libpostproc.so.51
%{_libdir}/%{_arch64}/libpostproc.so.51.2.0
%{_libdir}/%{_arch64}/libswscale.so.0
%{_libdir}/%{_arch64}/libswscale.so.0.10.0
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/ffmpeg
%{_bindir}/%{base_isa}/ffplay
%{_bindir}/%{base_isa}/ffserver
%hard %{_bindir}/ffmpeg
%hard %{_bindir}/ffplay
%hard %{_bindir}/ffserver
%else
%{_bindir}/ffmpeg
%{_bindir}/ffplay
%{_bindir}/ffserver
%endif
%{_libdir}/libavcodec.so.52
%{_libdir}/libavcodec.so.52.53.0
%{_libdir}/libavdevice.so.52
%{_libdir}/libavdevice.so.52.2.0
%{_libdir}/libavfilter.so.1
%{_libdir}/libavfilter.so.1.17.0
%{_libdir}/libavformat.so.52
%{_libdir}/libavformat.so.52.52.0
%{_libdir}/libavutil.so.50
%{_libdir}/libavutil.so.50.9.0
%{_libdir}/libpostproc.so.51
%{_libdir}/libpostproc.so.51.2.0
%{_libdir}/libswscale.so.0
%{_libdir}/libswscale.so.0.10.0
%attr(-,root,sys) %dir %{_datadir}
%{_datadir}/ffmpeg/libx264-lossless_max.ffpreset
%{_datadir}/ffmpeg/libx264-baseline.ffpreset
%{_datadir}/ffmpeg/libx264-normal.ffpreset
%{_datadir}/ffmpeg/libx264-slowfirstpass.ffpreset
%{_datadir}/ffmpeg/libx264-default.ffpreset
%{_datadir}/ffmpeg/libx264-max.ffpreset
%{_datadir}/ffmpeg/libx264-lossless_ultrafast.ffpreset
%{_datadir}/ffmpeg/libx264-lossless_fast.ffpreset
%{_datadir}/ffmpeg/libx264-ipod640.ffpreset
%{_datadir}/ffmpeg/libx264-fastfirstpass.ffpreset
%{_datadir}/ffmpeg/libx264-main.ffpreset
%{_datadir}/ffmpeg/libx264-lossless_slower.ffpreset
%{_datadir}/ffmpeg/libx264-hq.ffpreset
%{_datadir}/ffmpeg/libx264-lossless_medium.ffpreset
%{_datadir}/ffmpeg/libx264-ipod320.ffpreset
%{_datadir}/ffmpeg/libx264-lossless_slow.ffpreset
%{_mandir}/man1/ffmpeg.1
%{_mandir}/man1/ffplay.1
%{_mandir}/man1/ffserver.1

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libavcodec.so
%{_libdir}/%{_arch64}/libavdevice.so
%{_libdir}/%{_arch64}/libavfilter.so
%{_libdir}/%{_arch64}/libavformat.so
%{_libdir}/%{_arch64}/libavutil.so
%{_libdir}/%{_arch64}/libpostproc.so
%{_libdir}/%{_arch64}/libswscale.so
%attr(-,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/libavutil.pc
%{_libdir}/%{_arch64}/pkgconfig/libpostproc.pc
%{_libdir}/%{_arch64}/pkgconfig/libavcodec.pc
%{_libdir}/%{_arch64}/pkgconfig/libswscale.pc
%{_libdir}/%{_arch64}/pkgconfig/libavfilter.pc
%{_libdir}/%{_arch64}/pkgconfig/libavformat.pc
%{_libdir}/%{_arch64}/pkgconfig/libavdevice.pc
%endif
%{_libdir}/libavcodec.so
%{_libdir}/libavformat.so
%{_libdir}/libavdevice.so
%{_libdir}/libavfilter.so
%{_libdir}/libavutil.so
%{_libdir}/libpostproc.so
%{_libdir}/libswscale.so
%attr(-,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/libpostproc.pc
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/pkgconfig/libswscale.pc

%{_includedir}/libswscale/swscale.h
%{_includedir}/libavdevice/avdevice.h
%{_includedir}/libavutil/mem.h
%{_includedir}/libavutil/base64.h
%{_includedir}/libavutil/avutil.h
%{_includedir}/libavutil/pixfmt.h
%{_includedir}/libavutil/adler32.h
%{_includedir}/libavutil/rational.h
%{_includedir}/libavutil/avconfig.h
%{_includedir}/libavutil/intfloat_readwrite.h
%{_includedir}/libavutil/log.h
%{_includedir}/libavutil/fifo.h
%{_includedir}/libavutil/pixdesc.h
%{_includedir}/libavutil/avstring.h
%{_includedir}/libavutil/sha1.h
%{_includedir}/libavutil/mathematics.h
%{_includedir}/libavutil/md5.h
%{_includedir}/libavutil/lzo.h
%{_includedir}/libavutil/common.h
%{_includedir}/libavutil/crc.h
%{_includedir}/libavfilter/avfilter.h
%{_includedir}/libpostproc/postprocess.h
%{_includedir}/libavcodec/vdpau.h
%{_includedir}/libavcodec/dxva2.h
%{_includedir}/libavcodec/xvmc.h
%{_includedir}/libavcodec/vaapi.h
%{_includedir}/libavcodec/avcodec.h
%{_includedir}/libavcodec/opt.h
%{_includedir}/libavformat/avio.h
%{_includedir}/libavformat/avformat.h

%changelog
* Thu Feb 11 2010 - jlee@thestaticvoid.com
- Initial version
