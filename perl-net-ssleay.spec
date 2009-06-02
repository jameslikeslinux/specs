#
# spec file for package: perl-net-ssleay
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-net-ssleay
Version:	1.35
Summary:	Perl extension for using OpenSSL
License:	OpenSSL
Group:		Development/Perl
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~flora/Net-SSLeay-%{version}/lib/Net/SSLeay.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Net-SSLeay-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	SUNWopenssl-include
BuildRequires:	SUNWopenssl-libraries
Requires:	SUNWperl584core
Requires:	SUNWopenssl-libraries

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Florian Ragwitz <rafl@debian.org>
Meta(info.upstream_url):        http://search.cpan.org/~flora/Net-SSLeay-%{version}/lib/Net/SSLeay.pm

%description
This module offers some high level convinience functions for accessing web
pages on SSL servers.

%prep
%setup -q -n Net-SSLeay-%{version}

%build
PERL_MM_USE_DEFAULT=1 perl Makefile.PL PREFIX=%{_prefix} INSTALLSITEMAN3DIR=%{_mandir}/man3 DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4
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
