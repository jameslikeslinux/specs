#
# spec file for package: par2
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use par2_64 = par2-base.spec
%endif
%include base.inc
%use par2 = par2-base.spec

Name:		par2
Version:	%{par2.version}
Summary:	PAR 2.0 compatible file verification and repair tool
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://parchive.sourceforge.net/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWgnu-automake-19
BuildRequires:	SUNWaconf
BuildRequires:  SUNWggrp

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Peter Brian Clements <peterbclements@users.sourceforge.net>
Meta(info.upstream_url):	http://parchive.sourceforge.net/
Meta(info.classification):	org.opensolaris.category.2008:Applications/System Utilities

%description
A command line implementation of the PAR v2.0 specification. This specification
is used for parity checking and repair of a file set. If the files in the
recovery set ever get damaged (e.g. when they are transmitted or stored on a
faulty disk) the client can read the damaged input files, read the (possibly
damaged) PAR files, and regenerate the original input files. Of course, not all
damages can be repaired, but many can. 

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%par2_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%par2.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%par2_64.build -d %{name}-%{version}/%{_arch64}
%endif
%par2.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%par2_64.install -d %{name}-%{version}/%{_arch64}
%endif
%par2.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/par2 $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/par2create $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/par2repair $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/par2verify $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec par2
ln -s ../lib/isaexec par2create
ln -s ../lib/isaexec par2repair
ln -s ../lib/isaexec par2verify
%endif

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/par2
%hard %{_bindir}/%{_arch64}/par2create
%hard %{_bindir}/%{_arch64}/par2repair
%hard %{_bindir}/%{_arch64}/par2verify
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/par2
%hard %{_bindir}/%{base_isa}/par2create
%hard %{_bindir}/%{base_isa}/par2repair
%hard %{_bindir}/%{base_isa}/par2verify
%hard %{_bindir}/par2
%hard %{_bindir}/par2create
%hard %{_bindir}/par2repair
%hard %{_bindir}/par2verify
%else
%{_bindir}/par2
%hard %{_bindir}/par2create
%hard %{_bindir}/par2repair
%hard %{_bindir}/par2verify
%endif
%attr(755,root,sys) %dir %{_datadir}
%dir %{_mandir}
%dir %{_mandir}/man1
%{_mandir}/man1/par2.1
%hard %{_mandir}/man1/par2create.1
%hard %{_mandir}/man1/par2repair.1
%hard %{_mandir}/man1/par2verify.1

%changelog
* Thu Jan 07 2010 - jlee@thestaticvoid.com
- Initial version
