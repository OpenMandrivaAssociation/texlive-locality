# revision 20422
# category Package
# catalog-ctan /macros/latex/contrib/locality
# catalog-date 2010-11-12 15:28:10 +0100
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-locality
Version:	0.2
Release:	11
Summary:	Various macros for keeping things local
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/locality
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 753409
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718876
- texlive-locality
- texlive-locality
- texlive-locality
- texlive-locality

