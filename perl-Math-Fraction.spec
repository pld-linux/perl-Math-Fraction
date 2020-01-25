#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
			# fail - module needs an update to modern perl...

%define		pdir	Math
%define		pnam	Fraction
Summary:	Math::Fraction perl module
Summary(pl.UTF-8):	Moduł perla Math::Fraction
Name:		perl-Math-Fraction
Version:	53b
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/Fraction-v.%{version}.tar.gz
# Source0-md5:	add8995db001a2af6b50d3ff66f4c335
URL:		http://search.cpan.org/dist/Math-Fraction/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Fraction allows to manipulate exact fractions.

%description -l pl.UTF-8
Math::Fraction umożliwia operacje na ułamkach.

%prep
%setup -q -n Fraction-v.%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_vendorlib}/Math/*.pm
%{_mandir}/man3/*
