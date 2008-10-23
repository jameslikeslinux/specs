%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use readline_64 = readline.spec
%endif
%include base.inc
%use readline = readline.spec

Name:		TSVreadline
Version:	%{readline.version}
Summary:	Library for Editing Typed Command Lines
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc

%description
The GNU Readline library provides a set of functions for use by applications
that allow users to edit command lines as they are typed in. Both Emacs and vi
editing modes are available. The Readline library includes additional functions
to maintain a list of previously-entered command lines, to recall and perhaps
reedit those lines, and perform csh-like history expansion on previous
commands. 

This package contains the shared library.

%package devel
Summary:	Headers for readline
Requires:	%{name}

%description devel
The GNU Readline library provides a set of functions for use by applications
that allow users to edit command lines as they are typed in. Both Emacs and vi
editing modes are available. The Readline library includes additional functions
to maintain a list of previously-entered command lines, to recall and perhaps
reedit those lines, and perform csh-like history expansion on previous
commands. 

This package contains the readline development files. 

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%readline_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%readline.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%readline_64.build -d %{name}-%{version}/%{_arch64}
%endif
%readline.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%readline_64.install -d %{name}-%{version}/%{_arch64}
%endif
%readline.install -d %{name}-%{version}/%{base_arch}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libhistory.so.5
%{_libdir}/%{_arch64}/libreadline.so.5
%endif
%{_libdir}/libhistory.so.5
%{_libdir}/libreadline.so.5

%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/libhistory.a
%{_libdir}/%{_arch64}/libhistory.so
%{_libdir}/%{_arch64}/libreadline.a
%{_libdir}/%{_arch64}/libreadline.so
%endif
%{_libdir}/libhistory.a
%{_libdir}/libhistory.so
%{_libdir}/libreadline.a
%{_libdir}/libreadline.so
%{_includedir}/readline/readline.h
%{_includedir}/readline/chardefs.h
%{_includedir}/readline/keymaps.h
%{_includedir}/readline/history.h
%{_includedir}/readline/tilde.h
%{_includedir}/readline/rlstdc.h
%{_includedir}/readline/rlconf.h
%{_includedir}/readline/rltypedefs.h
%attr(755,root,sys) %dir %{_datadir}
%{_infodir}/readline.info
%{_infodir}/rluserman.info
%{_infodir}/history.info
%{_mandir}/man3/history.3
%{_mandir}/man3/readline.3
