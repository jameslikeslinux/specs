Name:		readline
Version:	5.2
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} --enable-shared
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
