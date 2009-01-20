%define module  Module-Load
%define name    perl-%{module}
%define version 0.14
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Runtime require of both modules and files
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
load eliminates the need to know whether you are trying to require either a
file or a module.

If you consult perldoc -f require you will see that require will behave
differently when given a bareword or a string.

In the case of a string, require assumes you are wanting to load a file. But in
the case of a bareword, it assumes you mean a module.

This gives nasty overhead when you are trying to dynamically require modules at
runtime, since you will need to change the module notation (Acme::Comment) to a
file notation fitting the particular platform you are on.

load elimates the need for this overhead and will just DWYM.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Module
%{_mandir}/*/*

