#
# spec file for package: libcuefile
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		libcuefile
Version:	453
Source0:	http://files.musepack.net/source/libcuefile_r%{version}.tar.gz

%prep
%setup -q -n libcuefile_r%{version}

%build
cc -shared -Iinclude -Isrc %{optflags} %{_ldflags} src/*.c -o libcuefile.so

%install
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -r include/cuetools $RPM_BUILD_ROOT%{_includedir}

mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp libcuefile.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT
