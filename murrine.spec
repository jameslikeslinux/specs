%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use murrine_64 = murrine-base.spec
%endif
%include base.inc
%use murrine = murrine-base.spec

Name:		murrine
Version:	%{murrine.version}
Release:	1
Summary:	Gtk2 Engine Featuring a Modern Glassy Look
License:	GPL
Group:		Desktop (GNOME)/Theming
Packager:       James Lee <jlee@thestaticvoid.org>
Vendor:		http://www.cimitan.com/murrine/files/%{name}-%{version}.tar.bz2
Url:		http://www.cimitan.com/murrine/
SUNW_Hotline:   %{url}
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright
SUNW_Category:  system

%include default-depend.inc
BuildRequires:	SUNWgnome-common-devel
Requires:	SUNWfontconfig
Requires:	SUNWfreetype2
Requires:	SUNWgnome-base-libs
Requires:	SUNWlexpt
Requires:	SUNWmlib
Requires:	SUNWpng
Requires:	SUNWxorg-clientlibs
Requires:	SUNWxwplt
Requires:	SUNWzlib

%description
Murrine is a Gtk2 engine, written in C language, using cairo vectorial drawing
library to draw widgets. It features a modern glassy look, and it is elegant
and clean on the eyes. It is also extremely customizable.

%package themes
Summary:	Themes for the Murrine engine by Cimi
Group:		Desktop (GNOME)/Theming
Requires:	%{name}

%description themes
This package includes themes by Cimi for the Murrine Gtk2 engine.  The themes
include: MurrinaGilouche, MurrinaAquaish, MurrinaVerdeOlivo, MurrinaBlue,
MurrinaFancyCandy, MurrinaLoveGray, and MurrineRounded.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%murrine_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%murrine.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%murrine_64.build -d %{name}-%{version}/%{_arch64}
%endif
%murrine.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%murrine_64.install -d %{name}-%{version}/%{_arch64}
%endif
%murrine.install -d %{name}-%{version}/%{base_arch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/gtk-2.0/2.10.0/engines/libmurrine.so
%endif
%{_libdir}/gtk-2.0/2.10.0/engines/libmurrine.so

%files themes
%defattr(-,root,bin)
%attr(755,root,sys) %dir %{_datadir}
%{_datadir}/themes/MurrinaAquaIsh/gtk-2.0/gtkrc
%{_datadir}/themes/MurrinaFancyCandy/gtk-2.0/gtkrc
%{_datadir}/themes/MurrinaGilouche/gtk-2.0/gtkrc
%{_datadir}/themes/MurrinaLoveGray/gtk-2.0/gtkrc
%{_datadir}/themes/MurrinaVerdeOlivo/gtk-2.0/gtkrc
%{_datadir}/themes/MurrineRounded/metacity-1/menu-mur.png
%{_datadir}/themes/MurrineRounded/metacity-1/menu.png
%{_datadir}/themes/MurrineRounded/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/MurrineRoundedIcon/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/MurrineRoundedLessFramed/metacity-1/menu-mur.png
%{_datadir}/themes/MurrineRoundedLessFramed/metacity-1/menu.png
%{_datadir}/themes/MurrineRoundedLessFramed/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/MurrineRoundedLessFramedIcon/metacity-1/menu-mur.png
%{_datadir}/themes/MurrineRoundedLessFramedIcon/metacity-1/menu.png
%{_datadir}/themes/MurrineRoundedLessFramedIcon/metacity-1/metacity-theme-1.xml

