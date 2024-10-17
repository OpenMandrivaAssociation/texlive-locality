Name:		texlive-locality
Version:	20422
Release:	2
Summary:	Various macros for keeping things local
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/locality
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A toolbox of macros designed to allow the LaTeX programmer to
work around some of the restrictions of the TeX grouping
mechanisms. The present release offers a preliminary view of
the package; not all of its facilities are working optimally.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/locality/locality.sty
%doc %{_texmfdistdir}/doc/latex/locality/README
%doc %{_texmfdistdir}/doc/latex/locality/changes.txt
%doc %{_texmfdistdir}/doc/latex/locality/locality.pdf
#- source
%doc %{_texmfdistdir}/source/latex/locality/locality.dtx
%doc %{_texmfdistdir}/source/latex/locality/locality.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
