###############################################################################

%define  debug_package %{nil}

###############################################################################

Summary:         Tool for service discovery, monitoring and configuration
Name:            consul
Version:         0.6.4
Release:         0%{?dist}
Group:           Applications/Internet
License:         MPLv2
URL:             http://www.consul.io

Source0:         https://github.com/hashicorp/%{name}/archive/v%{version}.tar.gz

BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:   golang >= 1.6

Provides:        %{name} = %{version}-%{release}

###############################################################################

%description
Consul is a tool for service discovery and configuration. Consul is 
distributed, highly available, and extremely scalable.

###############################################################################

%prep
%setup -qn %{name}-%{version}

mkdir -p .src/github.com/hashicorp/consul
mv * .src/github.com/hashicorp/consul/
mv .src src

%build
export GOPATH=$(pwd)
export XC_OS=$(go env GOOS)
export XC_ARCH=$(go env GOARCH)
export GO15VENDOREXPERIMENT=1
export CGO_ENABLED=0

pushd src/github.com/hashicorp/consul
  # This is hack for installing dependencies. Build failed on getting
  # git revision. 
  %{__make} %{?_smp_mflags} || :
  $GOPATH/bin/gox -osarch="${XC_OS}/${XC_ARCH}" -output "$GOPATH/%{name}" .
popd

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -pm 755 %{name} %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

###############################################################################

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

###############################################################################

%changelog
* Thu Mar 10 2016 Anton Novojilov <andy@essentialkaos.com> - 0.6.3-0
- Initial build