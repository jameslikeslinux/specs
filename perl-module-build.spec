#
# spec file for package: perl-module-build
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-module-build
Version:	0.33
Summary:	Build and install Perl modules
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~ewilhelm/Module-Build-%{version}/lib/Module/Build.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/E/EW/EWILHELM/Module-Build-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
Requires:	SUNWperl584core

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Eric Wilhelm <ewilhelm@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~ewilhelm/Module-Build-%{version}/lib/Module/Build.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Module::Build is a system for building, testing, and installing Perl modules.
It is meant to be an alternative to ExtUtils::MakeMaker.

%prep
%setup -q -n Module-Build-%{version}

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
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}

%changelog
* Mon Jun 01 2009 - jlee@thestaticvoid.com
- Initial version
