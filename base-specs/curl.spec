Name:		curl
Version:	7.19.0
Source0:	http://curl.haxx.se/download/%{name}-%{version}.tar.bz2
Patch0:		curl-sizeof-long.patch

%prep
%setup -q
%patch0
/usr/bin/autoconf

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
