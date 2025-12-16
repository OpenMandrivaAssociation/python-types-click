%define module types-click
%define oname types_click

Name:		python-types-click
Version:	7.1.8
Release:	2
Summary:	Typing stubs for click
URL:		https://pypi.org/project/types-click/
License:	Apache-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/t/types-click/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Typing stubs for click.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/click-stubs
%{python_sitelib}/%{oname}-%{version}*.egg-info
