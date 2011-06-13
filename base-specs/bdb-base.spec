#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%prep
cat %{SOURCE} | gzip -dc | tar xf -

%build
cd db-%tar_version/build_unix
../dist/configure --prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--docdir=%{_docdir} \
	--enable-static=no
make

%install
cd db-%tar_version/build_unix
make install DESTDIR=$RPM_BUILD_ROOT docdir=%{_docdir}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Wed Apr 29 2009 - ep@acm.org
- Initial vesion.