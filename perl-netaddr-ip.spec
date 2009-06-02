#
# spec file for package: perl-netaddr-ip
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-netaddr-ip
Version:	4.026
Summary:	Manages IPv4 and IPv6 addresses and subnets
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~miker/NetAddr-IP-%{version}/IP.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIKER/NetAddr-IP-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
Requires:	SUNWperl584core

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Michael Robinton <michael@bizsystems.com>
Meta(info.upstream_url):        http://search.cpan.org/~miker/NetAddr-IP-%{version}/IP.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
This module provides an object-oriented abstraction on top of IP addresses or
IP subnets, that allows for easy manipulations.

%prep
%setup -q -n NetAddr-IP-%{version}

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
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}

%changelog
* Mon Jun 01 2009 - jlee@thestaticvoid.com
- Initial version
