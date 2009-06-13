#
# spec file for package: perl-mail-spf
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define real_version 2.006

Name:		perl-mail-spf
Version:	2.0.0.6
Summary:	An object-oriented implementation of Sender Policy Framework
License:	BSD
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/dist/Mail-SPF/lib/Mail/SPF.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/J/JM/JMEHNLE/mail-spf/Mail-SPF-v%{real_version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	perl-module-build
BuildRequires:	perl-error
BuildRequires:	perl-net-dns
BuildRequires:	perl-net-dns-resolver-p10e
BuildRequires:	perl-netaddr-ip
BuildRequires:	perl-uri
BuildRequires:	perl-version
Requires:	SUNWperl584core
Requires:	perl-error
Requires:	perl-net-dns
Requires:	perl-net-dns-resolver-p10e
Requires:	perl-netaddr-ip
Requires:	perl-uri
Requires:	perl-version

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Julian Mehnle <julian@mehnle.net>
Meta(info.upstream_url):        http://search.cpan.org/dist/Mail-SPF/lib/Mail/SPF.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Mail::SPF is an object-oriented implementation of Sender Policy Framework
(SPF). See http://www.openspf.org for more information about SPF.

%prep
%setup -q -n Mail-SPF-v%{real_version}

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
%{_bindir}
%{_prefix}/perl5
%{_sbindir}
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}

%changelog
* Mon Jun 01 2009 - jlee@thestaticvoid.com
- Initial version
* Fri Jun 12 2009 - jlee@thestaticvoid.com
- Separate zeros with dots in version number for IPS compatibility.
