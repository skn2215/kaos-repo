################################################################################

%global __python3 %{_bindir}/python3

%global pythonver %(%{__python3} -c "import sys; print sys.version[:3]" 2>/dev/null || echo 0.0)
%{!?python3_sitearch: %global python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)" 2>/dev/null)}
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()" 2>/dev/null)}

################################################################################

%define package_name      influxdb
%define package_altname   influxdb-python

################################################################################

Summary:        InfluxDB-Python is a client for interacting with InfluxDB
Name:           python34-influxdb
Version:        5.2.0
Release:        0%{?dist}
License:        MIT
Group:          Development/Libraries
URL:            https://github.com/influxdata/influxdb-python

Source:         https://github.com/influxdata/%{package_altname}/archive/v%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildArch:      noarch

BuildRequires:  python34-devel python34-setuptools

Requires:       python34 python34-dateutil pytz python34-requests python34-six

Provides:       %{name} = %{verion}-%{release}

################################################################################

%description
%{name} is a client for interacting with InfluxDB - an open-source distributed
time series database.

################################################################################

%prep
%setup -qn %{package_altname}-%{version}

%build
%{__python3} setup.py build

%install
rm -rf %{buildroot}

%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

################################################################################

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

################################################################################

%changelog
* Wed Sep 12 2018 Anton Novojilov <andy@essentialkaos.com> - 5.2.0-0
- Updated to latest stable release

* Wed Feb 07 2018 Anton Novojilov <andy@essentialkaos.com> - 5.0.0-0
- Updated to latest stable release

* Fri Nov 17 2017 Gleb Goncharov <g.goncharov@fun-box.ru> - 4.4.1-0
- Initial build

