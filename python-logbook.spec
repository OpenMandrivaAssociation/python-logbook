%undefine _debugsource_template
%define module logbook
%define oname logbook

Name:		python-logbook
Summary:	A logging replacement for Python
Version:	1.9.2
Release:	1
License:	BSD
Group:		Development/Python
URL:		https://github.com/getlogbook/logbook
Source0:	https://github.com/getlogbook/logbook/archive/%{version}/%{oname}-%{version}.tar.gz
Source1:	logbook-%{version}-vendor.tar.xz

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-rust)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	cargo
BuildRequires:	rust-packaging

%description
Logbook is a logging sytem for Python that replaces the standard
library’s logging module. It was designed with both complex and simple
applications and mind and the idea to make logging fun.

Documentation: https://logbook.readthedocs.io/

%prep
%autosetup -n %{module}-%{version} -p1 -a1
# Remove bundled egg-info
rm -rf Logbook.egg-info
# prpe the vendored crates
%cargo_prep -v vendor

cat >>.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%files
%{python_sitearch}/%{module}/
%{python_sitearch}/%{module}-%{version}.dist-info/
