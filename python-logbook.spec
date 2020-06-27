%define debug_package %{nil}
%define	tarname	logbook

Summary:	A logging replacement for Python

Name:		python-logbook
Version:	1.5.3
Release:	1
Source0:  https://github.com/getlogbook/logbook/archive/%{version}/%{tarname}-%{version}.tar.gz
#Source0:	http://pypi.python.org/packages/source/L/Logbook/Logbook-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://logbook.pocoo.org/

BuildRequires:	python3dist(setuptools)

%description
Logbook is a logging sytem for Python that replaces the standard
library’s logging module. It was designed with both complex and simple
applications and mind and the idea to make logging fun.

%prep
%setup -q -n %{tarname}-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc CHANGES
%{python3_sitelib}/logbook*
