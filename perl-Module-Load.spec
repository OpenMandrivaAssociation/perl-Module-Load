%define upstream_name    Module-Load%define upstream_version 0.32
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Runtime require of both modules and files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Module
%{_mandir}/*/*


%changelog
* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.220.0-1
+ Revision: 759445
- version update 0.22

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-4mdv2011.0
+ Revision: 597191
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-3mdv2011.0
+ Revision: 562431
- rebuild

* Sat Jul 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-2mdv2011.0
+ Revision: 558166
- rebuild

* Wed Mar 03 2010 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.1
+ Revision: 513796
- update to 0.18

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 403865
- rebuild using %%perl_convert_version

* Mon Feb 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2009.1
+ Revision: 338737
- update to new version 0.16

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.1
+ Revision: 331586
- update to new version 0.14

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.12-4mdv2009.0
+ Revision: 257895
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.12-3mdv2009.0
+ Revision: 245942
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2008.1
+ Revision: 97515
- update to new version 0.12

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-3mdv2008.0
+ Revision: 86641
- rebuild




