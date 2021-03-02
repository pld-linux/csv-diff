Summary:	Python CLI tool and library for diffing CSV files
Name:		csv-diff
Version:	1.1
Release:	3
License:	Apache v2.0
Group:		Applications
#Source0Download: https://pypi.org/simple/csv-diff/
Source0:	https://files.pythonhosted.org/packages/source/c/csv-diff/%{name}-%{version}.tar.gz
# Source0-md5:	2c9cf505b45db4cb3c586c84cfef6f2e
URL:		https://github.com/simonw/csv-diff
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pytest-runner
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for viewing the difference between two CSV files.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/csv-diff
%{py3_sitescriptdir}/csv_diff
%{py3_sitescriptdir}/csv_diff-%{version}-py*.egg-info
