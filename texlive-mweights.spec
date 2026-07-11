%global tl_name mweights
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for multiple-weight font packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mweights
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mweights.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mweights.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Many font families available for use with LaTeX are available at
multiple weights. Many Type 1-oriented support packages for such fonts
re-define the standard \mddefault or \bfdefault macros. This can create
difficulties if the weight desired for one font family isn't available
for another font family, or if it differs from the weight desired for
another font family. The package provides a solution to these
difficulties.

