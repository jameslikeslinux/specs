#
# spec file for package: wavpack
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use wavpack_64 = wavpack-base.spec
%endif
%include base.inc
%use wavpack = wavpack-base.spec

Name:		wavpack
Version:	%{wavpack.version}
Summary:	Hybrid Lossless Wavefile Compressor
License:	BSD
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.wavpack.com/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:  SUNWggrp

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		David Bryant <david@wavpack.com>
Meta(info.upstream_url):	http://www.wavpack.com/
Meta(info.classification):	org.opensolaris.category.2008:Applications/Sound and Video

%description
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new version 4
format has been designed from the ground up to offer unparalleled performance
and functionality. 

This package contains the wavpack shared library and tools.

%package devel
Summary:	Headers for libwavpack
Requires:	%{name}

%description devel
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new version 4
format has been designed from the ground up to offer unparalleled performance
and functionality. 

This package contains the wavpack development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%wavpack_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%wavpack.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%wavpack_64.build -d %{name}-%{version}/%{_arch64}
%endif
%wavpack.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%wavpack_64.install -d %{name}-%{version}/%{_arch64}
%endif
%wavpack.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/wavpack $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/wvunpack $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/wvgain $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec wavpack
ln -s ../lib/isaexec wvunpack
ln -s ../lib/isaexec wvgain
%endif

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libwavpack.so.1
%{_libdir}/%{_arch64}/libwavpack.so.1.1.3
%{_bindir}/%{_arch64}/wavpack
%{_bindir}/%{_arch64}/wvunpack
%{_bindir}/%{_arch64}/wvgain
%endif
%{_libdir}/libwavpack.so.1
%{_libdir}/libwavpack.so.1.1.3
%if %can_isaexec
%{_bindir}/%{base_isa}/wavpack
%{_bindir}/%{base_isa}/wvunpack
%{_bindir}/%{base_isa}/wvgain
%hard %{_bindir}/wavpack
%hard %{_bindir}/wvunpack
%hard %{_bindir}/wvgain
%else
%{_bindir}/wavpack
%{_bindir}/wvunpack
%{_bindir}/wvgain
%endif

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libwavpack.la
%{_libdir}/%{_arch64}/libwavpack.so
%attr(755,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/wavpack.pc
%endif
%{_libdir}/libwavpack.la
%{_libdir}/libwavpack.so
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/wavpack.pc
%{_includedir}/wavpack/wavpack.h

%changelog
* Sun Nov 29 2009 - jlee@thestaticvoid.com
- Initial version
