#
# spec file for package: spamassassin
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		spamassassin
Version:	3.2.5
Summary:	Spam Filter
License:	Apache-2.0
Group:		System/Security
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://spamassassin.apache.org/
SUNW_Basedir:	/
SUNW_Copyright: %{name}.copyright

Source0:	http://download.filehat.com/apache/spamassassin/source/Mail-SpamAssassin-%{version}.tar.bz2

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	perl-digest-sha1
BuildRequires:	perl-html-parser
BuildRequires:	perl-net-dns
BuildRequires:	perl-lwp
BuildRequires:	perl-io-zlib
BuildRequires:	perl-archive-tar
BuildRequires:	perl-dbfile
Requires:	SUNWperl584core
Requires:	perl-digest-sha1
Requires:	perl-html-parser
Requires:	perl-net-dns
Requires:	perl-lwp
Requires:	perl-io-zlib
Requires:	perl-archive-tar
Requires:	perl-dbfile

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Apache.org <users@spamassassin.apache.org>
Meta(info.upstream_url):        http://spamassassin.apache.org/

%description
SpamAssassin is a mail filter which attempts to identify spam using
a variety of mechanisms including text analysis, Bayesian filtering,
DNS blocklists, and collaborative filtering databases.

%prep
%setup -q -n Mail-SpamAssassin-%{version}

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
