#
# spec file for package: perl-inet-socket-inet6
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		perl-inet-socket-inet6
Version:	2.56
Summary:	Object interface for AF_INET|AF_INET6 domain sockets
License:	Artistic
Group:		Development/Perl
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/dist/IO-Socket-INET6/lib/IO/Socket/INET6.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/IO-Socket-INET6-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	perl-socket6
Requires:	SUNWperl584core
Requires:	perl-socket6

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Shlomi Fish <shlomif@iglu.org.il>
Meta(info.upstream_url):        http://search.cpan.org/dist/IO-Socket-INET6/lib/IO/Socket/INET6.pm

%description
IO::Socket::INET6 provides an object interface to creating and using sockets in
either AF_INET or AF_INET6 domains. It is built upon the IO::Socket interface
and inherits all the methods defined by IO::Socket.

%prep
%setup -q -n IO-Socket-INET6-%{version}

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
