#
# spec file for package: libffcall
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libffcall
Version:	1.10
Source0:	http://www.haible.de/bruno/gnu/ffcall-%{version}.tar.gz
Patch0:		libffcall-00-install-mkdir.diff

%prep
%setup -q -n ffcall-%{version}
%patch0

%build
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --mandir=%{_mandir} --enable-shared
gmake %{makeargs}

%install
gmake DESTDIR=$RPM_BUILD_ROOT %{makeargs} install

%clean
rm -rf $RPM_BUILD_ROOT
