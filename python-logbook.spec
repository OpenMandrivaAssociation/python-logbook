%define	tarname	Logbook
%define name	python-logbook
%define version	0.4
%define rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define release %{rel}
%endif

Summary:	A logging replacement for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/L/%{tarname}/%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://logbook.pocoo.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-setuptools

%description
Logbook is a logging sytem for Python that replaces the standard
library’s logging module. It was designed with both complex and simple
applications and mind and the idea to make logging fun.

%prep
%setup -q -n %{tarname}-%{version}

%build
make cybuild
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%py_platsitedir/Logbook*
%py_platsitedir/logbook*
