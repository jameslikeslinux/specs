#
# spec file for package: perl-io-socket-ssl
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-io-socket-ssl
Version:	1.23
Summary:	Nearly transparent SSL encapsulation for IO::Socket::INET
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~sullr/IO-Socket-SSL-%{version}/SSL.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/S/SU/SULLR/IO-Socket-SSL-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	perl-net-ssleay
Requires:	SUNWperl584core
Requires:	perl-net-ssleay

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Steffen Ullrich <Steffen_Ullrich@genua.de>
Meta(info.upstream_url):        http://search.cpan.org/~sullr/IO-Socket-SSL-%{version}/SSL.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
This module is a true drop-in replacement for IO::Socket::INET that uses SSL to
encrypt data before it is transferred to a remote server or client.

%prep
%setup -q -n IO-Socket-SSL-%{version}

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
