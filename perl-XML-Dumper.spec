%include	/usr/lib/rpm/macros.perl
Summary:	XML-Dumper perl module
Summary(pl):	Modu³ perla XML-Dumper
Name:		perl-XML-Dumper
Version:	0.3
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-Dumper-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-XML-Parser
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
XML-Dumper - module for dumping Perl objects from/to XML.

%description -l pl
XML-Dumper - modu³ konwertuj±cy obiekty perla do XML i odwrotnie.

%prep
%setup -q -n XML-Dumper-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/XML/Dumper
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/XML/Dumper.pm
%{perl_sitearch}/auto/XML/Dumper

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
