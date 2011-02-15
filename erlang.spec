#
# spec file for package: erlang
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define mybindir %{_bindir}

%ifarch amd64 
%include arch64.inc
%define optflags -m64
%define _ldflags -m64 -L/usr/lib/amd64 -R/usr/lib/amd64 
%use erlang_64 = erlang-base.spec
%endif
%include base.inc
%define optflags
%define _ldflags
%if %can_isaexec
%define mybindir %{_bindir}/%{base_isa}
%endif
%use erlang = erlang-base.spec

Name:		erlang
Version:	%{erlang.version}
Summary:	Erlang programming language and OTP libraries
License:	Erlang Public License
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.erlang.org/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
BuildRequires:	SUNWgcc432
BuildRequires:	SUNWggrp
BuildRequires:	SUNWbtool
BuildRequires:	SUNWj6dev
BuildRequires:	SUNWopenssl-include
BuildRequires:	SUNWopenssl-libraries
BuildRequires:	wxwidgets-devel
Requires:	SUNWopenssl-libraries
Requires:	wxwidgets

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):		erlang-bugs@erlang.org
Meta(info.upstream_url):	http://www.erlang.org/
Meta(info.classification):	org.opensolaris.category.2008:Development/Other Languages

%description
Open Source Erlang is a functional programming language designed at the
Ericsson Computer Science Laboratory.

Some of Erlang main features are:

 * Clear declarative syntax and is largely free from side-effects;
 * Builtin support for real-time, concurrent and distributed programming;
 * Designed for development of robust and continously operated programs;
 * Dynamic code replacement at runtime.

The Erlang distribution also includes OTP (Open Telecom Platform) which
provides a reach set of libraries and applications. 

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64
mkdir %{name}-%{version}/%{_arch64}
%erlang_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%erlang.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64
%erlang_64.build -d %{name}-%{version}/%{_arch64}
%endif
%erlang.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64
%erlang_64.install -d %{name}-%{version}/%{_arch64}
%endif
%erlang.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
cd $RPM_BUILD_ROOT%{_bindir}
for i in dialyzer epmd erl erlc escript run_erl run_test to_erl typer; do
	ln -s ../lib/isaexec $i
done
%endif

rm -rf $RPM_BUILD_ROOT%{_datadir}/info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%ifarch amd64
%{_bindir}/%{_arch64}/dialyzer
%{_bindir}/%{_arch64}/epmd
%{_bindir}/%{_arch64}/erl
%{_bindir}/%{_arch64}/erlc
%{_bindir}/%{_arch64}/escript
%{_bindir}/%{_arch64}/run_erl
%{_bindir}/%{_arch64}/run_test
%{_bindir}/%{_arch64}/to_erl
%{_bindir}/%{_arch64}/typer
%{_libdir}/%{_arch64}/erlang
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/dialyzer
%{_bindir}/%{base_isa}/epmd
%{_bindir}/%{base_isa}/erl
%{_bindir}/%{base_isa}/erlc
%{_bindir}/%{base_isa}/escript
%{_bindir}/%{base_isa}/run_erl
%{_bindir}/%{base_isa}/run_test
%{_bindir}/%{base_isa}/to_erl
%{_bindir}/%{base_isa}/typer
%hard %{_bindir}/dialyzer
%hard %{_bindir}/epmd
%hard %{_bindir}/erl
%hard %{_bindir}/erlc
%hard %{_bindir}/escript
%hard %{_bindir}/run_erl
%hard %{_bindir}/run_test
%hard %{_bindir}/to_erl
%hard %{_bindir}/typer
%else
%{_bindir}/dialyzer
%{_bindir}/epmd
%{_bindir}/erl
%{_bindir}/erlc
%{_bindir}/escript
%{_bindir}/run_erl
%{_bindir}/run_test
%{_bindir}/to_erl
%{_bindir}/typer
%endif
%{_libdir}/erlang

%changelog
* Fri Jan 21 2011 - jlee@thestaticvoid.com
- Initial version
