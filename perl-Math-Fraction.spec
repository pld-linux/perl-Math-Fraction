%include	/usr/lib/rpm/macros.perl
Summary:	Math-Fraction perl module
Summary(pl):	Modu³ perla Math-Fraction
Name:		perl-Math-Fraction
Version:	53b
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Math/Fraction-v.%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-Fraction allows to manipulate exact fractions.

%description -l pl
Math-Fraction umo¿liwia operacje na u³amkach.

%prep
%setup -q -n Fraction-v.%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Math/*.pm
%{_mandir}/man3/*
