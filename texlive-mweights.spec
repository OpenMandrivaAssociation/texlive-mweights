Name:		texlive-mweights
Version:	53520
Release:	2
Summary:	Support for multiple-weight font packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mweights
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mweights.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mweights.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Many font families available for use with LaTeX are available
at multiple weights. Many Type 1-oriented support packages for
such fonts re-define the standard \mddefault or \bfdefault
macros. This can create difficulties if the weight desired for
one font family isn't available for another font family, or if
it differs from the weight desired for another font family. The
package provides a solution to these difficulties.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mweights
%doc %{_texmfdistdir}/doc/latex/mweights

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
