#
# spec file for package: perl-error
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-error
Version:	0.17015
Summary:	Error/exception handling in an OO-ish way
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~shlomif/Error-%{version}/lib/Error.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/Error-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
Requires:	SUNWperl584core

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Shlomi Fish <shlomif@iglu.org.il>
Meta(info.upstream_url):        http://search.cpan.org/~shlomif/Error-%{version}/lib/Error.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
The Error package provides two interfaces. Firstly Error provides a procedural
interface to exception handling. Secondly Error is a base class for
errors/exceptions that can either be thrown, for subsequent catch, or can
simply be recorded.

%prep
%setup -q -n Error-%{version}

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
