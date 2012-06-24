%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Dumper
Summary:	XML::Dumper Perl module
Summary(cs):	Modul XML::Dumper pro Perl
Summary(da):	Perlmodul XML::Dumper
Summary(de):	XML::Dumper Perl Modul
Summary(es):	M�dulo de Perl XML::Dumper
Summary(fr):	Module Perl XML::Dumper
Summary(it):	Modulo di Perl XML::Dumper
Summary(ja):	XML::Dumper Perl �⥸�塼��
Summary(ko):	XML::Dumper �� ����
Summary(no):	Perlmodul XML::Dumper
Summary(pl):	Modu� Perla XML::Dumper
Summary(pt):	M�dulo de Perl XML::Dumper
Summary(pt_BR):	M�dulo Perl XML::Dumper
Summary(ru):	������ ��� Perl XML::Dumper
Summary(sv):	XML::Dumper Perlmodul
Summary(uk):	������ ��� Perl XML::Dumper
Summary(zh_CN):	XML::Dumper Perl ģ��
Name:		perl-XML-Dumper
Version:	0.4
Release:	9
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-XML-Parser >= 2.16
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
XML::Dumper - modu� konwertuj�cy obiekty Perla do XML i odwrotnie.

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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Dumper.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/[Rmn]*
