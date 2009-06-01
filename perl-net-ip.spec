#
# spec file for package: perl-net-ip
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-net-ip
Version:	1.25
Summary:	Perl Extension for Manipulating IPv4/IPv6 Addresses
License:	Artistic
Group:		Development/Perl
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~manu/Net-IP-%{version}/IP.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MANU/Net-IP-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
Requires:	SUNWperl584core

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Manuel Valente <manuel.valente@gmail.com>
Meta(info.upstream_url):        http://search.cpan.org/~manu/Net-IP-%{version}/IP.pm

%description
This module provides functions to deal with IPv4/IPv6 addresses.

%prep
%setup -q -n Net-IP-%{version}

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
%{_bindir}/ipcount
%{_bindir}/iptab
%{_prefix}/perl5
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}

%changelog
* Sun May 31 2009 - jlee@thestaticvoid.com
- Initial version
