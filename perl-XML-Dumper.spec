%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Dumper
Summary:	XML-Dumper perl module
Summary(pl):	Modu³ perla XML-Dumper
Name:		perl-XML-Dumper
Version:	0.4
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML-Dumper - module for dumping Perl objects from/to XML.

%description -l pl
XML-Dumper - modu³ konwertuj±cy obiekty perla do XML i odwrotnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/XML/Dumper.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
