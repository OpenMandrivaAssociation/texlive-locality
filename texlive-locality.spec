Name:		texlive-locality
Version:	0.2
Release:	1
Summary:	Various macros for keeping things local
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/locality
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A toolbox of macros designed to allow the LaTeX programmer to
work around some of the restrictions of the TeX grouping
mechanisms. The present release offers a preliminary view of
the package; not all of its facilities are working optimally.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
