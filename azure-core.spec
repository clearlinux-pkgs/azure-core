#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-core
Version  : 1.5.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/b2/99/6522a2c1fb32a6c06a107abceab07f833884127770cf09b214c08e325dad/azure-core-1.5.0.zip
Source0  : https://files.pythonhosted.org/packages/b2/99/6522a2c1fb32a6c06a107abceab07f833884127770cf09b214c08e325dad/azure-core-1.5.0.zip
Summary  : Microsoft Azure Core Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-core-python = %{version}-%{release}
Requires: azure-core-python3 = %{version}-%{release}
Requires: azure-nspkg
Requires: requests
Requires: six
BuildRequires : azure-nspkg
BuildRequires : buildreq-distutils3
BuildRequires : requests
BuildRequires : six

%description
# Azure Core shared client library for Python
        
        Azure core provides shared exceptions and modules for Python SDK client libraries.

%package python
Summary: python components for the azure-core package.
Group: Default
Requires: azure-core-python3 = %{version}-%{release}

%description python
python components for the azure-core package.


%package python3
Summary: python3 components for the azure-core package.
Group: Default
Requires: python3-core
Provides: pypi(azure_core)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the azure-core package.


%prep
%setup -q -n azure-core-1.5.0
cd %{_builddir}/azure-core-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588700422
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
