################################################################################

%global __python3 %{_bindir}/python3

%global pythonver %(%{__python3} -c "import sys; print sys.version[:3]" 2>/dev/null || echo 0.0)
%{!?python3_sitearch: %global python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)" 2>/dev/null)}
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()" 2>/dev/null)}

################################################################################

%define package_name      jinja2

# Fix for https://github.com/pallets/jinja/issues/653
%global _python_bytecompile_errors_terminate_build 0

################################################################################

Summary:        Sandboxed template engine
Name:           python34-jinja2
Version:        2.10
Release:        0%{?dist}
License:        BSD
Group:          Development/Libraries
URL:            http://jinja.pocoo.org

Source:         https://github.com/mitsuhiko/%{package_name}/archive/%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildArch:      noarch

BuildRequires:  python34-devel python34-setuptools

Requires:       python34

Provides:       %{name} = %{verion}-%{release}

################################################################################

%description
Jinja is a sandboxed template engine written in pure Python. It
provides a Django-like non-XML syntax and compiles templates into
executable python code. It's basically a combination of Django
templates and python code.

################################################################################

%prep
%setup -qn jinja-%{version}

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
* Fri Nov 17 2017 Anton Novojilov <andy@essentialkaos.com> - 2.10-0
- Updated to latest stable release

* Mon Jul 10 2017 Anton Novojilov <andy@essentialkaos.com> - 2.9.6-0
- Updated to latest stable release

* Wed Mar 22 2017 Anton Novojilov <andy@essentialkaos.com> - 2.9.5-0
- Updated to latest stable release

* Wed Aug 12 2015 Anton Novojilov <andy@essentialkaos.com> - 2.8-0
- Initial build
