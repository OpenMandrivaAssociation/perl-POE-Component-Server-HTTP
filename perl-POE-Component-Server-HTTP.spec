%define module	POE-Component-Server-HTTP
%define	name	perl-%{module}
%define	version	0.09
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:    	%{release}
License:   	Artistic and GPL	
Group:		Development/Perl
Summary:   	Poe Component to write HTTP server
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/POE/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(POE::API::Peek)
BuildRequires:  perl(YAML)
BuildArch:	noarch

%description
POE::Component::Server::HTTP (PoCo::HTTPD) is a framework for building custom 
HTTP servers based on POE. 
It is loosely modeled on the ideas of apache and the mod_perl/Apache module.

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
%doc Changes README
%{perl_vendorlib}/POE
%{_mandir}/man3/*

