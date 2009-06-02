#
# spec file for package: perl-io-compress
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-io-compress
Version:	2.019
Summary:	IO:: Interface to Compressed Files
License:	Artistic
Group:		Development/Perl
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~pmqs/IO-Compress-%{version}/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/IO-Compress-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	perl-compress-raw-bzip2
BuildRequires:	perl-compress-raw-zlib
Requires:	SUNWperl584core
Requires:	perl-compress-raw-bzip2
Requires:	perl-compress-raw-zlib

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Paul Marquees <pmqs@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~pmqs/IO-Compress-%{version}/

%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the zlib and bzip2 libraries.

%prep
%setup -q -n IO-Compress-%{version}

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
