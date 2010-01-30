#
# spec file for package: libgcrypt
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64
%include arch64.inc
%define build_type x86_64-pc-solaris2.11
%use libgcrypt_64 = libgcrypt-base.spec
%endif
%include base.inc
%define build_type i386-pc-solaris2.11
%use libgcrypt = libgcrypt-base.spec

Name:		libgcrypt
Version:	%{libgcrypt.version}
Summary:	Libgcrypt
License:	LGPLv2.1
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.gnu.org/software/libgcrypt/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWgcc
BuildRequires:	SUNWbtool
BuildRequires:	SUNWggrp
BuildRequires:	SUNWlibgpg-error
Requires:	SUNWlibgpg-error

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Werner Koch <wk@gnupg.org>
Meta(info.upstream_url):	http://www.gnu.org/software/libgcrypt/
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
This is a general purpose cryptographic library based on the code from GnuPG.
It provides functions for all cryptograhic building blocks: symmetric ciphers
(AES, DES, Blowfish, CAST5, Twofish, Arcfour), hash algorithms (MD4, MD5,
RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all hash algorithms), public key
algorithms (RSA, ElGamal, DSA), large integer functions, random numbers and a
lot of supporting functions. 

This package contains the shared library.

%package devel
Summary:	Headers for libgcrypt
Requires:	%{name}

%description devel
This is a general purpose cryptographic library based on the code from GnuPG.
It provides functions for all cryptograhic building blocks: symmetric ciphers
(AES, DES, Blowfish, CAST5, Twofish, Arcfour), hash algorithms (MD4, MD5,
RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all hash algorithms), public key
algorithms (RSA, ElGamal, DSA), large integer functions, random numbers and a
lot of supporting functions. 

This package contains the libgcrypt development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64
mkdir %{name}-%{version}/%{_arch64}
%libgcrypt_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libgcrypt.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64
%libgcrypt_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libgcrypt.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64
%libgcrypt_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libgcrypt.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/dumpsexp $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/hmac256 $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec dumpsexp
ln -s ../lib/isaexec hmac256
%endif

rm -rf $RPM_BUILD_ROOT%{_sbindir} $RPM_BUILD_ROOT%{_datadir}/info/dir

%files
%defattr(-,root,bin)
%ifarch amd64
%{_libdir}/%{_arch64}/libgcrypt.so.11
%{_libdir}/%{_arch64}/libgcrypt.so.11.5.3
%{_bindir}/%{_arch64}/dumpsexp
%{_bindir}/%{_arch64}/hmac256
%endif
%{_libdir}/libgcrypt.so.11
%{_libdir}/libgcrypt.so.11.5.3
%if %can_isaexec
%{_bindir}/%{base_isa}/dumpsexp
%{_bindir}/%{base_isa}/hmac256
%hard %{_bindir}/dumpsexp
%hard %{_bindir}/hmac256
%else
%{_bindir}/dumpsexp
%{_bindir}/hmac256
%endif

%files devel
%defattr(-,root,bin)
%ifarch amd64
%{_libdir}/%{_arch64}/libgcrypt.la
%{_libdir}/%{_arch64}/libgcrypt.so
%{_bindir}/%{_arch64}/libgcrypt-config
%endif
%{_libdir}/libgcrypt.la
%{_libdir}/libgcrypt.so
%{_bindir}/libgcrypt-config
%{_includedir}/gcrypt.h
%{_includedir}/gcrypt-module.h
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_datadir}/aclocal
%{_datadir}/aclocal/libgcrypt.m4
%{_datadir}/info/gcrypt.info

%changelog
* Thu Jan 28 2010 - jlee@thestaticvoid.com
- Initial version
