Name:		texlive-prettytok
Version:	63842
Release:	2
Summary:	Pretty-print token lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/prettytok
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prettytok.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prettytok.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pretty-print token lists to HTML file for debugging purposes.
Open the file in any browser to view the result. Can be used to
replace \tl_analysis_show:n.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/prettytok
%doc %{_texmfdistdir}/doc/latex/prettytok

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
