%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Dumper
Summary:	XML::Dumper Perl module
Summary(cs):	Modul XML::Dumper pro Perl
Summary(da):	Perlmodul XML::Dumper
Summary(de):	XML::Dumper Perl Modul
Summary(es):	Módulo de Perl XML::Dumper
Summary(fr):	Module Perl XML::Dumper
Summary(it):	Modulo di Perl XML::Dumper
Summary(ja):	XML::Dumper Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	XML::Dumper ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul XML::Dumper
Summary(pl):	Modu³ Perla XML::Dumper
Summary(pt):	Módulo de Perl XML::Dumper
Summary(pt_BR):	Módulo Perl XML::Dumper
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl XML::Dumper
Summary(sv):	XML::Dumper Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl XML::Dumper
Summary(zh_CN):	XML::Dumper Perl Ä£¿é
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
XML::Dumper - Perlový modul umo¾òující dump objektù Perlu z/do XML.

%description -l da
XML::Dumper - Perlmodul for at sende Perlobjekt fra/till XML.

%description -l de
XML::Dumper - Perl-Modul für das Dumping von Perl-Objekten von/zu
XML.

%description -l es
XML::Dumper - Módulo Perl para volcar objetos perl a/desde XML.

%description -l fr
XML::Dumper - Module Perl pour décharger des objets depuis/vers XML.

%description -l it
XML::Dumper - Modulo Perl per eseguire il dumping degli oggetti di
Perl da/a XML.

%description -l ja
XML ¤È¤Î´Ö¤Ç Perl ¥ª¥Ö¥¸¥§¥¯¥È¤ò¥À¥ó¥×¤¹¤ë¤¿¤á¤Î Perl ¥â¥¸¥å¡¼¥ë¡£

%description -l ko
XML::Dumper - XML ·ÎºÎÅÍ/À¸·Î ÆÞ °´Ã¼µéÀ» ¹ö¸®´Âµ¥ ÇÊ¿äÇÑ ÆÞ ¸ðÁÙ.

%description -l pl
XML::Dumper - modu³ konwertuj±cy obiekty Perla do XML i odwrotnie.

%description -l pt
XML::Dumper - Módulo de Perl para traduzir objectos de Perl de e para
XML.

%description -l sv
XML::Dumper - Perlmodul för att skicka Perlobjekt från/till XML.

%description -l zh_CN
XML::Dumper - ÓÃÓÚ×ª´¢µ½ XML »ò´Ó XML ×ª´¢ Perl ¶ÔÏóµÄ Perl Ä£¿é¡£

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
