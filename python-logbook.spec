#define debug_package %{nil}

%global srcname Logbook
%define	lname	%(echo %{srcname} | tr [:upper:] [:lower:])

Summary:	A logging replacement for Python
Name:		python-%{lname}
Version:	1.5.3
Release:	4
License:	BSD
Group:		Development/Python
Url:		http://logbook.pocoo.org/
#Source0:  https://github.com/getlogbook/logbook/archive/%{version}/%{lname}-%{version}.tar.gz
Source0:	https://pypi.python.org/packages/source/L/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:  python3dist(cython)

%description
Logbook is a logging sytem for Python that replaces the standard
library’s logging module. It was designed with both complex and simple
applications and mind and the idea to make logging fun.

%files
%doc CHANGES
%{python_sitearch}/%{lname}/
%{python_sitearch}/%{srcname}-%{version}-py%{pyver}.egg-info/

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{_bindir}/cython logbook/_speedups.pyx
%py_build

%install
%py_install

