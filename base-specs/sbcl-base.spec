#
# spec file for package: sbcl
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		sbcl
Version:	1.0.28
Source0:	http://voxel.dl.sourceforge.net/sourceforge/sbcl/%{name}-%{version}-source.tar.bz2
Source1:	http://voxel.dl.sourceforge.net/sourceforge/sbcl/%{bindist}-binary.tar.bz2

%prep
%setup -q
bzip2 -dc %{SOURCE1} | tar -xf -

%build
sed -i 's@/usr/local/lib/sbcl@%{sbclhome}@' src/runtime/runtime.c
SBCL_ARCH=%{sbclarch} sh make.sh "%{bindist}/src/runtime/sbcl --core %{bindist}/output/sbcl.core" || true

%install
INSTALL_ROOT=$RPM_BUILD_ROOT/usr sh install.sh

%clean
rm -rf $RPM_BUILD_ROOT
