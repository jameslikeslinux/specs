#
# spec file for package: perl-net-dns
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-net-dns
Version:	0.65
Summary:	Perl interface to the DNS resolver
License:	Artistic
Group:		Development/Perl
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/dist/Net-DNS/lib/Net/DNS.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/O/OL/OLAF/Net-DNS-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	perl-digest-hmac
BuildRequires:	perl-net-ip
BuildRequires:	perl-inet-socket-inet6
Requires:	SUNWperl584core
Requires:	perl-digest-hmac
Requires:	perl-net-ip
Requires:	perl-inet-socket-inet6

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Olaf Kolkman <olaf@net-dns.org>
Meta(info.upstream_url):        http://search.cpan.org/dist/Net-DNS/lib/Net/DNS.pm

%description
Net::DNS is a collection of Perl modules that act as a Domain Name System (DNS)
resolver. It allows the programmer to perform DNS queries that are beyond the
capabilities of gethostbyname and gethostbyaddr.

%prep
%setup -q -n Net-DNS-%{version}

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLSITEMAN3DIR=%{_mandir}/man3 DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4 --no-online-tests --no-IPv6-tests
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
* Sun May 31 2009 - jlee@thestaticvoid.com
- Initial version
