%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%if %unstable
%define dont_strip 1
%endif

%define lib_name_orig libkdevplatform4
%define lib_major 4
%define lib_name %mklibname kdevplatform %lib_major
%define old_lib_major 2
%define old_lib_name %mklibname kdevplatform4 %old_lib_major

Name: 		kdevplatform4
Summary: 	Integrated Development Environment for C++/C
Version:    0.9.84
Epoch:      4
URL:        http://www.kde.org 
Release:    %mkrel 2
Source:     ftp://ftp.kde.org/pub/kde/stable/%version/src/kdevplatform-%version.tar.bz2
Patch0:		kdevplatform-0.9.84-force-compile-teamwork.patch
Group: 		Development/C++
BuildRoot:	%_tmppath/%name-%version-%release-root
License:    GPL
BuildRequires: kdelibs4-devel 
BuildRequires: flex
BuildRequires: graphviz
BuildRequires: db-devel
BuildRequires: subversion-devel
BuildRequires: apr-devel
BuildRequires: apr-util-devel
%if %compile_apidox
BuildRequires: doxygen
%endif
BuildRequires:    libcommoncpp-devel
BuildRequires:    rapidsvn
BuildRequires:    boost-devel
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes:        kdevelop4 < 3.93
Conflicts:	%lib_name-devel < 4:0.9.83-0.886617.3

%description
%name module needed by Kdevelop or Quanta

%files
%defattr(-,root,root) 
%{_kde_bindir}/kdevteamwork_server
%_kde_appsdir/kdevprojectmanagerview
%_kde_appsdir/kdevstandardoutputview
%_kde_appsdir/kdevduchainview
%_kde_appsdir/kdevfilemanager
%_kde_appsdir/kdevcvs
%_kde_appsdir/kdevquickopen
%_kde_appsdir/kdevproblemreporter
%_kde_appsdir/kdevteamwork
%_kde_appsdir/kdevgit
%_kde_appsdir/kdevbzr
%_kde_appsdir/kdevcontextbrowser
%_kde_appsdir/kdevhg
%_kde_appsdir/kdevsourceformatter
%_kde_datadir/kde4/services/kdevquickopen.desktop
%_kde_datadir/kde4/services/kcm_kdev_uisettings.desktop
%_kde_datadir/kde4/services/kdevduchainview.desktop
%_kde_datadir/kde4/services/kdevfilemanager.desktop
%_kde_datadir/kde4/services/kdevgenericmanager.desktop
%_kde_datadir/kde4/services/kdevkonsoleview.desktop
%_kde_datadir/kde4/services/kdevprojectmanagerview.desktop
%_kde_datadir/kde4/services/kdevsnippet.desktop
%_kde_datadir/kde4/services/kdevstandardoutputview.desktop
%_kde_datadir/kde4/servicetypes/kdevelopplugin.desktop
%_kde_datadir/kde4/services/kcm_kdev_envsettings.desktop
%_kde_datadir/kde4/services/kcm_kdev_bgsettings.desktop
%_kde_datadir/kde4/services/kcm_kdev_ccsettings.desktop
%_kde_datadir/kde4/services/kcm_kdev_projectsettings.desktop
%_kde_datadir/kde4/services/kdevsubversion.desktop
%_kde_datadir/kde4/services/kdevproblemreporter.desktop
%_kde_datadir/kde4/services/kdevcvs.desktop
%_kde_datadir/kde4/services/kcm_kdev_runsettings.desktop
%_kde_datadir/kde4/services/kdevexecute.desktop
%_kde_datadir/kde4/services/kdevteamwork.desktop
%_kde_datadir/kde4/services/kcm_kdev_genericprojectmanagersettings.desktop
%_kde_datadir/kde4/services/kcm_kdevsourceformattersettings.desktop
%_kde_datadir/kde4/services/kdevbzr.desktop
%_kde_datadir/kde4/services/kdevcontextbrowser.desktop
%_kde_datadir/kde4/services/kdevgit.desktop
%_kde_datadir/kde4/services/kdevhg.desktop
%_kde_datadir/kde4/services/kdevkrossplugin.desktop
%_kde_datadir/kde4/services/kdevsourceformatter.desktop
%_kde_datadir/kde4/services/kdevvcscommon.desktop
%_kde_datadir/kde4/services/kcm_kdev_pluginsettings.desktop
%_kde_libdir/kde4/kcm_kdev_runsettings.so
%_kde_libdir/kde4/kdevexecute.so
%_kde_libdir/kde4/kcm_kdev_uisettings.so
%_kde_libdir/kde4/kdevduchainview.so
%_kde_libdir/kde4/kdevfilemanager.so
%_kde_libdir/kde4/kdevgenericmanager.so
%_kde_libdir/kde4/kdevkonsoleview.so
%_kde_libdir/kde4/kdevprojectmanagerview.so
%_kde_libdir/kde4/kdevsnippet.so
%_kde_libdir/kde4/kdevstandardoutputview.so
%_kde_libdir/kde4/kcm_kdev_envsettings.so
%_kde_libdir/kde4/kdevcvs.so
%_kde_libdir/kde4/kdevquickopen.so
%_kde_libdir/kde4/kcm_kdev_bgsettings.so
%_kde_libdir/kde4/kcm_kdev_ccsettings.so
%_kde_libdir/kde4/kcm_kdev_projectsettings.so
%_kde_libdir/kde4/kdevproblemreporter.so
%_kde_libdir/kde4/kdevsubversion.so
%_kde_libdir/kde4/kdevteamwork.so
%_kde_libdir/kde4/kdevbzr.so
%_kde_libdir/kde4/kdevcontextbrowser.so
%_kde_libdir/kde4/kdevgit.so
%_kde_libdir/kde4/kdevhg.so
%_kde_libdir/kde4/kdevkrossplugin.so
%_kde_libdir/kde4/kdevsourceformatter.so
%_kde_libdir/kde4/kdevvcscommon.so
%_kde_libdir/kde4/kcm_kdevsourceformattersettings.so
%_kde_libdir/kde4/kcm_kdev_genericprojectmanagersettings.so
%_kde_libdir/kde4/kcm_kdev_pluginsettings.so
%_kde_libdir/libkdevteamwork_diff2.so
%_kde_libdir/libkdevteamwork_dynamictext.so
%_kde_libdir/libkdevteamwork_network.so
%_kde_iconsdir/hicolor/22x22/actions/run-clean.png
%_kde_iconsdir/hicolor/22x22/actions/run-install.png

#-----------------------------------------------------------------------------

%define kdevplatformtestshell_major 1
%define libkdevplatformtestshell %mklibname kdevplatformtestshell %kdevplatformtestshell_major

%package -n %libkdevplatformtestshell
Summary: KDE 4 library
Group: System/Libraries
Obsoletes:   %{_lib}kdevplatformtestshell4 < 3:4.0.69-1

%description -n %libkdevplatformtestshell
KDE 4 library.

%if %mdkversion < 200900
%post -n %libkdevplatformtestshell -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdevplatformtestshell -p /sbin/ldconfig
%endif

%files -n %libkdevplatformtestshell
%defattr(-,root,root)
%_kde_libdir/libkdevplatformtestshell.so.%{kdevplatformtestshell_major}*

#-----------------------------------------------------------------------------

%define kdevplatforminterfaces_major 1
%define libkdevplatforminterfaces %mklibname kdevplatforminterfaces %kdevplatforminterfaces_major

%package -n %libkdevplatforminterfaces
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatforminterfaces
KDE 4 library.

%if %mdkversion < 200900
%post -n %libkdevplatforminterfaces -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdevplatforminterfaces -p /sbin/ldconfig
%endif

%files -n %libkdevplatforminterfaces
%defattr(-,root,root)
%_kde_libdir/libkdevplatforminterfaces.so.%{kdevplatforminterfaces_major}*

#-----------------------------------------------------------------------------

%define kdevplatformlanguage_major 1
%define libkdevplatformlanguage %mklibname kdevplatformlanguage %kdevplatformlanguage_major

%package -n %libkdevplatformlanguage
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformlanguage
KDE 4 library.

%if %mdkversion < 200900
%post -n %libkdevplatformlanguage -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdevplatformlanguage -p /sbin/ldconfig
%endif

%files -n %libkdevplatformlanguage
%defattr(-,root,root)
%_kde_libdir/libkdevplatformlanguage.so.%{kdevplatformlanguage_major}*

#-----------------------------------------------------------------------------

%define kdevplatformoutputview_major 1
%define libkdevplatformoutputview %mklibname kdevplatformoutputview %kdevplatformoutputview_major

%package -n %libkdevplatformoutputview
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformoutputview
KDE 4 library.

%if %mdkversion < 200900
%post -n %libkdevplatformoutputview -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdevplatformoutputview -p /sbin/ldconfig
%endif

%files -n %libkdevplatformoutputview
%defattr(-,root,root)
%_kde_libdir/libkdevplatformoutputview.so.%{kdevplatformoutputview_major}*

#-----------------------------------------------------------------------------

%define kdevplatformproject_major 1
%define libkdevplatformproject %mklibname kdevplatformproject %kdevplatformproject_major

%package -n %libkdevplatformproject
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformproject
KDE 4 library.

%if %mdkversion < 200900
%post -n %libkdevplatformproject -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdevplatformproject -p /sbin/ldconfig
%endif

%files -n %libkdevplatformproject
%defattr(-,root,root)
%_kde_libdir/libkdevplatformproject.so.%{kdevplatformproject_major}*

#-----------------------------------------------------------------------------

%define kdevplatformshell_major 1
%define libkdevplatformshell %mklibname kdevplatformshell %kdevplatformshell_major

%package -n %libkdevplatformshell
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformshell
KDE 4 library.

%if %mdkversion < 200900
%post -n %libkdevplatformshell -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdevplatformshell -p /sbin/ldconfig
%endif

%files -n %libkdevplatformshell
%defattr(-,root,root)
%_kde_libdir/libkdevplatformshell.so.%{kdevplatformshell_major}*

#-----------------------------------------------------------------------------

%define kdevplatformutil_major 1
%define libkdevplatformutil %mklibname kdevplatformutil %kdevplatformutil_major

%package -n %libkdevplatformutil
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformutil
KDE 4 library.

%if %mdkversion < 200900
%post -n %libkdevplatformutil -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdevplatformutil -p /sbin/ldconfig
%endif

%files -n %libkdevplatformutil
%defattr(-,root,root)
%_kde_libdir/libkdevplatformutil.so.%{kdevplatformutil_major}*

#-----------------------------------------------------------------------------

%define kdevplatformvcs_major 1
%define libkdevplatformvcs %mklibname kdevplatformvcs %kdevplatformvcs_major

%package -n %libkdevplatformvcs
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformvcs
KDE 4 library.

%if %mdkversion < 200900
%post -n %libkdevplatformvcs -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdevplatformvcs -p /sbin/ldconfig
%endif

%files -n %libkdevplatformvcs
%defattr(-,root,root)
%_kde_libdir/libkdevplatformvcs.so.%{kdevplatformvcs_major}*

#-----------------------------------------------------------------------------

%define kdevplatformveritas_major 1
%define libkdevplatformveritas %mklibname kdevplatformveritas %kdevplatformveritas_major

%package -n %libkdevplatformveritas
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformveritas
KDE 4 library.

%if %mdkversion < 200900
%post -n %libkdevplatformveritas -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdevplatformveritas -p /sbin/ldconfig
%endif

%files -n %libkdevplatformveritas
%defattr(-,root,root)
%_kde_libdir/libkdevplatformveritas.so.%{kdevplatformveritas_major}*

#-----------------------------------------------------------------------------

%define sublime_major 1
%define libsublime %mklibname sublime %sublime_major

%package -n %libsublime
Summary: KDE 4 library
Group: System/Libraries

%description -n %libsublime
KDE 4 library.

%if %mdkversion < 200900
%post -n %libsublime -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libsublime -p /sbin/ldconfig
%endif

%files -n %libsublime
%defattr(-,root,root)
%_kde_libdir/libsublime.so.%{sublime_major}*

#-----------------------------------------------------------------------------

%package -n %lib_name-devel
Summary: Development files for kdevplatform
Group: Development/KDE and Qt

Provides:  kdevplatform4-devel = %epoch:%version-%release
Obsoletes: %{_lib}kdevplatform43-devel < 4.0.73-1
Conflicts: kdevplatfom4 < 4:0.9.83-0.886617.4

Requires: %libkdevplatformtestshell = %epoch:%version-%release
Requires: %libkdevplatforminterfaces = %epoch:%version-%release
Requires: %libkdevplatformlanguage = %epoch:%version-%release
Requires: %libkdevplatformoutputview = %epoch:%version-%release
Requires: %libkdevplatformproject = %epoch:%version-%release
Requires: %libkdevplatformshell = %epoch:%version-%release
Requires: %libkdevplatformutil = %epoch:%version-%release
Requires: %libkdevplatformvcs = %epoch:%version-%release
Requires: %libkdevplatformveritas = %epoch:%version-%release
Requires: %libsublime = %epoch:%version-%release

%description -n %lib_name-devel
Development files for kdevplatform.

%files -n %lib_name-devel
%defattr(-,root,root)
%_kde_appsdir/cmake/modules/FindKDevPlatform.cmake
%{_kde_libdir}/kdevplatform/KDevPlatformConfig.cmake
%{_kde_libdir}/kdevplatform/KDevPlatformConfigVersion.cmake
%_kde_includedir/kdevplatform
%{_kde_libdir}/libkdevplatformtestshell.so
%{_kde_libdir}/libkdevplatforminterfaces.so
%{_kde_libdir}/libkdevplatformlanguage.so
%{_kde_libdir}/libkdevplatformoutputview.so
%{_kde_libdir}/libkdevplatformproject.so
%{_kde_libdir}/libkdevplatformshell.so
%{_kde_libdir}/libkdevplatformutil.so
%{_kde_libdir}/libkdevplatformvcs.so
%{_kde_libdir}/libkdevplatformveritas.so
%{_kde_libdir}/libsublime.so

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdevplatform-%version
%patch0 -p0

%build
%cmake_kde4
%make

%if %compile_apidox
make apidox
%endif

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
rm -fr %buildroot

