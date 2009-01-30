Name:		libsigsegv
Version:	2.6
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-shared
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
