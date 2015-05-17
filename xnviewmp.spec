# TODO
# - system exiftool
# - system Qt4
# NOTE:
# - requires libjpeg6 (in pld build libjpeg6.spec)
Summary:	XnViewMP - The enhanced version of XnView for all platforms
Name:		xnviewmp
Version:	0.72
Release:	0.1
License:	FREEWARE (NO Adware, NO Spyware) for private or educational use
Group:		X11/Applications
Source0:	http://download.xnview.com/XnViewMP-linux.tgz
# NoSource0-md5:	a25161fd85775e6259fa83dc0323377d
NoSource:	0
Source1:	http://download.xnview.com/XnViewMP-linux-x64.tgz
# NoSource1-md5:	1e3ffc900abf13795f148156d7796c72
NoSource:	1
Patch0:		desktop.patch
URL:		http://www.xnview.com/
BuildRequires:	rpmbuild(find_lang) >= 1.37
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_libdir}/%{name}

%description
XnViewMP is the enhanced version to XnView. It is a powerful
cross-platform media browser, viewer and converter. Compatible with
more than 500 formats.

%prep
%setup -qcT
%ifarch %{ix86}
SOURCE=%{S:0}
%endif
%ifarch %{x8664}
SOURCE=%{S:1}
%endif
install -d tmp
tar xf $SOURCE -C tmp
mv tmp/XnView/* .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir},%{_pixmapsdir},%{_desktopdir}}

cp -a AddOn Plugins UI language lib $RPM_BUILD_ROOT%{_appdir}
cp -p PrintPresets.txt country.txt qt.conf $RPM_BUILD_ROOT%{_appdir}
install -p XnView xnview.sh $RPM_BUILD_ROOT%{_appdir}
ln -s %{_appdir}/xnview.sh $RPM_BUILD_ROOT%{_bindir}/xnview

cp -p XnView.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p xnview.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang qt --with-qm
%find_lang xnview --with-qm

cat *.lang > lang.%{name}

# cleanups
# .pod sources
%{__rm} $RPM_BUILD_ROOT%{_appdir}/AddOn/lib/File/RandomAccess.pod
%{__rm} $RPM_BUILD_ROOT%{_appdir}/AddOn/lib/Image/ExifTool.pod

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f lang.%{name}
%defattr(644,root,root,755)
%doc README WhatsNew.txt license.txt
%attr(755,root,root) %{_bindir}/xnview
%{_desktopdir}/XnView.desktop
%{_pixmapsdir}/xnview.png

%dir %{_appdir}
%{_appdir}/PrintPresets.txt
%{_appdir}/country.txt

%attr(755,root,root) %{_appdir}/XnView
%attr(755,root,root) %{_appdir}/xnview.sh

%{_appdir}/UI
%dir %{_appdir}/AddOn
%{_appdir}/AddOn/Masks
%{_appdir}/AddOn/Thumbs

# exiftool
%attr(755,root,root) %{_appdir}/AddOn/exiftool
%dir %{_appdir}/AddOn/lib
%dir %{_appdir}/AddOn/lib/Image
%{_appdir}/AddOn/lib/Image/ExifTool.pm
%{_appdir}/AddOn/lib/Image/ExifTool


%dir %{_appdir}/AddOn/lib/File
%{_appdir}/AddOn/lib/File/RandomAccess.pm

%dir %{_appdir}/Plugins
%attr(755,root,root) %{_appdir}/Plugins/IlmImf.so
%attr(755,root,root) %{_appdir}/Plugins/openjp2.so
%attr(755,root,root) %{_appdir}/Plugins/webp.so

%dir %{_appdir}/language
%lang(bg) %{_appdir}/language/exif_bg.lng
%lang(de) %{_appdir}/language/exif_de.lng
%lang(es) %{_appdir}/language/exif_es.lng
%lang(fi) %{_appdir}/language/exif_fi.lng
%lang(fr) %{_appdir}/language/exif_fr.lng
%lang(it) %{_appdir}/language/exif_it.lng
%lang(ja) %{_appdir}/language/exif_ja.lng
%lang(pl) %{_appdir}/language/exif_pl.lng
%lang(ru) %{_appdir}/language/exif_ru.lng

# Qt4
%{_appdir}/qt.conf
%dir %{_appdir}/lib
%dir %{_appdir}/lib/codecs
%dir %{_appdir}/lib/imageformats
%dir %{_appdir}/lib/phonon_backend
%attr(755,root,root) %{_appdir}/lib/codecs/lib*codecs.so
%attr(755,root,root) %{_appdir}/lib/imageformats/libq*.so
%attr(755,root,root) %{_appdir}/lib/libQt*.so.4*
%attr(755,root,root) %{_appdir}/lib/libphonon.so.4
%attr(755,root,root) %{_appdir}/lib/phonon_backend/libphonon_gstreamer.so
