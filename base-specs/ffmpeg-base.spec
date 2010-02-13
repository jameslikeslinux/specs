#
# spec file for package: ffmpeg
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		ffmpeg
Version:	0.5.20100211
Source0:	http://ffmpeg.org/releases/ffmpeg-export-snapshot.tar.bz2
Patch0:		ffmpeg-00-mlib.diff
Patch1:		ffmpeg-01-configure-doc.diff

%prep
%setup -q -n ffmpeg-export-2010-02-11

# see http://blogs.sun.com/siva/entry/some_updates_ruby_dtrace_ffmpeg
%patch0
%patch1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
        CPUS=1
fi 

# for pod2man
export PATH=/usr/perl5/bin:$PATH 

./configure --prefix=%{_prefix} \
	    --bindir=%{_bindir} \
	    --libdir=%{_libdir} \
	    --shlibdir=%{_libdir} \
	    --cc=gcc-4.3.2 \
            --extra-cflags="%{optflags}" \
	    --extra-ldflags="%{optflags} %{_ldflags}" \
	    --disable-static \
	    --enable-shared \
	    --enable-runtime-cpudetect \
	    --enable-postproc \
	    --enable-avfilter \
	    --enable-avfilter-lavf \
	    --enable-pthreads \
	    --enable-libfaad \
	    --enable-libspeex \
	    --enable-libtheora \
	    --enable-libvorbis \
	    --enable-mlib \
	    --enable-gpl

gmake -j $CPUS

%install
# force usage of ginstall instead of solaris install
gsed -i 's/\tinstall/\tginstall/' Makefile subdir.mak
gmake DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
