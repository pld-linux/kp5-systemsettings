%define		kdeplasmaver	5.21.3
%define		qtver		5.9.0
%define		kpname		systemsettings
Summary:	KDE system settings
Name:		kp5-%{kpname}
Version:	5.21.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	f3068d6246cbe9b1df120a92da41ac3c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kactivities-devel
BuildRequires:	kf5-kactivities-stats-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-khtml-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kirigami2-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE system settings.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
rm -rf po/id
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/systemsettings5
%{_desktopdir}/kdesystemsettings.desktop
%{_desktopdir}/systemsettings.desktop
%{_datadir}/kservices5/settings-*.desktop
%{_datadir}/kservicetypes5/systemsettings*.desktop
%{_datadir}/kxmlgui5/systemsettings
%{_datadir}/systemsettings
%{_datadir}/kpackage/genericqml/org.kde.systemsettings.sidebar
%{_datadir}/metainfo/org.kde.systemsettings.metainfo.xml
%{_datadir}/qlogging-categories5/systemsettings.categories
%dir %{_libdir}/qt5/plugins/systemsettingsview
%attr(755,root,root) %{_libdir}/qt5/plugins/systemsettingsview/icon_mode.so
%attr(755,root,root) %{_libdir}/qt5/plugins/systemsettingsview/systemsettings_sidebar_mode.so
%{_datadir}/kglobalaccel/systemsettings.desktop
