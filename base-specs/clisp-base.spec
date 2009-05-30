Name:		clisp
Version:	2.47
Source0:	http://ftp.gnu.org/pub/gnu/%{name}/release/%{version}/%{name}-%{version}.tar.bz2
Patch0:		clisp-00-detect-multilib.diff

%prep
%setup -q
%patch0

%build
export CC="%{cc}"
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} %{confargs}
cd src
gmake

%install
cd src
gmake DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
