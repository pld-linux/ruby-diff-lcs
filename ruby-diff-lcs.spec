%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define ruby_ridir      %(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')

Summary:	a Ruby port of Algorithm::Diff
Name:		ruby-Diff-LCS
Version:	1.1.1
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/1533/diff-lcs-%{version}.tar.gz
# Source0-md5:	ecea8ae3b8823e740ef6cbef84495245
Source1:	setup.rb
Patch0:	%{name}-nogems.patch
URL:	http://raa.ruby-lang.org/project/diff-lcs/
BuildRequires:	ruby
BuildRequires:	pax
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt longest
common subsequence (LCS) algorithm to compute intelligent differences between
two sequenced enumerable containers. The implementation is based on Mario I.
Wolczko's Smalltalk version (1.2, 1993) and Ned Konz's Perl version
(Algorithm::Diff). 

%package -n htmldiff
Summary:	Tool to find differences in HTML files
Group:	Applications/Text
Requires:	ruby-Text-Format >= 0.64

%description -n htmldiff
Tool to find differences in HTML files

%package ldiff
Summary:	Ruby Diff tool
Group:	Applications/Text

%description ldiff
Ruby Diff tool

%prep
rm -rf diff-lcs-%{version}
# use pax because dirs in tar file are read-only, preventing extraction
gunzip -c %{SOURCE0} | pax -r -v
chmod -R u+rw diff-lcs-%{version}
%setup -D -T -n diff-lcs-%{version}
%patch0 -p1

%build
cp %{SOURCE1} .
ruby setup.rb config \
        --site-ruby=%{ruby_rubylibdir} \
        --so-dir=%{ruby_archdir}

ruby setup.rb setup
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib

rm ri/ri/Array/cdesc-Array.yaml
rm ri/ri/String/cdesc-String.yaml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
        --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*
%{ruby_ridir}/*

%files -n htmldiff
%{_bindir}/htmldiff
   
%files ldiff
%{_bindir}/ldiff
