%include	/usr/lib/rpm/macros.perl
Summary:	Math::Fraction perl module
Summary(pl):	Modu� perla Math::Fraction
Name:		perl-Math-Fraction
Version:	53b
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/Fraction-v.%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Fraction allows to manipulate exact fractions.

%description -l pl
Math::Fraction umo�liwia operacje na u�amkach.

%prep
%setup -q -n Fraction-v.%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_sitelib}/Math/*.pm
%{_mandir}/man3/*
