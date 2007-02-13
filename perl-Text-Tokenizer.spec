#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Tokenizer
Summary:	Text::Tokenizer - Perl extension for tokenizing text(config) files
Summary(pl.UTF-8):	Text::Tokenizer - rozszerzenie Perla do rozkładania plików tekstowych
Name:		perl-Text-Tokenizer
Version:	0.4.0
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5dba654c94018936892b4f0303928bfb
URL:		http://search.cpan.org/dist/Text-Tokenizer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Tokenizer is very fast lexical analyzer, that can be used to
process input text from file or buffer to basic tokens.

%description -l pl.UTF-8
Text::Tokenizer jest bardzo szybkim analizatorem leksykalnym, który
może być użyty do przetwarzania tokenów z pliku lub bufora.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/Text/*.pm
%dir %{perl_vendorarch}/auto/Text/Tokenizer
%{perl_vendorarch}/auto/Text/Tokenizer/*.bs
%{perl_vendorarch}/auto/Text/Tokenizer/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Tokenizer/*.so
%{_mandir}/man3/*
