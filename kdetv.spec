#
# Conditional build:
%bcond_without	lirc		# without lirc support
#
Summary:	KDE Video4Linux Stream Capture Viewer
Summary(de.UTF-8):	Video4Linux Stream Player für KDE
Summary(pl.UTF-8):	Przeglądarka strumienia Video4Linux dla KDE
Name:		kdetv
Version:	0.8.9
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dziegel.free.fr/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	7a5d73e08bc133cc2db228cb6655670e
Patch0:		%{name}.desktop.patch
Patch1:		kde-ac260.patch
Patch2:		kde-ac260-lt.patch
Patch3:		kde-am.patch
URL:		http://www.kdetv.org/
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	arts-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	kdelibs-devel >= 9:3.3.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	zlib-devel
BuildRequires:	zvbi-devel
Obsoletes:	kwintv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdetv is a KDE application based on the bttv-driver by Ralph Metzler.
kdetv allows you to watch TV in a window on your PC screen.

%description -l de.UTF-8
Kdetv ist eine KDE Applikation die auf den bttv Treiber von Ralph
Metzler bassiert. Kdetv ermöglicht es TV auf ihren PC zu gucken.

%description -l pl.UTF-8
kdetv jest aplikacją KDE bazującą na sterowniku bttv autorstwa Ralpha
Metzlera. kdetv pozwala na oglądanie TV w oknie na ekranie PC.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.* admin
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?with_lirc:en}%{!?with_lirc:dis}able-kdetv-lirc \
	--with-alsa-dir=%{_prefix} \
	--with-qt-libraries=%{_libdir} \
	--with-zvbi-dir=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	kde_appsdir=%{_desktopdir} \
	kde_htmldir=%{_kdedocdir} \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_desktopdir}/Multimedia/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so*
%{_libdir}/kde3/*.la
%{_libdir}/*.la
%{_desktopdir}/*.desktop
%{_datadir}/apps/kdetv
%{_datadir}/apps/profiles/*
%{_datadir}/services/kdetv
%{_datadir}/servicetypes/kdetv
%{_iconsdir}/hicolor/*/*/*.png
