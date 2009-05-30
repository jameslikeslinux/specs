%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use libao_64 = libao-base.spec
%endif
%include base.inc
%use libao = libao-base.spec

Name:		libao
Version:	%{libao.version}
Summary:	Cross Platform Audio Library
License:	GPLv2
Group:		System/Libraries
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://www.xiph.org/ao/
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc

Meta(info.maintainer):		James Lee <jlee@thestaticvoid.org>
Meta(info.upstream):		Stan Seibert <volsung@xiph.org>
Meta(info.upstream_url):	http://www.xiph.org/ao/

%description
Libao is a cross-platform audio library that allows programs to output audio
using a simple API on a wide variety of platforms.

This package contains the shared library.

%package devel
Summary:	Headers for libao
Group:		System/Libraries
Requires:	%{name}

%description devel
Libao is a cross-platform audio library that allows programs to output audio
using a simple API on a wide variety of platforms.

This package contains the libao development files.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%libao_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%libao.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%libao_64.build -d %{name}-%{version}/%{_arch64}
%endif
%libao.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libao_64.install -d %{name}-%{version}/%{_arch64}
%endif
%libao.install -d %{name}-%{version}/%{base_arch}

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/amd64/ao/plugins-2/libesd.so
%{_libdir}/amd64/libao.so.2
%{_libdir}/amd64/libao.so.2.1.3
%endif
%{_libdir}/libao.so.2.1.3
%{_libdir}/libao.so.2
%{_libdir}/ao/plugins-2/libesd.so


%files devel
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/amd64/libao.so
%{_libdir}/amd64/libao.la
%{_libdir}/amd64/ao/plugins-2/libesd.la
%attr(755,root,other) %dir %{_libdir}/amd64/pkgconfig
%{_libdir}/amd64/pkgconfig/ao.pc
%endif
%{_libdir}/libao.so
%{_libdir}/libao.la
%{_libdir}/ao/plugins-2/libesd.la
%attr(755,root,other) %dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/ao.pc
%{_includedir}/ao/os_types.h
%{_includedir}/ao/ao.h
%{_includedir}/ao/plugin.h
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_docdir}
%{_docdir}/libao-%{version}/ao_append_option.html
%{_docdir}/libao-%{version}/plugin-api.html
%{_docdir}/libao-%{version}/config.html
%{_docdir}/libao-%{version}/ao_sample_format.html
%{_docdir}/libao-%{version}/ao_option.html
%{_docdir}/libao-%{version}/ao_plugin_test.html
%{_docdir}/libao-%{version}/ao_plugin_set_option.html
%{_docdir}/libao-%{version}/index.html
%{_docdir}/libao-%{version}/drivers.html
%{_docdir}/libao-%{version}/style.css
%{_docdir}/libao-%{version}/ao_file_extension.html
%{_docdir}/libao-%{version}/ao_plugin_device_clear.html
%{_docdir}/libao-%{version}/ao_default_driver_id.html
%{_docdir}/libao-%{version}/ao_driver_info.html
%{_docdir}/libao-%{version}/ao_plugin_file_extension.html
%{_docdir}/libao-%{version}/ao_plugin_open.html
%{_docdir}/libao-%{version}/ao_open_file.html
%{_docdir}/libao-%{version}/ao_driver_id.html
%{_docdir}/libao-%{version}/ao_plugin_close.html
%{_docdir}/libao-%{version}/ao_info.html
%{_docdir}/libao-%{version}/overview.html
%{_docdir}/libao-%{version}/ao_plugin_device_init.html
%{_docdir}/libao-%{version}/ao_play.html
%{_docdir}/libao-%{version}/ao_driver_info_list.html
%{_docdir}/libao-%{version}/ao_free_options.html
%{_docdir}/libao-%{version}/ao_device.html
%{_docdir}/libao-%{version}/ao_plugin_play.html
%{_docdir}/libao-%{version}/ao_example.c
%{_docdir}/libao-%{version}/libao-api.html
%{_docdir}/libao-%{version}/plugin-overview.html
%{_docdir}/libao-%{version}/ao_initialize.html
%{_docdir}/libao-%{version}/ao_plugin_driver_info.html
%{_docdir}/libao-%{version}/ao_close.html
%{_docdir}/libao-%{version}/ao_shutdown.html
%{_docdir}/libao-%{version}/ao_open_live.html
%{_docdir}/libao-%{version}/ao_is_big_endian.html
%{_mandir}/man5/libao.conf.5
%attr(755,root,other) %dir %{_datadir}/aclocal
%{_datadir}/aclocal/ao.m4

%changelog
* Fri May 29 2009 - jlee@thestaticvoid.com
- Initial version
