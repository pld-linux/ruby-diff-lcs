#
# Conditional build:
%bcond_with	tests		# tests [actually not run]

%define pkgname diff-lcs
Summary:	a Ruby port of Algorithm::Diff
Summary(pl.UTF-8):	Port Algorithm::Diff dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.2.5
Release:	4
License:	GPL v2+ or MIT or Artistic
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	7172cb271324fa944d9fbea5fe1f7344
URL:		http://diff-lcs.rubyforge.org/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-rdoc < 5
BuildRequires:	ruby-rdoc >= 4.0
%if %{with tests}
BuildRequires:	ruby-hoe < 4
BuildRequires:	ruby-hoe >= 3.7
BuildRequires:	ruby-hoe-bundler < 2
BuildRequires:	ruby-hoe-bundler >= 1.2
BuildRequires:	ruby-hoe-doofus < 2
BuildRequires:	ruby-hoe-doofus >= 1.0
BuildRequires:	ruby-hoe-gemspec2 < 2
BuildRequires:	ruby-hoe-gemspec2 >= 1.1
BuildRequires:	ruby-hoe-git < 2
BuildRequires:	ruby-hoe-git >= 1.5
BuildRequires:	ruby-hoe-rubygems < 2
BuildRequires:	ruby-hoe-rubygems >= 1.0
BuildRequires:	ruby-hoe-travis < 2
BuildRequires:	ruby-hoe-travis >= 1.2
BuildRequires:	ruby-rake < 11
BuildRequires:	ruby-rake >= 10.0
BuildRequires:	ruby-rspec < 3
BuildRequires:	ruby-rspec >= 2.0
BuildRequires:	ruby-rubyforge >= 2.0.4
%endif
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
Summary:	HTML documentation for Ruby Diff::LCS module
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla modułu języka Ruby Diff::LCS
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for Ruby Diff::LCS module.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla modułu języka Ruby Diff::LCS

%package ri
Summary:	ri documentation for Rubty Diff::LCS module
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla modułu języka Ruby Diff::LCS
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for Rubty Diff::LCS module.

%description ri -l pl.UTF-8
Dokumentacja w formacie ri dla modułu języka Ruby Diff::LCS.

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
# write .gemspec
%__gem_helper spec

rdoc --ri --op ri lib
rdoc --op rdoc lib
%{__rm} -r ri/{Array,String}
%{__rm} ri/created.rid
%{__rm} ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_vendorlibdir},%{ruby_specdir},%{ruby_ridir},%{ruby_rdocdir}}
install -p bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc History.rdoc License.rdoc
%dir %{ruby_vendorlibdir}/diff
%{ruby_vendorlibdir}/diff-lcs.rb
%{ruby_vendorlibdir}/diff/lcs.rb
%{ruby_vendorlibdir}/diff/lcs
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

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
