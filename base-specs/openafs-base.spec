Name:		openafs
Version:	1.4.8
Source0:	http://openafs.org/dl/openafs/%{version}/openafs-%{version}-src.tar.bz2
Patch0:		openafs-amd64.patch

%prep
%setup -q
%patch0 -p1

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --libexecdir=/usr/lib --sbindir=%{_sbindir} --with-afs-sysname=%{sysname} --with-krb5-conf=/usr/bin/krb5-config
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT
