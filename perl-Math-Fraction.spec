%include	/usr/lib/rpm/macros.perl
Summary:	Math::Fraction perl module
Summary(pl):	Modu³ perla Math::Fraction
Name:		perl-Math-Fraction
Version:	53b
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/Fraction-v.%{version}.tar.gz
# Source0-md5:	add8995db001a2af6b50d3ff66f4c335
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Fraction allows to manipulate exact fractions.

%description -l pl
Math::Fraction umo¿liwia operacje na u³amkach.

%prep
%setup -q -n Fraction-v.%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_vendorlib}/Math/*.pm
%{_mandir}/man3/*
