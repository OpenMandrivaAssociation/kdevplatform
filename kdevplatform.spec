%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

# Don't do it when debug is set to nil (like in 2012.1)
%if %{unstable}
#define dont_strip 1
%endif

%define kdevelop_ver 4.%(echo %{version} | cut -d. -f2,3)

%define libname_orig libkdevplatform4
%define major	5
%define libname %mklibname kdevplatform %{major}
%define old_major 2
%define old_libname %mklibname kdevplatform4 %{old_major}

Summary:	Integrated Development Environment for C++/C
Name:		kdevplatform
Epoch:		4
Version:	5.0.3
Release:	1
Group:		Development/C++
License:	GPLv2
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/kdevelop/%{version}/src/kdevplatform-%{version}.tar.xz
Patch1:		kdevplatform-5.0.3-bsdtar.patch
BuildRequires:	flex
BuildRequires:	graphviz
BuildRequires:	boost-devel
BuildRequires:	db-devel
BuildRequires:	subversion-devel
BuildRequires:	pkgconfig(apr-1)
BuildRequires:	pkgconfig(apr-util-1)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	cmake(LibKompareDiff2)

BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5XmlGui)

BuildRequires:	cmake(Grantlee5)

BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5QuickWidgets)

%if %{compile_apidox}
BuildRequires:	doxygen
%endif

%description
%{name} module needed by Kdevelop or Quanta

%files -f %{name}.lang
%{_bindir}/kdev_dbus_socket_transformer
%{_bindir}/kdev_format_source
%{_bindir}/kdevplatform_shell_environment.sh
%{_datadir}/kdevcodegen
%{_datadir}/kdevcodeutils
%{_iconsdir}/hicolor/22x22/actions/run-clean.png
%{_iconsdir}/hicolor/22x22/actions/run-install.png
%{_iconsdir}/hicolor/*/apps/git.png
%{_iconsdir}/hicolor/*/apps/subversion.*
%{_iconsdir}/hicolor/*/apps/bazaar.png
%{_iconsdir}/hicolor/*/actions/breakpoint.png
%{_libdir}/qt5/plugins/kdevplatform
%{_libdir}/qt5/plugins/grantlee/5.1/kdev_filters.so
%{_libdir}/qt5/qml/org/kde/kdevplatform/libkdevelopdashboarddeclarativeplugin.so
%{_libdir}/qt5/qml/org/kde/kdevplatform/qmldir
%{_datadir}/kservicetypes5/kdevelopplugin.desktop

#-----------------------------------------------------------------------------

%define kdevplatformtests_major 10
%define libkdevplatformtests %mklibname KDevPlatformTests %{kdevplatformtests_major}

%package -n %{libkdevplatformtests}
Summary:	KF5 library
Group:		System/Libraries

%description -n %{libkdevplatformtests}
KF5 library.

%files -n %{libkdevplatformtests}
%{_libdir}/libKDevPlatformTests.so.%{kdevplatformtests_major}*

#-----------------------------------------------------------------------------

%define kdevplatforminterfaces_major 10
%define libkdevplatforminterfaces %mklibname KDevPlatformInterfaces %{kdevplatforminterfaces_major}

%package -n %{libkdevplatforminterfaces}
Summary:	KF5 library
Group:		System/Libraries

%description -n %{libkdevplatforminterfaces}
KF5 library.

%files -n %{libkdevplatforminterfaces}
%{_libdir}/libKDevPlatformInterfaces.so.%{kdevplatforminterfaces_major}*

#-----------------------------------------------------------------------------

%define kdevplatformlanguage_major 10
%define libkdevplatformlanguage %mklibname KDevPlatformLanguage %{kdevplatformlanguage_major}

%package -n %{libkdevplatformlanguage}
Summary:	KF5 library
Group:		System/Libraries

%description -n %{libkdevplatformlanguage}
KF5 library.

%files -n %{libkdevplatformlanguage}
%{_libdir}/libKDevPlatformLanguage.so.%{kdevplatformlanguage_major}*

#-----------------------------------------------------------------------------

%define kdevplatformoutputview_major 10
%define libkdevplatformoutputview %mklibname KDevPlatformOutputView %{kdevplatformoutputview_major}

%package -n %{libkdevplatformoutputview}
Summary:	KF5 library
Group:		System/Libraries

%description -n %{libkdevplatformoutputview}
KF5 library.

%files -n %{libkdevplatformoutputview}
%{_libdir}/libKDevPlatformOutputView.so.%{kdevplatformoutputview_major}*

#-----------------------------------------------------------------------------

%define kdevplatformproject_major 10
%define libkdevplatformproject %mklibname KDevPlatformProject %{kdevplatformproject_major}

%package -n %{libkdevplatformproject}
Summary:	KF5 library
Group:		System/Libraries

%description -n %{libkdevplatformproject}
KF5 library.

%files -n %{libkdevplatformproject}
%{_libdir}/libKDevPlatformProject.so.%{kdevplatformproject_major}*

#-----------------------------------------------------------------------------

%define kdevplatformshell_major 10
%define libkdevplatformshell %mklibname KDevPlatformShell %{kdevplatformshell_major}

%package -n %{libkdevplatformshell}
Summary:	KF5 library
Group:		System/Libraries

%description -n %{libkdevplatformshell}
KF5 library.

%files -n %{libkdevplatformshell}
%{_libdir}/libKDevPlatformShell.so.%{kdevplatformshell_major}*

#-----------------------------------------------------------------------------

%define kdevplatformutil_major 10
%define libkdevplatformutil %mklibname KDevPlatformUtil %{kdevplatformutil_major}

%package -n %{libkdevplatformutil}
Summary:	KF5 library
Group:		System/Libraries

%description -n %{libkdevplatformutil}
KF5 library.

%files -n %{libkdevplatformutil}
%{_libdir}/libKDevPlatformUtil.so.%{kdevplatformutil_major}*

#-----------------------------------------------------------------------------

%define kdevplatformvcs_major 10
%define libkdevplatformvcs %mklibname KDevplatformVcs %{kdevplatformvcs_major}

%package -n %{libkdevplatformvcs}
Summary:	KF5 library
Group:		System/Libraries

%description -n %{libkdevplatformvcs}
KF5 library.

%files -n %{libkdevplatformvcs}
%{_libdir}/libKDevPlatformVcs.so.%{kdevplatformvcs_major}*

#-----------------------------------------------------------------------------

%define sublime_major 10
%define libsublime %mklibname KDevPlatformSublime %{sublime_major}

%package -n %{libsublime}
Summary:	KF5 library
Group: System/Libraries

%description -n %{libsublime}
KF5 library.

%files -n %{libsublime}
%{_libdir}/libKDevPlatformSublime.so.%{sublime_major}*

#-----------------------------------------------------------------------------

%define kdevplatformdebugger_major 10
%define libkdevplatformdebugger %mklibname KDevPlatformDebugger %{kdevplatformdebugger_major}

%package -n %{libkdevplatformdebugger}
Summary:	KF5 library
Group:		System/Libraries

%description -n %{libkdevplatformdebugger}
KF5 library.

%files -n %{libkdevplatformdebugger}
%{_libdir}/libKDevPlatformDebugger.so.%{kdevplatformdebugger_major}*

#-----------------------------------------------------------------------------

%define kdevplatformdocumentation_major 10
%define libkdevplatformdocumentation %mklibname KDevPlatformDocumentation %{kdevplatformdocumentation_major}

%package -n %{libkdevplatformdocumentation}
Summary:	KF5 library
Group:		System/Libraries

%description -n %{libkdevplatformdocumentation}
KF5 library.

%files -n %{libkdevplatformdocumentation}
%{_libdir}/libKDevPlatformDocumentation.so.%{kdevplatformdocumentation_major}*


#-----------------------------------------------------------------------------

%define kdevplatformserialization_major 10
%define libkdevplatformserialization %mklibname KDevPlatformSerialization %kdevplatformserialization_major

%package -n %libkdevplatformserialization
Summary: KF5 library
Group: System/Libraries

%description -n %libkdevplatformserialization
KF5 library.

%files -n %libkdevplatformserialization
%_libdir/libKDevPlatformSerialization.so.%{kdevplatformserialization_major}*

#-----------------------------------------------------------------------------

%package -n %{libname}-devel
Summary:	Development files for kdevplatform
Group:		Development/KDE and Qt

Provides:	kdevplatform-devel = %{EVRD}

Requires:	%{libkdevplatformtests} = %{EVRD}
Requires:	%{libkdevplatforminterfaces} = %{EVRD}
Requires:	%{libkdevplatformlanguage} = %{EVRD}
Requires:	%{libkdevplatformoutputview} = %{EVRD}
Requires:	%{libkdevplatformproject} = %{EVRD}
Requires:	%{libkdevplatformshell} = %{EVRD}
Requires:	%{libkdevplatformutil} = %{EVRD}
Requires:	%{libkdevplatformvcs} = %{EVRD}
Requires:	%{libsublime} = %{EVRD}
Requires:	%{libkdevplatformdebugger} = %{EVRD}
Requires:	%{libkdevplatformdocumentation} = %{EVRD}
Requires:	%{libkdevplatformserialization} = %{EVRD}

%description -n %{libname}-devel
Development files for kdevplatform.

%files -n %{libname}-devel
%{_libdir}/cmake/KDevPlatform
%{_includedir}/kdevplatform
%{_libdir}/libKDevPlatformSerialization.so
%{_libdir}/libKDevPlatformTests.so
%{_libdir}/libKDevPlatformInterfaces.so
%{_libdir}/libKDevPlatformLanguage.so
%{_libdir}/libKDevPlatformOutputView.so
%{_libdir}/libKDevPlatformProject.so
%{_libdir}/libKDevPlatformShell.so
%{_libdir}/libKDevPlatformUtil.so
%{_libdir}/libKDevPlatformVcs.so
%{_libdir}/libKDevPlatformSublime.so
%{_libdir}/libKDevPlatformDebugger.so
%{_libdir}/libKDevPlatformDocumentation.so

#-----------------------------------------------------------------------------

%prep
%setup -qn kdevplatform-%{version}
%apply_patches

%build
%cmake_kde5 -DBSDTAR=1
%ninja

%if %{compile_apidox}
make apidox
%endif

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-kde

