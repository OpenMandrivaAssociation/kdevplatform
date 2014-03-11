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
%define major	4
%define libname %mklibname kdevplatform %{major}
%define old_major 2
%define old_libname %mklibname kdevplatform4 %{old_major}

Summary:	Integrated Development Environment for C++/C
Name:		kdevplatform4
Epoch:		4
Version:	1.6.0
Release:	1
Group:		Development/C++
License:	GPLv2
Url:		http://www.kde.org
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/kdevelop/%{kdevelop_ver}/src/kdevplatform-%{version}.tar.xz
BuildRequires:	flex
BuildRequires:	graphviz
BuildRequires:	rapidsvn
BuildRequires:	boost-devel
BuildRequires:	db-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	subversion-devel
BuildRequires:	pkgconfig(apr-1)
BuildRequires:	pkgconfig(apr-util-1)
BuildRequires:	pkgconfig(libccext2)
BuildRequires:	pkgconfig(QJson)
%if %{compile_apidox}
BuildRequires:	doxygen
%endif

%description
%{name} module needed by Kdevelop or Quanta

%files -f %{name}.lang
%{_kde_bindir}/kdev_dbus_socket_transformer
%{_kde_bindir}/kdev_format_source.sh
%{_kde_bindir}/kdevplatform_shell_environment.sh
%{_kde_appsdir}/kdevprojectmanagerview
%{_kde_appsdir}/kdevstandardoutputview
%{_kde_appsdir}/kdevfilemanager
%{_kde_appsdir}/kdevcvs
%{_kde_appsdir}/kdevquickopen
%{_kde_appsdir}/kdevproblemreporter
%{_kde_appsdir}/kdevcontextbrowser
%{_kde_appsdir}/kdevsourceformatter
%{_kde_appsdir}/kdevappwizard
%{_kde_appsdir}/kdevclassbrowser
%{_kde_appsdir}/kdevdebugger
%{_kde_appsdir}/kdevdocumentswitcher
%{_kde_appsdir}/kdevcodegen
%{_kde_appsdir}/kdevpatchreview
%{_kde_appsdir}/kdevdocumentview
%{_kde_appsdir}/kdevgrepview
%{_kde_appsdir}/kdevsession
%{_kde_appsdir}/kdevsnippet
%{_kde_appsdir}/kdevcodeutils
%{_kde_appsdir}/kdevexternalscript
%{_kde_servicetypes}/kdevelopplugin.desktop
%{_kde_services}/kdevquickopen.desktop
%{_kde_services}/kcm_kdev_uisettings.desktop
%{_kde_services}/kdevfilemanager.desktop
%{_kde_services}/kdevgenericmanager.desktop
%{_kde_services}/kdevkonsoleview.desktop
%{_kde_services}/kdevprojectmanagerview.desktop
%{_kde_services}/kdevsnippet.desktop
%{_kde_services}/kdevstandardoutputview.desktop
%{_kde_services}/kcm_kdev_envsettings.desktop
%{_kde_services}/kcm_kdev_bgsettings.desktop
%{_kde_services}/kcm_kdev_ccsettings.desktop
%{_kde_services}/kcm_kdev_projectsettings.desktop
%{_kde_services}/kdevsubversion.desktop
%{_kde_services}/kdevproblemreporter.desktop
%{_kde_services}/kdevcvs.desktop
%{_kde_services}/kdevexecute.desktop
%{_kde_services}/kcm_kdev_genericprojectmanagersettings.desktop
%{_kde_services}/kcm_kdevsourceformattersettings.desktop
%{_kde_services}/kdevcontextbrowser.desktop
%{_kde_services}/kcm_kdev_pluginsettings.desktop
%{_kde_services}/kdevappwizard.desktop
%{_kde_services}/kdevclassbrowser.desktop
%{_kde_services}/kdevdocumentswitcher.desktop
%{_kde_services}/kdevopenwith.desktop
%{_kde_services}/kdevpatchreview.desktop
%{_kde_services}/kdevdocumentview.desktop
%{_kde_services}/kdevgrepview.desktop
%{_kde_services}/kdevcodeutils.desktop
%{_kde_services}/kdevexternalscript.desktop
%{_kde_services}/kdevgit.desktop
%{_kde_services}/kdevpastebin.desktop
%{_kde_services}/kdevreviewboard.desktop
%{_kde_services}/kdev-dash-projectfileelement.desktop
%{_kde_services}/kdevexecutescript.desktop
%{_kde_services}/kdevprojectdashboard.desktop
%{_kde_services}/kdevvcschangesview.desktop
%{_kde_libdir}/kde4/kdevexecute.so
%{_kde_libdir}/kde4/kcm_kdev_uisettings.so
%{_kde_libdir}/kde4/kdevfilemanager.so
%{_kde_libdir}/kde4/kdevgenericmanager.so
%{_kde_libdir}/kde4/kdevkonsoleview.so
%{_kde_libdir}/kde4/kdevprojectmanagerview.so
%{_kde_libdir}/kde4/kdevsnippet.so
%{_kde_libdir}/kde4/kdevstandardoutputview.so
%{_kde_libdir}/kde4/kcm_kdev_envsettings.so
%{_kde_libdir}/kde4/kdevcvs.so
%{_kde_libdir}/kde4/kdevquickopen.so
%{_kde_libdir}/kde4/kcm_kdev_bgsettings.so
%{_kde_libdir}/kde4/kcm_kdev_ccsettings.so
%{_kde_libdir}/kde4/kcm_kdev_projectsettings.so
%{_kde_libdir}/kde4/kdevproblemreporter.so
%{_kde_libdir}/kde4/kdevsubversion.so
%{_kde_libdir}/kde4/kdevcontextbrowser.so
%{_kde_libdir}/kde4/kcm_kdevsourceformattersettings.so
%{_kde_libdir}/kde4/kcm_kdev_genericprojectmanagersettings.so
%{_kde_libdir}/kde4/kcm_kdev_pluginsettings.so
%{_kde_libdir}/kde4/kdevappwizard.so
%{_kde_libdir}/kde4/kdevclassbrowser.so
%{_kde_libdir}/kde4/kdevdocumentswitcher.so
%{_kde_libdir}/kde4/kdevopenwith.so
%{_kde_libdir}/kde4/kdevpatchreview.so
%{_kde_libdir}/kde4/kdevdocumentview.so
%{_kde_libdir}/kde4/kdevgrepview.so
%{_kde_libdir}/kde4/kdevcodeutils.so
%{_kde_libdir}/kde4/kdevexternalscript.so
%{_kde_libdir}/kde4/kdevgit.so
%{_kde_libdir}/kde4/kdevpastebin.so
%{_kde_libdir}/kde4/kdevreviewboard.so
%{_kde_libdir}/kde4/kdevexecutescript.so
%{_kde_libdir}/kde4/kdevprojectdashboard.so
%{_kde_libdir}/kde4/kdevvcschangesviewplugin.so
%{_kde_libdir}/kde4/plasma_kdev_projectfileelement.so
%{_kde_iconsdir}/hicolor/*/apps/reviewboard.png
%{_kde_iconsdir}/hicolor/22x22/actions/run-clean.png
%{_kde_iconsdir}/hicolor/22x22/actions/run-install.png
%{_kde_iconsdir}/hicolor/*/apps/git.png
%{_kde_iconsdir}/hicolor/*/apps/subversion.png

#-----------------------------------------------------------------------------

%define kdevplatformtests_major 6
%define libkdevplatformtests %mklibname kdevplatformtests %{kdevplatformtests_major}

%package -n %{libkdevplatformtests}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdevplatformtests}
KDE 4 library.

%files -n %{libkdevplatformtests}
%{_kde_libdir}/libkdevplatformtests.so.%{kdevplatformtests_major}*

#-----------------------------------------------------------------------------

%define kdevplatforminterfaces_major 6
%define libkdevplatforminterfaces %mklibname kdevplatforminterfaces %{kdevplatforminterfaces_major}

%package -n %{libkdevplatforminterfaces}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdevplatforminterfaces}
KDE 4 library.

%files -n %{libkdevplatforminterfaces}
%{_kde_libdir}/libkdevplatforminterfaces.so.%{kdevplatforminterfaces_major}*

#-----------------------------------------------------------------------------

%define kdevplatformlanguage_major 6
%define libkdevplatformlanguage %mklibname kdevplatformlanguage %{kdevplatformlanguage_major}

%package -n %{libkdevplatformlanguage}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdevplatformlanguage}
KDE 4 library.

%files -n %{libkdevplatformlanguage}
%{_kde_libdir}/libkdevplatformlanguage.so.%{kdevplatformlanguage_major}*

#-----------------------------------------------------------------------------

%define kdevplatformoutputview_major 6
%define libkdevplatformoutputview %mklibname kdevplatformoutputview %{kdevplatformoutputview_major}

%package -n %{libkdevplatformoutputview}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdevplatformoutputview}
KDE 4 library.

%files -n %{libkdevplatformoutputview}
%{_kde_libdir}/libkdevplatformoutputview.so.%{kdevplatformoutputview_major}*

#-----------------------------------------------------------------------------

%define kdevplatformproject_major 6
%define libkdevplatformproject %mklibname kdevplatformproject %{kdevplatformproject_major}

%package -n %{libkdevplatformproject}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdevplatformproject}
KDE 4 library.

%files -n %{libkdevplatformproject}
%{_kde_libdir}/libkdevplatformproject.so.%{kdevplatformproject_major}*

#-----------------------------------------------------------------------------

%define kdevplatformshell_major 6
%define libkdevplatformshell %mklibname kdevplatformshell %{kdevplatformshell_major}

%package -n %{libkdevplatformshell}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdevplatformshell}
KDE 4 library.

%files -n %{libkdevplatformshell}
%{_kde_libdir}/libkdevplatformshell.so.%{kdevplatformshell_major}*

#-----------------------------------------------------------------------------

%define kdevplatformutil_major 6
%define libkdevplatformutil %mklibname kdevplatformutil %{kdevplatformutil_major}

%package -n %{libkdevplatformutil}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdevplatformutil}
KDE 4 library.

%files -n %{libkdevplatformutil}
%{_kde_libdir}/libkdevplatformutil.so.%{kdevplatformutil_major}*

#-----------------------------------------------------------------------------

%define kdevplatformvcs_major 6
%define libkdevplatformvcs %mklibname kdevplatformvcs %{kdevplatformvcs_major}

%package -n %{libkdevplatformvcs}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdevplatformvcs}
KDE 4 library.

%files -n %{libkdevplatformvcs}
%{_kde_libdir}/libkdevplatformvcs.so.%{kdevplatformvcs_major}*

#-----------------------------------------------------------------------------

%define sublime_major 6
%define libsublime %mklibname sublime %{sublime_major}

%package -n %{libsublime}
Summary:	KDE 4 library
Group: System/Libraries

%description -n %{libsublime}
KDE 4 library.

%files -n %{libsublime}
%{_kde_libdir}/libsublime.so.%{sublime_major}*

#-----------------------------------------------------------------------------

%define kdevplatformdebugger_major 6
%define libkdevplatformdebugger %mklibname kdevplatformdebugger %{kdevplatformdebugger_major}

%package -n %{libkdevplatformdebugger}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdevplatformdebugger}
KDE 4 library.

%files -n %{libkdevplatformdebugger}
%{_kde_libdir}/libkdevplatformdebugger.so.%{kdevplatformdebugger_major}*

#-----------------------------------------------------------------------------

%define kdevplatformdocumentation_major 6
%define libkdevplatformdocumentation %mklibname kdevplatformdocumentation %{kdevplatformdocumentation_major}

%package -n %{libkdevplatformdocumentation}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdevplatformdocumentation}
KDE 4 library.

%files -n %{libkdevplatformdocumentation}
%{_kde_libdir}/libkdevplatformdocumentation.so.%{kdevplatformdocumentation_major}*

#-----------------------------------------------------------------------------

%package -n %{libname}-devel
Summary:	Development files for kdevplatform
Group:		Development/KDE and Qt

Provides:	kdevplatform4-devel = %{EVRD}

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

%description -n %{libname}-devel
Development files for kdevplatform.

%files -n %{libname}-devel
%{_kde_libdir}/cmake/kdevplatform/*.cmake
%{_kde_includedir}/kdevplatform
%{_kde_libdir}/libkdevplatformtests.so
%{_kde_libdir}/libkdevplatforminterfaces.so
%{_kde_libdir}/libkdevplatformlanguage.so
%{_kde_libdir}/libkdevplatformoutputview.so
%{_kde_libdir}/libkdevplatformproject.so
%{_kde_libdir}/libkdevplatformshell.so
%{_kde_libdir}/libkdevplatformutil.so
%{_kde_libdir}/libkdevplatformvcs.so
%{_kde_libdir}/libsublime.so
%{_kde_libdir}/libkdevplatformdebugger.so
%{_kde_libdir}/libkdevplatformdocumentation.so

#-----------------------------------------------------------------------------

%prep
%setup -qn kdevplatform-%{version}

%build
%cmake_kde4
%make

%if %{compile_apidox}
make apidox
%endif

%install
%makeinstall_std -C build

%find_lang %{name} --all-name --with-kde

