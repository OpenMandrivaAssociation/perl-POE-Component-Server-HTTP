%define upstream_name	 POE-Component-Server-HTTP
%define	upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:   	Poe Component to write HTTP server
License:   	Artistic and GPL+	
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(POE::API::Peek)
BuildRequires:  perl(YAML)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
POE::Component::Server::HTTP (PoCo::HTTPD) is a framework for building custom 
HTTP servers based on POE. 
It is loosely modeled on the ideas of apache and the mod_perl/Apache module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
