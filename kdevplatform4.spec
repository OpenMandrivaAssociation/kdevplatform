%define revision 682496

%define use_enable_final 1
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif

%define lib_name_orig libkdevplatform4
%define lib_major 3
%define lib_name %mklibname kdevplatform4 %lib_major
%define old_lib_major 2
%define old_lib_name %mklibname kdevplatform4 %old_lib_major

Name: 		kdevplatform4
Summary: 	Integrated Development Environment for C++/C
Version: 	3.91
Release: 	%mkrel 0.%revision.1
Epoch: 3
URL: http://www.kde.org 
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdevplatform-%version.%revision.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdevplatform-%version.tar.bz2
%endif
Group: 		Development/C++
BuildRoot:	%_tmppath/%name-%version-%release-root
License: GPL
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
%py_requires -d
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description

%name module needed by Kdevelop or Quanta

%files
%defattr(-,root,root) 
%_kde_appsdir/kdevprojectmanagerview/kdevprojectmanagerview.rc
%_kde_appsdir/kdevstandardoutputview/kdevstandardoutputview.rc
%_kde_appsdir/kdevsubversion/kdevsubversion.rc
%_kde_datadir/kde4/services/kcm_kdev_uisettings.desktop
%_kde_datadir/kde4/services/kdevduchainview.desktop
%_kde_datadir/kde4/services/kdevfilemanager.desktop
%_kde_datadir/kde4/services/kdevgenericmanager.desktop
%_kde_datadir/kde4/services/kdevkonsoleview.desktop
%_kde_datadir/kde4/services/kdevprojectmanagerview.desktop
%_kde_datadir/kde4/services/kdevsnippet.desktop
%_kde_datadir/kde4/services/kdevstandardoutputview.desktop
%_kde_datadir/kde4/services/kdevsubversion.desktop
%_kde_datadir/kde4/servicetypes/kdevelopplugin.desktop
%_kde_libdir/kde4/kcm_kdev_uisettings.so
%_kde_libdir/kde4/kdevduchainview.so
%_kde_libdir/kde4/kdevfilemanager.so
%_kde_libdir/kde4/kdevgenericmanager.so
%_kde_libdir/kde4/kdevkonsoleview.so
%_kde_libdir/kde4/kdevprojectmanagerview.so
%_kde_libdir/kde4/kdevsnippet.so
%_kde_libdir/kde4/kdevstandardoutputview.so
%_kde_libdir/kde4/kdevsubversion.so

#-----------------------------------------------------------------------------

%define libkdevplatformeditor %mklibname kdevplatformeditor 4

%package -n %libkdevplatformeditor
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformeditor
KDE 4 library.

%post -n %libkdevplatformeditor -p /sbin/ldconfig
%postun -n %libkdevplatformeditor -p /sbin/ldconfig

%files -n %libkdevplatformeditor
%defattr(-,root,root)
%_kde_libdir/libkdevplatformeditor.so.*

#-----------------------------------------------------------------------------

%define libkdevplatforminterfaces %mklibname kdevplatforminterfaces 4

%package -n %libkdevplatforminterfaces
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatforminterfaces
KDE 4 library.

%post -n %libkdevplatforminterfaces -p /sbin/ldconfig
%postun -n %libkdevplatforminterfaces -p /sbin/ldconfig

%files -n %libkdevplatforminterfaces
%defattr(-,root,root)
%_kde_libdir/libkdevplatforminterfaces.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformlanguage %mklibname kdevplatformlanguage 4

%package -n %libkdevplatformlanguage
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformlanguage
KDE 4 library.

%post -n %libkdevplatformlanguage -p /sbin/ldconfig
%postun -n %libkdevplatformlanguage -p /sbin/ldconfig

%files -n %libkdevplatformlanguage
%defattr(-,root,root)
%_kde_libdir/libkdevplatformlanguage.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformoutputview %mklibname kdevplatformoutputview 4

%package -n %libkdevplatformoutputview
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformoutputview
KDE 4 library.

%post -n %libkdevplatformoutputview -p /sbin/ldconfig
%postun -n %libkdevplatformoutputview -p /sbin/ldconfig

%files -n %libkdevplatformoutputview
%defattr(-,root,root)
%_kde_libdir/libkdevplatformoutputview.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformproject %mklibname kdevplatformproject 4

%package -n %libkdevplatformproject
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformproject
KDE 4 library.

%post -n %libkdevplatformproject -p /sbin/ldconfig
%postun -n %libkdevplatformproject -p /sbin/ldconfig

%files -n %libkdevplatformproject
%defattr(-,root,root)
%_kde_libdir/libkdevplatformproject.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformshell %mklibname kdevplatformshell 4

%package -n %libkdevplatformshell
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformshell
KDE 4 library.

%post -n %libkdevplatformshell -p /sbin/ldconfig
%postun -n %libkdevplatformshell -p /sbin/ldconfig

%files -n %libkdevplatformshell
%defattr(-,root,root)
%_kde_libdir/libkdevplatformshell.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformutil %mklibname kdevplatformutil 4

%package -n %libkdevplatformutil
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformutil
KDE 4 library.

%post -n %libkdevplatformutil -p /sbin/ldconfig
%postun -n %libkdevplatformutil -p /sbin/ldconfig

%files -n %libkdevplatformutil
%defattr(-,root,root)
%_kde_libdir/libkdevplatformutil.so.*

#-----------------------------------------------------------------------------

%define libkdevplatformvcs %mklibname kdevplatformvcs 4

%package -n %libkdevplatformvcs
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdevplatformvcs
KDE 4 library.

%post -n %libkdevplatformvcs -p /sbin/ldconfig
%postun -n %libkdevplatformvcs -p /sbin/ldconfig

%files -n %libkdevplatformvcs
%defattr(-,root,root)
%_kde_libdir/libkdevplatformvcs.so.*

#-----------------------------------------------------------------------------

%define libsublime %mklibname sublime 4

%package -n %libsublime
Summary: KDE 4 library
Group: System/Libraries

%description -n %libsublime
KDE 4 library.

%post -n %libsublime -p /sbin/ldconfig
%postun -n %libsublime -p /sbin/ldconfig

%files -n %libsublime
%defattr(-,root,root)
%_kde_libdir/libsublime.so.*

#-----------------------------------------------------------------------------

%package -n %lib_name-devel
Summary: Development files for kdevplatform
Group: Development/KDE and Qt

Provides: kdevplatform4-devel = %epoch:%version-%release
Requires: %lib_name = %epoch:%version-%release

%description -n %lib_name-devel
Development files for kdevplatform.

%files -n %lib_name-devel
%defattr(-,root,root)
%_datadir/apps/cmake/modules/FindKDevPlatform.cmake

#------------------------------------------------

%prep
%setup -q -n kdevplatform-%version

%build

cd $RPM_BUILD_DIR/kdevplatform-%version
%cmake_kde4 \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=debug
%endif


%make


%if %compile_apidox
make apidox
%endif

%install
rm -fr %buildroot

cd $RPM_BUILD_DIR/kdevplatform-%version
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot



