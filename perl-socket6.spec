#
# spec file for package: perl-socket6
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-socket6
Version:	0.23
Summary:	IPv6 related part of the C socket.h defines and structure manipulators
License:	BSD
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~umemoto/Socket6-%{version}/Socket6.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/U/UM/UMEMOTO/Socket6-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
Requires:	SUNWperl584core

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Hajimu Umemoto <ume@mahoroba.org>
Meta(info.upstream_url):        http://search.cpan.org/~umemoto/Socket6-%{version}/Socket6.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
This module provides glue routines to the various IPv6 functions.

%prep
%setup -q -n Socket6-%{version}

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLSITEMAN3DIR=%{_mandir}/man3 DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{_prefix}/perl5

%changelog
* Sun May 31 2009 - jlee@thestaticvoid.com
- Initial version
