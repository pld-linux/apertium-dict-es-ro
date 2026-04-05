Summary:	Spanish-Romanian language pair for Apertium
Summary(pl.UTF-8):	Para języków hiszpański-rumuński dla Apertium
%define	lpair	es-ro
Name:		apertium-dict-%{lpair}
Version:	0.7.5
Release:	1
License:	GPL v3
Group:		Applications/Text
Source0:	https://github.com/apertium/apertium-%{lpair}/archive/v%{version}/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	0da8846bd998e2caaa0a386ed572ce17
URL:		https://www.apertium.org/
BuildRequires:	apertium-devel >= 3.8.1
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	pkgconfig
Requires:	apertium >= 3.8.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between Spanish and Romanian, morphological analysis or part-of-speech
tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między hiszpańskim a rumuńskim, a także analizy morfologicznej lub
oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/ro-es.mode
