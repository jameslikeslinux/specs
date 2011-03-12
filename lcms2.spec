#
# spec file for package: lcms2
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use lcms2_64 = lcms2-base.spec
%endif
%include base.inc
%use lcms2 = lcms2-base.spec

Name:		lcms2
Version:	%{lcms2.version}
Summary:	Color Management Library
License:	MIT
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.littlecms.com/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWjpg-devel
BuildRequires:	SUNWTiff-devel
BuildRequires:	SUNWzlib
Requires:	SUNWjpg
Requires:	SUNWTiff
Requires:	SUNWzlib

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		Marti Maria <info@littlecms.com>
Meta(info.upstream_url):	https://github.com/mm2/Little-CMS
Meta(info.classification):	org.opensolaris.category.2008:System/Libraries

%description
A free, open source, CMM engine. It provides fast transforms between ICC
profiles.

This package contains the shared library.

%package devel
Summary:	Headers for lcms2
Requires:	%{name}

%description devel
A free, open source, CMM engine. It provides fast transforms between ICC
profiles.

This package contains the lcms2 development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%lcms2_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%lcms2.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%lcms2_64.build -d %{name}-%{version}/%{_arch64}
%endif
%lcms2.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%lcms2_64.install -d %{name}-%{version}/%{_arch64}
%endif
%lcms2.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}

mv $RPM_BUILD_ROOT%{_bindir}/tificc $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/transicc $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/linkicc $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/jpgicc $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/psicc $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec tificc
ln -s ../lib/isaexec transicc
ln -s ../lib/isaexec linkicc
ln -s ../lib/isaexec jpgicc
ln -s ../lib/isaexec psicc
%endif

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/tificc
%{_bindir}/%{_arch64}/transicc
%{_bindir}/%{_arch64}/linkicc
%{_bindir}/%{_arch64}/jpgicc
%{_bindir}/%{_arch64}/psicc
%{_libdir}/%{_arch64}/liblcms2.so.2
%{_libdir}/%{_arch64}/liblcms2.so.2.0.1
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/tificc
%{_bindir}/%{base_isa}/transicc
%{_bindir}/%{base_isa}/linkicc
%{_bindir}/%{base_isa}/jpgicc
%{_bindir}/%{base_isa}/psicc
%hard %{_bindir}/tificc
%hard %{_bindir}/transicc
%hard %{_bindir}/linkicc
%hard %{_bindir}/jpgicc
%hard %{_bindir}/psicc
%else
%{_bindir}/tificc
%{_bindir}/transicc
%{_bindir}/linkicc
%{_bindir}/jpgicc
%{_bindir}/psicc
%endif
%{_libdir}/liblcms2.so.2
%{_libdir}/liblcms2.so.2.0.1
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}/man1/tificc.1
%{_mandir}/man1/jpgicc.1


%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/liblcms2.so
%{_libdir}/%{_arch64}/liblcms2.la
%attr(755,root,other) %dir %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/lcms2.pc
%endif
%{_libdir}/liblcms2.so
%{_libdir}/liblcms2.la
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/lcms2.pc
%{_includedir}/lcms2.h
%{_includedir}/lcms2_plugin.h
%attr(755,root,sys) %dir %{_datadir}

%changelog
* Thu Mar 10 2011 - jlee@thestaticvoid.com
- Initial version
