%include	/usr/lib/rpm/macros.perl
Summary:	Math-Fraction perl module
Summary(pl):	Modu³ perla Math-Fraction
Name:		perl-Math-Fraction
Version:	53b
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Fraction-v.%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Math/Fraction
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,ToDo}.gz

%{perl_sitelib}/Math/*.pm
%{perl_sitearch}/auto/Math/Fraction

%{_mandir}/man3/*
