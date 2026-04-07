#
# Conditional build:
%bcond_with	tests	# unit tests (4 failures with python 3.13 as of 1.1)

Summary:	Tool to measure, monitor and analyse the memory behaviour of Python 2 objects
Summary(pl.UTF-8):	Narzędzie do pomiaru, monitorowania i analizy zachowania pamięciowego obiektów Pythona 2
Name:		python3-pympler
Version:	1.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pympler/
Source0:	https://files.pythonhosted.org/packages/source/P/Pympler/pympler-%{version}.tar.gz
# Source0-md5:	de698a9a3f2b968b4da9d71bc5eebb0d
URL:		https://pypi.org/project/Pympler/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pympler is a development tool to measure, monitor and analyse the
memory behaviour of Python objects in a running Python application.

%description -l pl.UTF-8
Pympler to narzędzie programistyczne do pomiaru, monitorowania i
analizy zachowania pamięciowego obiektów Pythona w działającej
aplikacji.

%prep
%setup -q -n pympler-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} test/runtest.py -pre-install -verbose 3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE README.md
%{py3_sitescriptdir}/pympler
%{py3_sitescriptdir}/Pympler-%{version}-py*.egg-info
