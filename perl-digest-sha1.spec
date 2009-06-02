#
# spec file for package: perl-digest-sha1
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-digest-sha1
Version:	2.12
Summary:	Perl interface to the SHA-1 algorithm
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~gaas/Digest-SHA1-%{version}/SHA1.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Digest-SHA1-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
Requires:	SUNWperl584core

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Gisle Aas <gisle@ActiveState.com>
Meta(info.upstream_url):        http://search.cpan.org/~gaas/Digest-SHA1-%{version}/SHA1.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
The Digest::SHA1 module allows you to use the NIST SHA-1 message digest
algorithm from within Perl programs. The algorithm takes as input a message of
arbitrary length and produces as output a 160-bit "fingerprint" or "message
digest" of the input.

%prep
%setup -q -n Digest-SHA1-%{version}

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
* Sun May 31 2009 - jlee@thestaticvoid.com
- Initial version
