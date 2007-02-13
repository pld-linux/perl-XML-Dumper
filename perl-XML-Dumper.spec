#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Dumper
Summary:	XML::Dumper - Perl module for dumping Perl objects from/to XML
Summary(cs.UTF-8):	XML::Dumper - Perlový modul umožňující dump objektů Perlu z/do XML
Summary(pl.UTF-8):	XML::Dumper - moduł Perla konwertujący obiekty Perla do XML-a i odwrotnie
Name:		perl-XML-Dumper
Version:	0.81
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	10726bbe78bef5e4264d5f57533da7c1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-XML-Parser >= 2.16
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Dumper - Perl module for dumping Perl objects from/to XML.

%description -l cs.UTF-8
XML::Dumper - Perlový modul umožňující dump objektů Perlu z/do XML.

%description -l da.UTF-8
XML::Dumper - Perlmodul for at sende Perlobjekt fra/till XML.

%description -l de.UTF-8
XML::Dumper - Perl-Modul für das Dumping von Perl-Objekten von/zu
XML.

%description -l es.UTF-8
XML::Dumper - Módulo Perl para volcar objetos perl a/desde XML.

%description -l fr.UTF-8
XML::Dumper - Module Perl pour décharger des objets depuis/vers XML.

%description -l it.UTF-8
XML::Dumper - Modulo Perl per eseguire il dumping degli oggetti di
Perl da/a XML.

%description -l ja.UTF-8
XML との間で Perl オブジェクトをダンプするための Perl モジュール。

%description -l ko.UTF-8
XML::Dumper - XML 로부터/으로 펄 객체들을 버리는데 필요한 펄 모줄.

%description -l pl.UTF-8
XML::Dumper - moduł konwertujący obiekty Perla do XML-a i odwrotnie.

%description -l pt.UTF-8
XML::Dumper - Módulo de Perl para traduzir objectos de Perl de e para
XML.

%description -l sv.UTF-8
XML::Dumper - Perlmodul för att skicka Perlobjekt från/till XML.

%description -l zh_CN.UTF-8
XML::Dumper - 用于转储到 XML 或从 XML 转储 Perl 对象的 Perl 模块。

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_vendorlib}/XML/Dumper.pm
%{_mandir}/man3/*
