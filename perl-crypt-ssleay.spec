#
# spec file for package: perl-crypt-ssleay
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-crypt-ssleay
Version:	0.57
Summary:	OpenSSL support for LWP
License:	Artistic
Group:		Development/Perl
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~dland/Crypt-SSLeay-%{version}/SSLeay.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/D/DL/DLAND/Crypt-SSLeay-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	SUNWopenssl-include
BuildRequires:	SUNWopenssl-libraries
Requires:	SUNWperl584core
BuildRequires:	SUNWopenssl-libraries

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            David Landgren <david@landgren.net>
Meta(info.upstream_url):        http://search.cpan.org/~dland/Crypt-SSLeay-%{version}/SSLeay.pm

%description
This perl module provides support for the https protocol under LWP, to allow an
LWP::UserAgent object to perform GET, HEAD and POST requests.

%prep
%setup -q -n Crypt-SSLeay-%{version}

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
* Sun May 31 2009 - jlee@thestaticvoid.com
- Initial version
