#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.10
%define		qtver		5.15.2
%define		kpname		systemsettings
Summary:	KDE system settings
Name:		kp5-%{kpname}
Version:	5.27.10
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	1319f82a4043456a4cb99cfcc2ba90fe
URL:		https://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
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
BuildRequires:	kp5-plasma-workspace-devel >= %{kdeplasmaver}
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
rm -rf po/id
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

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
%attr(755,root,root) %{_libdir}/libsystemsettingsview.so.3
%{_libdir}/qt5/plugins/kf5/krunner/krunner_systemsettings.so
%attr(755,root,root) %{_bindir}/systemsettings
%{_datadir}/kservicetypes5/infocenterexternalapp.desktop
%{zsh_compdir}/_systemsettings
