#
# spec file for package: perl-io-zlib
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-io-zlib
Version:	1.09
Summary:	IO:: style interface to Compress::Zlib
License:	Artistic
Group:		Development/Perl
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/dist/IO-Zlib/Zlib.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOMHUGHES/IO-Zlib-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
Requires:	SUNWperl584core

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Tom Hughes <tom@compton.nu>
Meta(info.upstream_url):        http://search.cpan.org/dist/IO-Zlib/Zlib.pm

%description
IO::Zlib provides an IO:: style interface to Compress::Zlib and hence to
gzip/zlib compressed files. It provides many of the same methods as the
IO::Handle interface.

%prep
%setup -q -n IO-Zlib-%{version}

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
