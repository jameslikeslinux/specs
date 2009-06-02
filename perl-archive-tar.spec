#
# spec file for package: perl-archive-tar
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-archive-tar
Version:	1.48
Summary:	Module for manipulations of tar archives
License:	Artistic
Group:		Development/Perl
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/dist/Archive-Tar/lib/Archive/Tar.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KANE/Archive-Tar-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	perl-io-compress
BuildRequires:	perl-io-zlib
BuildRequires:	perl-package-constants
Requires:	SUNWperl584core
Requires:	perl-io-compress
Requires:	perl-io-zlib
Requires:	perl-package-constants

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Jos Boumans <kane@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/dist/Archive-Tar/lib/Archive/Tar.pm

%description
Archive::Tar provides an object oriented mechanism for handling tar files. It
provides class methods for quick and easy files handling while also allowing
for the creation of tar file objects for custom manipulation. If you have the
IO::Zlib module installed, Archive::Tar will also support compressed or gzipped
tar files.

%prep
%setup -q -n Archive-Tar-%{version}

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLSITEMAN1DIR=%{_mandir}/man1 INSTALLSITEMAN3DIR=%{_mandir}/man3 DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}
%defattr(-,root,bin)
%{_prefix}/perl5
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}

%changelog
* Mon Jun 01 2009 - jlee@thestaticvoid.com
- Initial version
