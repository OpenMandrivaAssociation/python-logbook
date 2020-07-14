%define debug_package %{nil}
%define	tarname	logbook

Summary:	A logging replacement for Python

Name:		python-logbook
Version:	1.5.3
Release:	3
#Source0:  https://github.com/getlogbook/logbook/archive/%{version}/%{tarname}-%{version}.tar.gz
Source0:	http://pypi.python.org/packages/source/L/Logbook/Logbook-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://logbook.pocoo.org/

BuildRequires:  pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:  python3dist(cython)

%description
Logbook is a logging sytem for Python that replaces the standard
library’s logging module. It was designed with both complex and simple
applications and mind and the idea to make logging fun.

%prep
%setup -q -n Logbook-%{version}

%build
%{_bindir}/cython logbook/_speedups.pyx
%py_build

%install
%py_install

%files
%doc CHANGES
%{python3_sitelib}/logbook*
