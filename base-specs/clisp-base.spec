Name:		clisp
Version:	2.46
Source0:	http://ftp.gnu.org/pub/gnu/%{name}/release/%{version}/%{name}-%{version}.tar.bz2
Patch0:		clisp-libsigsegv-2.6.patch
Patch1:		clisp-detect-multilib.patch

%prep
%setup -q
%patch0
%patch1

%build
export CC="%{cc}"
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} %{confargs}
cd src
make

%install
cd src
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
