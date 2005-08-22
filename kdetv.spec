Summary:	KDE Video4Linux Stream Capture Viewer
Summary(pl):	Przegl±darka strumienia Video4Linux dla KDE
Name:		kdetv
Version:	0.8.8
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dziegel.free.fr/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	587885b528b3b737d3bce07526b7f8e8
Patch0:		%{name}.desktop.patch
URL:		http://www.kdetv.org/
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	arts-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.3.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	lirc-devel
BuildRequires:	zlib-devel
BuildRequires:	zvbi-devel
Obsoletes:	kwintv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdetv is a KDE application based on the bttv-driver by Ralph Metzler.
kdetv allows you to watch TV in a window on your PC screen.

%description -l pl
kdetv jest aplikacj± KDE bazuj±c± na sterowniku bttv autorstwa Ralpha
Metzlera. kdetv pozwala na ogl±danie TV w oknie na ekranie PC.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* admin
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-alsa-dir=%{_prefix} \
	--with-qt-libraries=%{_libdir} \
	--with-zvbi-dir=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	kde_appsdir=%{_desktopdir} \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_desktopdir}/Multimedia/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

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
