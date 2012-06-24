#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Dumper
Summary:	XML::Dumper - Perl module for dumping Perl objects from/to XML
Summary(pl):	XML::Dumper - Perlov� modul umo��uj�c� dump objekt� Perlu z/do XML
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

%description -l cs
XML::Dumper - Perlov� modul umo��uj�c� dump objekt� Perlu z/do XML.

%description -l da
XML::Dumper - Perlmodul for at sende Perlobjekt fra/till XML.

%description -l de
XML::Dumper - Perl-Modul f�r das Dumping von Perl-Objekten von/zu
XML.

%description -l es
XML::Dumper - M�dulo Perl para volcar objetos perl a/desde XML.

%description -l fr
XML::Dumper - Module Perl pour d�charger des objets depuis/vers XML.

%description -l it
XML::Dumper - Modulo Perl per eseguire il dumping degli oggetti di
Perl da/a XML.

%description -l ja
XML �Ȥδ֤� Perl ���֥������Ȥ����פ��뤿��� Perl �⥸�塼�롣

%description -l ko
XML::Dumper - XML �κ���/���� �� ��ü���� �����µ� �ʿ��� �� ����.

%description -l pl
XML::Dumper - modu� konwertuj�cy obiekty Perla do XML-a i odwrotnie.

%description -l pt
XML::Dumper - M�dulo de Perl para traduzir objectos de Perl de e para
XML.

%description -l sv
XML::Dumper - Perlmodul f�r att skicka Perlobjekt fr�n/till XML.

%description -l zh_CN
XML::Dumper - ����ת���� XML ��� XML ת�� Perl ����� Perl ģ�顣

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
