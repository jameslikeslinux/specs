#
# spec file for package: musepack
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use musepack_64 = musepack-base.spec
%endif
%include base.inc
%use musepack = musepack-base.spec

Name:		musepack
Version:	%{musepack.version}
Summary:	Musepack
License:	BSD/LGPLv2.1/GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.musepack.net/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWgnu-automake-19
BuildRequires:	SUNWaconf
BuildRequires:	SUNWlibtool
BuildRequires:	SUNWggrp
BuildRequires:	libreplaygain-devel
BuildRequires:	libcuefile-devel
Requires:	libreplaygain
Requires:	libcuefile

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Shy Keidar <shykeidar@musepack.net>
Meta(info.upstream_url):	http://www.musepack.net/
Meta(info.classification):	org.opensolaris.category.2008:Applications/Sound and Video

%description
Musepack is an audio compression format with a strong emphasis on high
quality. It's not lossless, but it is designed for transparency, so that you
won't be able to hear differences between the original wave file and the much
smaller MPC file.

It is based on the MPEG-1 Layer-2 / MP2 algorithms, but since 1997 it has
rapidly developed and vastly improved and is now at an advanced stage in which
it contains heavily optimized and patentless code. 

This package contains the musepack shared library and tools.

%package devel
Summary:	Headers for libmpcdec
Requires:	%{name}

%description devel
This package contains the musepack development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%musepack_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%musepack.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%musepack_64.build -d %{name}-%{version}/%{_arch64}
%endif
%musepack.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%musepack_64.install -d %{name}-%{version}/%{_arch64}
%endif
%musepack.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/mpcenc $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/mpc2sv8 $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/mpccut $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/mpcdec $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/mpcchap $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/mpcgain $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/wavcmp $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec mpcenc
ln -s ../lib/isaexec mpc2sv8
ln -s ../lib/isaexec mpccut
ln -s ../lib/isaexec mpcdec
ln -s ../lib/isaexec mpcchap
ln -s ../lib/isaexec mpcgain
ln -s ../lib/isaexec wavcmp
%endif

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libmpcdec.so.6
%{_libdir}/%{_arch64}/libmpcdec.so.6.1.0
%{_bindir}/%{_arch64}/mpcenc
%{_bindir}/%{_arch64}/mpc2sv8
%{_bindir}/%{_arch64}/mpccut
%{_bindir}/%{_arch64}/mpcdec
%{_bindir}/%{_arch64}/mpcchap
%{_bindir}/%{_arch64}/mpcgain
%{_bindir}/%{_arch64}/wavcmp
%endif
%{_libdir}/libmpcdec.so.6
%{_libdir}/libmpcdec.so.6.1.0
%if %can_isaexec
%{_bindir}/%{base_isa}/mpcenc
%{_bindir}/%{base_isa}/mpc2sv8
%{_bindir}/%{base_isa}/mpccut
%{_bindir}/%{base_isa}/mpcdec
%{_bindir}/%{base_isa}/mpcchap
%{_bindir}/%{base_isa}/mpcgain
%{_bindir}/%{base_isa}/wavcmp
%hard %{_bindir}/mpcenc
%hard %{_bindir}/mpc2sv8
%hard %{_bindir}/mpccut
%hard %{_bindir}/mpcdec
%hard %{_bindir}/mpcchap
%hard %{_bindir}/mpcgain
%hard %{_bindir}/wavcmp
%else
%{_bindir}/mpcenc
%{_bindir}/mpc2sv8
%{_bindir}/mpccut
%{_bindir}/mpcdec
%{_bindir}/mpcchap
%{_bindir}/mpcgain
%{_bindir}/wavcmp
%endif

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libmpcdec.la
%{_libdir}/%{_arch64}/libmpcdec.so
%endif
%{_libdir}/libmpcdec.la
%{_libdir}/libmpcdec.so
%{_includedir}/mpc/mpcdec.h
%{_includedir}/mpc/mpc_types.h
%{_includedir}/mpc/streaminfo.h
%{_includedir}/mpc/datatypes.h
%{_includedir}/mpc/minimax.h
%{_includedir}/mpc/reader.h
%{_includedir}/mpc/mpcmath.h

%changelog
* Fri Nov 27 2009 - jlee@thestaticvoid.com
- Initial version
