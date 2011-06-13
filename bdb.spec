#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%include Solaris.inc

Name:				bdb
URL:				http://www.oracle.com/technology/products/berkeley-db/index.html
Summary:			Oracle Berkeley DB
Version:			4.8.30
%define tar_version %{version}.NC
Source:				http://download.oracle.com/berkeley-db/db-%{tar_version}.tar.gz
License:			Oracle BSD License
Distribution:		OpenSolaris
Vendor:				OpenSolaris Community
SUNW_BaseDir:		/usr
SUNW_Copyright:		%{name}.copyright
BuildRoot:			%{_tmppath}/%{name}-%{version}-build
Meta(info.upstream):	 	Oracle Berkeley DB <berkeleydb-info_us@oracle.com>
Meta(info.maintainer):	 	Emanuele Pucciarelli <ep@acm.org>
Meta(info.classification):	System/Libraries

%include default-depend.inc

%define _docdir /usr/share/doc/bdb

%ifarch amd64 sparcv9
%include arch64.inc
%use thispackage_64 = bdb-base.spec
%endif

%include base.inc
%use thispackage = bdb-base.spec


%prep
rm -rf %name-%{tar_version}
mkdir %name-%{tar_version}

%ifarch amd64 sparcv9
mkdir %name-%{tar_version}/%_arch64
%thispackage_64.prep -d %name-%{tar_version}/%_arch64
%endif

mkdir %name-%{tar_version}/%base_arch
%thispackage.prep -d %name-%{tar_version}/%base_arch

%build


%ifarch amd64 sparcv9
%thispackage_64.build -d %name-%tar_version/%_arch64
%endif

%thispackage.build -d %name-%tar_version/%base_arch


%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%thispackage_64.install -d %name-%tar_version/%_arch64
%endif

%thispackage.install -d %name-%tar_version/%base_arch

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*.so
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) /usr/include
/usr/include/*
%dir %attr (0755, root, bin) %{_docdir}
%{_docdir}/*




%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/*.so
%endif

%changelog
* Tue May 5 2009 - ep@acm.org
- Updated meta info, dependencies.
* Wed Apr 29 2009 - ep@acm.org
- Initial vesion.# rebuild
# trigger re-build
## Re-build 24/09/09
