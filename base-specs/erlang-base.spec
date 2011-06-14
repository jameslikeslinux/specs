#
# spec file for package: erlang
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		erlang
Version:	14.2.3
Source0:	http://www.erlang.org/download/otp_src_R14B03.tar.gz
Patch0:		erlang-00-hwaddr.diff
Patch1:		erlang-01-wx-sunstudio.diff
Patch2:		erlang-02-_T-to-wxT.diff

%prep
%setup -q -n otp_src_R14B03
%patch0
%patch2

cd lib/wx
%patch1
autoconf

%build
export CC=gcc-4.3.2
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --bindir=%{mybindir} --libdir=%{_libdir} --with-wx-config=%{_bindir}/wx-config
gmake

%install
gmake DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
