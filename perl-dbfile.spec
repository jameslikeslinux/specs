#
# spec file for package: perl-dbfile
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-dbfile
Version:	1.820
Summary:	Perl5 access to Berkeley DB version 1.x
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~pmqs/DB_File-%{version}/DB_File.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/DB_File-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	bdb
Requires:	SUNWperl584core
Requires:	bdb

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Paul Marquees <pmqs@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~pmqs/DB_File-%{version}/DB_File.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Compress::Raw::Bzip2 provides an interface to the in-memory
compression/uncompression functions from the bzip2 compression library.

%prep
%setup -q -n DB_File-%{version}

%build
perl Makefile.PL PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}

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
