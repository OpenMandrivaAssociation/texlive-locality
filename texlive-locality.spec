%global tl_name locality
%global tl_revision 20422

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Various macros for keeping things local
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/locality
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/locality.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A toolbox of macros designed to allow the LaTeX programmer to work
around some of the restrictions of the TeX grouping mechanisms. The
present release offers a preliminary view of the package; not all of its
facilities are working optimally

