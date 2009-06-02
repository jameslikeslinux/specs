#
# spec file for package: perl-digest-hmac
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-digest-hmac
Version:	1.01
Summary:	Keyed-Hashing for Message Authentication
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~gaas/Digest-HMAC-%{version}/lib/Digest/HMAC.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Digest-HMAC-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	perl-digest-sha1
Requires:	SUNWperl584core
Requires:	perl-digest-sha1

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Gisle Aas <gisle@ActiveState.com>
Meta(info.upstream_url):        http://search.cpan.org/~gaas/Digest-HMAC-%{version}/lib/Digest/HMAC.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
HMAC is used for message integrity checks between two parties that share a
secret key, and works in combination with some other Digest algorithm, usually
MD5 or SHA-1. The HMAC mechanism is described in RFC 2104.

%prep
%setup -q -n Digest-HMAC-%{version}

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
