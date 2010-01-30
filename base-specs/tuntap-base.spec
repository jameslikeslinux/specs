#
# spec file for package: tuntap
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

Name:		tuntap
Version:	20091116
Source0:	http://www.whiteboard.ne.jp/~admin2/tuntap/source/tuntap/tuntap.tar.gz
Patch0:		tuntap-00-install-user.diff

%prep
%setup -q -n tuntap
%patch0

%build
./configure %{configopts}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
