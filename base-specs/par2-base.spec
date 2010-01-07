#
# spec file for package: par2
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		par2
Version:	0.4
Source0:	http://downloads.sourceforge.net/project/parchive/par2cmdline/%{version}/par2cmdline-%{version}.tar.gz
Source1:	par2.1
Patch0:		par2-00-sunstudio.diff

%prep
%setup -q -n par2cmdline-%{version}
%patch0 -p1
aclocal-1.9
autoheader
autoconf
automake-1.9

%build
export CXXFLAGS="%{cxx_optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --bindir=%{_bindir}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
cd $RPM_BUILD_ROOT%{_bindir}
ln -sf par2 par2create
ln -sf par2 par2repair
ln -sf par2 par2verify

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1
cd $RPM_BUILD_ROOT%{_mandir}/man1
ln -sf par2.1 par2create.1
ln -sf par2.1 par2repair.1
ln -sf par2.1 par2verify.1

%clean
rm -rf $RPM_BUILD_ROOT
