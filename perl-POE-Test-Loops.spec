#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Test-Loops
Summary:	POE::Test::Loops - reusable tests for POE::Loop authors
Summary(pl.UTF-8):	POE::Test::Loops - testy do wykorzystywania przez autorów POE::Loop
Name:		perl-POE-Test-Loops
Version:	0.97
Release:	1
# same as perl 
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e0091f644d52d6dfcf16dc41da56b386
URL:		http://search.cpan.org/dist/POE-Test-Loops/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
poe-gen-tests program and the accompanying POE::Test::Loop::* modules
make up POE's tests for POE::Loop subclasses. These tests are designed
to run identically regardless of the current event loop. POE uses them
to test the event loops it bundles. 

Developers of other POE::Loop modules are encouraged to use this
package to generate over 420 comprehensive tests for their own work.

%description -l pl.UTF-8
Program poe-gen-tests wraz z towarzyszącymi modułami
POE::Test::Loop::* tworzą testy POE dla podklas POE::Loop. Testy te są
projektowane z myślą o identycznym działaniu niezależnie od aktualnej
pętli zdarzeń. POE wykorzystuje je do testowania dołączonych pętli
zdarzeń.

Zachęca się twórców innych modułów POE::Loop do używania tego pakietu
do generowania ponad 420 wyczerpujących testów dla swojego
oprogramowania.

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
%doc CHANGES README
%{perl_vendorlib}/POE/Test/*.pm
%{perl_vendorlib}/POE/Test/Loops
%attr(755,root,root) %{_bindir}/poe-gen-tests
%{_mandir}/man1/poe-gen-tests.1p*
#%{_mandir}/man3/*
