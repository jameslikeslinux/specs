#
# spec file for package: perl-version
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-version
Version:	0.76
Summary:	Perl extension for Version Objects
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~jpeacock/version-%{version}/lib/version.pod
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/J/JP/JPEACOCK/version-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
Requires:	SUNWperl584core

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            John Peacock <jpeacock@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~jpeacock/version-%{version}/lib/version.pod
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Overloaded version objects for all modern versions of Perl. This module
implements all of the features of version objects which are part of Perl
5.10.0

%prep
%setup -q -n version-%{version}

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
