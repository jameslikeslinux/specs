#
# spec file for package: python26-mutagen
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define python_version 2.6

Name:		python26-mutagen
Version:	1.18
Summary:	Audio Metadata Editing Library
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://code.google.com/p/mutagen/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://mutagen.googlecode.com/files/mutagen-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWPython26
Requires:	SUNWPython26

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Joe Wreschnig <piman@sacredchao.net>
Meta(info.upstream_url):        http://code.google.com/p/mutagen/
Meta(info.classification):	org.opensolaris.category.2008:Development/Python

%description
Mutagen is a Python module to handle audio metadata. It supports ASF, FLAC,
M4A, Monkey's Audio, MP3, Musepack, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg
Vorbis, True Audio, WavPack and OptimFROG audio files. All versions of ID3v2
are supported, and all standard ID3v2.4 frames are parsed. It can read Xing
headers to accurately calculate the bitrate and length of MP3s. ID3 and APEv2
tags can be edited regardless of audio format. It can also manipulate Ogg
streams on an individual packet/page level.

%prep
%setup -q -n mutagen-%{version}

%build
python%{python_version} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python%{python_version} setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

# move to vendor-packages
if [ -d $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages ] ; then
	mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages
	mv $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages/* \
		$RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages/
	rmdir $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{_bindir}/moggsplit
%{_bindir}/mid3iconv
%{_bindir}/mid3v2
%{_bindir}/mutagen-pony
%{_bindir}/mutagen-inspect
%{_libdir}/python%{python_version}/vendor-packages/mutagen
%{_libdir}/python%{python_version}/vendor-packages/mutagen-%{version}-py%{python_version}.egg-info
%attr(-,root,sys) %dir %{_datadir}
%{_mandir}/man1/mutagen-inspect.1
%{_mandir}/man1/mid3v2.1
%{_mandir}/man1/mutagen-pony.1
%{_mandir}/man1/moggsplit.1
%{_mandir}/man1/mid3iconv.1

%changelog
* Thu Feb 11 2010 - jlee@thestaticvoid.com
- Initial version
