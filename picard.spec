#
# spec file for package: picard
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define python_version 2.6

Name:		picard
Version:	0.14
Summary:	MusicBrainz Picard
License:	GPLv2
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://musicbrainz.org/doc/MusicBrainz_Picard
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	ftp://ftp.musicbrainz.org/pub/musicbrainz/picard/picard-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWPython26
BuildRequires:	python26-qt
BuildRequires:	python26-mutagen
BuildRequires:	SUNWlibdiscid-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libofa-devel
Requires:	SUNWPython26
Requires:	python26-qt
Requires:	python26-mutagen
Requires:	SUNWlibdiscid
Requires:	ffmpeg
Requires:	libofa

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Lukáš Lalinský <lalinsky@gmail.com>
Meta(info.upstream_url):        http://musicbrainz.org/doc/MusicBrainz_Picard
Meta(info.classification):	org.opensolaris.category.2008:Applications/Sound and Video

%description
MusicBrainz Picard is a cross-platform (Linux/Mac OS X/Windows) application
written in Python and is the official MusicBrainz tagger. 

%prep
%setup -q

%build
python%{python_version} setup.py config

# this is an awful hack
# python distutils on solaris always uses pycc to compile which
# causes c++ compilation to fail.  this sets the c compiler to CC
# so picard.util.astrcmp builds.  it errors out trying to build
# the next c extension, so execute the build again using the
# regular c compiler.
CC=$CXX LDFLAGS="-lCrun" python%{python_version} setup.py build || true
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
%{_bindir}/picard
%{_libdir}/python%{python_version}/vendor-packages/picard
%{_libdir}/python%{python_version}/vendor-packages/picard-%{version}-py%{python_version}.egg-info
%attr(-,root,sys) %dir %{_datadir}
%attr(-,root,other) %dir %{_datadir}/applications
%{_datadir}/applications/picard.desktop
%attr(-,root,other) %{_datadir}/icons
%attr(-,root,other) %{_datadir}/locale

%changelog
* Sat Feb 13 2010 - jlee@thestaticvoid.com
- Initial version
