#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Test-Loops
Summary:	x
#Summary(pl):	
Name:		perl-POE-Test-Loops
Version:	0.97
Release:	1
# same as perl 
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e0091f644d52d6dfcf16dc41da56b386
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program and the accompanying POE::Test::Loop::* modules make up POE's
tests for POE::Loop subclasses. These tests are designed to run identically
regardless of the current event loop. POE uses them to test the event loops it
bundles. 
Developers of other POE::Loop modules are encouraged use this package to
generate over 420 comprehensive tests for their own work.

# %description -l pl
# TODO

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
%{_mandir}/man1/poe-gen-tests.1p.gz
#%{_mandir}/man3/*
