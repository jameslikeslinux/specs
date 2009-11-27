#
# spec file for package: libfaad2
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libfaad2_64 = libfaad2-base.spec
%endif
%include base.inc
%use libfaad2 = libfaad2-base.spec

Name:		libfaad2
Version:	%{libfaad2.version}
Summary:	AAC decoder
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.audiocoding.com/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWbtool
BuildRequires:	SUNWggrp

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		M. Bakker <mbakker@nero.com>
Meta(info.upstream_url):	http://www.audiocoding.com/
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
FAAD2 is an open source MPEG-4 and MPEG-2 AAC decoder.

This package contains the shared library.

%package devel
Summary:	Headers for libfaad2
Requires:	%{name}

%description devel
FAAD2 is an open source MPEG-4 and MPEG-2 AAC decoder.

This package contains the libfaad2 development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libfaad2_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libfaad2.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%libfaad2_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libfaad2.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libfaad2_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libfaad2.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/faad $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec faad
%endif

mv $RPM_BUILD_ROOT%{_mandir}/manm $RPM_BUILD_ROOT%{_mandir}/man1
mv $RPM_BUILD_ROOT%{_mandir}/man1/faad.man $RPM_BUILD_ROOT%{_mandir}/man1/faad.1


%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libfaad.so.2
%{_libdir}/%{_arch64}/libfaad.so.2.0.0
%{_bindir}/%{_arch64}/faad
%endif
%{_libdir}/libfaad.so.2
%{_libdir}/libfaad.so.2.0.0
%if %can_isaexec
%{_bindir}/%{base_isa}/faad
%hard %{_bindir}/faad
%else
%{_bindir}/faad
%endif
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}/man1/faad.1

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libmp4ff.a
%{_libdir}/%{_arch64}/libfaad.la
%{_libdir}/%{_arch64}/libfaad.so
%endif
%{_libdir}/libmp4ff.a
%{_libdir}/libfaad.so
%{_libdir}/libfaad.la
%{_includedir}/mp4ffint.h
%{_includedir}/neaacdec.h
%{_includedir}/faad.h
%{_includedir}/mp4ff.h

%changelog
* Thu Nov 26 2009 - jlee@thestaticvoid.com
- Initial version
