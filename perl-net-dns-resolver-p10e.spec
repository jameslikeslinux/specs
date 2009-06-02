#
# spec file for package: perl-net-dns-resolver-p10e
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-net-dns-resolver-p10e
Version:	0.003
Summary:	An object-oriented implementation of Sender Policy Framework
License:	BSD
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~jmehnle/Net-DNS-Resolver-Programmable-v%{version}/lib/Net/DNS/Resolver/Programmable.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/J/JM/JMEHNLE/net-dns-resolver-programmable/Net-DNS-Resolver-Programmable-v%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	perl-module-build
BuildRequires:	perl-net-dns
BuildRequires:	perl-version
Requires:	SUNWperl584core
Requires:	perl-net-dns
Requires:	perl-version

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Julian Mehnle <julian@mehnle.net>
Meta(info.upstream_url):        http://search.cpan.org/~jmehnle/Net-DNS-Resolver-Programmable-v%{version}/lib/Net/DNS/Resolver/Programmable.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Net::DNS::Resolver::Programmable is a Net::DNS::Resolver descendant class that
allows a virtual DNS to be emulated instead of querying the real DNS.

%prep
%setup -q -n Net-DNS-Resolver-Programmable-v%{version}

%build
perl Build.PL --prefix %{_prefix} --destdir $RPM_BUILD_ROOT --install_path lib=%{_prefix}/perl5/vendor_perl/5.8.4 --install_path arch=`ls -d %{_prefix}/perl5/vendor_perl/5.8.4/*-solaris-64int` --install_path bindoc=%{_mandir}/man1 --install_path libdoc=%{_mandir}/man3
./Build

%install
rm -rf $RPM_BUILD_ROOT
./Build pure_install

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
