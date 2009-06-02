#
# spec file for package: perl-html-parser
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-html-parser
Version:	3.60
Summary:	HTML Parser Class
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/dist/HTML-Parser/Parser.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/HTML-Parser-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	perl-html-tagset
Requires:	SUNWperl584core
Requires:	perl-html-tagset

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Gisle Aas <gisle@ActiveState.com>
Meta(info.upstream_url):        http://search.cpan.org/dist/HTML-Parser/Parser.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
The HTML::Parser class will recognize markup and separate it from plain text
(alias data content) in HTML documents. As different kinds of markup and text
are recognized, the corresponding event handlers are invoked.

%prep
%setup -q -n HTML-Parser-%{version}

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
