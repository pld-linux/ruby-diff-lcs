%define pkgname diff-lcs
Summary:	a Ruby port of Algorithm::Diff
Summary(pl.UTF-8):	Port Algorithm::Diff dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.1.2
Release:	3
License:	GPL
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	60524d29b37f76d56ce835323e324879
Patch0:		%{name}-nogems.patch
URL:		http://raa.ruby-lang.org/project/diff-lcs/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Provides:	ruby-Diff-LCS
Obsoletes:	ruby-Diff-LCS
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt
longest common subsequence (LCS) algorithm to compute intelligent
differences between two sequenced enumerable containers. The
implementation is based on Mario I. Wolczko's Smalltalk version (1.2,
1993) and Ned Konz's Perl version (Algorithm::Diff).

%description -l pl.UTF-8
Diff::LCS to port Algorithm::Diff używający algorytmu najdłuższego
wspólnego podciągu (LCS - longest common subsequence) McIlroya-Hunta
do obliczania inteligentnych różnic między dwoma uporządkowanymi
kontenerami. Implementacja jest oparta na wersji dla Smalltalka
autorstwa Mario I. Wolczko (1.2 z roku 1993) i wersji dla Perla
autorstwa Neda Konza (Algorithm::Diff).

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%package -n htmldiff
Summary:	Tool to find differences in HTML files
Summary(pl.UTF-8):	Narzędzie do znajdowania różnic w plikach HTML
Group:		Applications/Text
Requires:	ruby-text-format >= 0.64

%description -n htmldiff
Tool to find differences in HTML files.

%description -n htmldiff -l pl.UTF-8
Narzędzie do znajdowania różnic w plikach HTML.

%package ldiff
Summary:	Ruby Diff tool
Summary(pl.UTF-8):	Narzędzie Ruby Diff
Group:		Applications/Text

%description ldiff
Ruby Diff tool.

%description ldiff -l pl.UTF-8
Narzędzie Ruby Diff.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{Array,String}
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}
install -p bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{ruby_vendorlibdir}/diff
%{ruby_vendorlibdir}/diff/lcs.rb
%{ruby_vendorlibdir}/diff/lcs

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Diff

%files -n htmldiff
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/htmldiff

%files ldiff
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ldiff
