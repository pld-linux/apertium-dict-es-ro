Summary:	Spanish-Romanian language pair for Apertium
Summary(pl.UTF-8):	Para języków hiszpański-rumuński dla Apertium
%define	lpair	es-ro
Name:		apertium-dict-%{lpair}
Version:	0.7.1
Release:	1
License:	GPL v3
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	9de6e21ddf8dfb65a6b09b430e8ab600
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-apertium32.patch
Patch2:		%{name}-fix.patch
Patch3:		%{name}-install.patch
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox >= 3.2.0
BuildRequires:	pkgconfig
Requires:	apertium >= 3.2.0
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apertium/modes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed here (see modes subdir) and contain wrong (builddir) paths
%{__rm} $RPM_BUILD_ROOT%{_datadir}/apertium/apertium-%{lpair}/*.mode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/ro-es.mode
