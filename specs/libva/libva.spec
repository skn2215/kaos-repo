################################################################################

%define _posixroot        /
%define _root             /root
%define _opt              /opt
%define _bin              /bin
%define _sbin             /sbin
%define _srv              /srv
%define _home             /home
%define _lib32            %{_posixroot}lib
%define _lib64            %{_posixroot}lib64
%define _libdir32         %{_prefix}%{_lib32}
%define _libdir64         %{_prefix}%{_lib64}
%define _logdir           %{_localstatedir}/log
%define _rundir           %{_localstatedir}/run
%define _lockdir          %{_localstatedir}/lock/subsys
%define _cachedir         %{_localstatedir}/cache
%define _spooldir         %{_localstatedir}/spool
%define _crondir          %{_sysconfdir}/cron.d
%define _loc_prefix       %{_prefix}/local
%define _loc_exec_prefix  %{_loc_prefix}
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_libdir       %{_loc_exec_prefix}/%{_lib}
%define _loc_libdir32     %{_loc_exec_prefix}/%{_lib32}
%define _loc_libdir64     %{_loc_exec_prefix}/%{_lib64}
%define _loc_libexecdir   %{_loc_exec_prefix}/libexec
%define _loc_sbindir      %{_loc_exec_prefix}/sbin
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_datarootdir  %{_loc_prefix}/share
%define _loc_includedir   %{_loc_prefix}/include
%define _rpmstatedir      %{_sharedstatedir}/rpm-state
%define _pkgconfigdir     %{_libdir}/pkgconfig

%define __ldconfig        %{_sbin}/ldconfig

################################################################################

Summary:            Video Acceleration (VA) API for Linux
Name:               libva
Version:            1.8.3
Release:            1%{?dist}
Group:              System Environment/Libraries
License:            MIT
URL:                https://github.com/01org/libva

Source0:            https://github.com/01org/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:      gcc gcc-c++ make libtool libudev-devel
BuildRequires:      libdrm-devel >= 2.4.23 libpciaccess-devel mesa-libGL-devel
BuildRequires:      libXext-devel libXfixes-devel

Conflicts:          libdrm < 2.4.23

Provides:           libva-utils = %{version}-%{release}
Provides:           libva-freeworld = %{version}-%{release}

Obsoletes:          libva-utils < %{version}-%{release}
Obsoletes:          libva-freeworld < %{version}-%{release}

Provides:           %{name} = %{version}-%{release}

################################################################################

%description
Libva is open source library to provide hardware accelerated video
encoding and decoding. It supported by GStreamer, VLC media player, Mpv and
MPlayer.

################################################################################

%package devel
Summary:            Libraries and headers for (VA) API
Group:              Development/Libraries

Requires:           %{name} = %{version}-%{release}

%description devel
Libva headers and libraries which provides the VA API video acceleration API.

################################################################################

%prep
%setup -q

%build
libtoolize -f
autoreconf -fi

%configure --disable-static --enable-glx

%{__make} %{?_smp_mflags}

%install
rm -rf %{buildroot}

%{make_install}

%clean
rm -rf %{buildroot}

################################################################################

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

################################################################################

%files
%defattr(-,root,root,-)
%doc COPYING NEWS
%{_libdir}/%{name}*.so*
%{_pkgconfigdir}/%{name}*.pc

%files devel
%defattr(-,root,root,-)
%{_includedir}/va/*.h
%{_libdir}/%{name}*.so
%{_libdir}/%{name}*.la

################################################################################

%changelog
* Fri Sep 22 2017 Anton Novojilov <andy@essentialkaos.com> - 1.8.3-1
- Minor spec improvement

* Sat Sep 16 2017 Anton Novojilov <andy@essentialkaos.com> - 1.8.3-0
- Updated to latest version

* Fri Apr 15 2016 Gleb Goncharov <yum@gongled.ru> - 1.7.0-0
- Updated to latest version
- Bump VA API version to 0.39
- Add support for VP9 10bit decode API
- Allow libva to load the vaapi driver provided by Mesa Gallium for nouveau
  and radeon
- Fix libva-glx against OpenGL 3.1 or above
