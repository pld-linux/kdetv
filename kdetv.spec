Summary:	KDE Video4Linux Stream Capture Viewer
Summary(pl):	Przegl±darka strumienia Video4Linux dla KDE
Name:		kdetv
Version:	0.8.0
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dziegel.free.fr/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	750c5e6b01b5509f2f60358270ffe318
Patch0:		%{name}-userbuild.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.kdetv.org/
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	arts-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	lirc-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	zlib-devel
BuildRequires:	zvbi-devel
Obsoletes:	kwintv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdetv is a KDE application based on the bttv-driver by Ralph Metzler.
kdetv allows you to watch TV in a window on your PC screen.

%description -l pl
kdetv jest aplikacj± KDE bazuj±c± na sterowniku bttv autorstwa Ralpha
Metzlera. kdetv pozwala na ogl±danie TV w oknie na ekranie twojego
PC.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__perl} -pi -e 's@(ac_zvbi_libraries="\$withval"/)lib@$1%{_lib}@' configure
%{__perl} -pi -e 's@(ac_alsa_libraries="\$withval"/)lib@$1%{_lib}@' configure

%build
cp -f /usr/share/automake/config.* admin
%configure \
	--with-alsa-dir=/usr \
	--with-qt-libraries=%{_libdir} \
	--with-zvbi-dir=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	kde_appsdir=%{_desktopdir} \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_desktopdir}/Multimedia/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO VERSION ChangeLog AUTHORS
%attr(0755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so*
%{_libdir}/kde3/*.la
%{_desktopdir}/*.desktop
%{_datadir}/apps/kdetv
%{_datadir}/apps/profiles/*
%{_iconsdir}/*/*/*/*.png
%{_datadir}/services/kdetv
%{_datadir}/servicetypes/kdetv
