%define upstream_name	 POE-Component-Server-HTTP
%define	upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Poe Component to write HTTP server
License:	Artistic and GPL+	
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(POE::API::Peek)
BuildRequires:	perl(LWP)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(HTTP::Status)
BuildRequires:	perl(YAML)
BuildArch:	noarch

%description
POE::Component::Server::HTTP (PoCo::HTTPD) is a framework for building custom 
HTTP servers based on POE. 
It is loosely modeled on the ideas of apache and the mod_perl/Apache module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Seem to fail for now reason
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/POE
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 406181
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.09-4mdv2009.0
+ Revision: 241822
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-2mdv2008.0
+ Revision: 86802
- rebuild


* Mon May 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2007.0
- New release 0.09
- spec cleanup

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-3mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Fri Jan 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-2mdk
- Add buildRequires

* Wed Jan 25 2006 Michael Scherer <misc@mandriva.org> 0.08-1mdk
- First Mandriva package

