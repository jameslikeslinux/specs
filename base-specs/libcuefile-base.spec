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
$CC -shared -Iinclude -Isrc %{optflags} %{_ldflags} src/*.c -o libcuefile.so.0.0.0

%install
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -r include/cuetools $RPM_BUILD_ROOT%{_includedir}

mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp libcuefile.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}
cd $RPM_BUILD_ROOT%{_libdir}
ln -s libcuefile.so.0.0.0 libcuefile.so.0
ln -s libcuefile.so.0.0.0 libcuefile.so

%clean
rm -rf $RPM_BUILD_ROOT
