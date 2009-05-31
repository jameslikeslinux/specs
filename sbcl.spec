%include Solaris.inc
%ifarch amd64 
%include arch64.inc
%define bindist sbcl-1.0.23-x86-solaris
%define sbclarch x86-64
%define sbclhome /usr/lib/amd64/sbcl
%use sbcl_64 = sbcl-base.spec
%endif
%include base.inc
%ifarch i386
%define bindist sbcl-1.0.23-x86-solaris
%define sbclarch x86
%define sbclhome /usr/lib/sbcl
%endif
%ifarch sparc sparcv9
%define bindist sbcl-1.0.23-sparc-solaris
%define sbclarch sparc
%define sbclhome /usr/lib/sbcl
%endif
%use sbcl = sbcl-base.spec

Name:		sbcl
Version:	%{sbcl.version}
Summary:	A Common Lisp Implementation
License:	BSD
Group:		Development/Other Languages
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.sbcl.org/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		SBCL <sbcl-devel@lists.sourceforge.net>
Meta(info.upstream_url):	http://www.sbcl.org/

%description
Steel Bank Common Lisp (SBCL) is an open source (free software) compiler and
runtime system for ANSI Common Lisp. It provides an interactive environment
including an integrated native compiler, a debugger, and many extensions.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64
mkdir %{name}-%{version}/%{_arch64}
%sbcl_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%sbcl.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64
%sbcl_64.build -d %{name}-%{version}/%{_arch64}
%endif
%sbcl.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64
%sbcl_64.install -d %{name}-%{version}/%{_arch64}
mkdir $RPM_BUILD_ROOT%{_bindir}/%{_arch64}
mv $RPM_BUILD_ROOT%{_bindir}/sbcl $RPM_BUILD_ROOT%{_bindir}/%{_arch64}
mkdir $RPM_BUILD_ROOT%{_libdir}/%{_arch64}
mv $RPM_BUILD_ROOT%{_libdir}/sbcl $RPM_BUILD_ROOT%{_libdir}/%{_arch64}
%endif
%sbcl.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/sbcl $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec sbcl
%endif

rm -rf $RPM_BUILD_ROOT%{_datadir}/info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%ifarch amd64
%{_bindir}/%{_arch64}/sbcl
%{_libdir}/%{_arch64}/sbcl
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/sbcl
%hard %{_bindir}/sbcl
%else
%{_bindir}/sbcl
%endif
%{_libdir}/sbcl
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_datadir}/doc
%{_datadir}/doc/sbcl
%{_mandir}/man1/sbcl.1

%changelog
* Sat May 30 2009 - jlee@thestaticvoid.com
- Initial version
