# revision 19709
# category Package
# catalog-ctan /macros/plain/contrib/font-change
# catalog-date 2010-07-19 16:45:16 +0200
# catalog-license other-free
# catalog-version 2010.1
Name:		texlive-font-change
Version:	2010.1
Release:	4
Summary:	Macros to Change Text and Math fonts in plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/font-change
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/font-change.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/font-change.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Macros to Change Text and Math fonts in TeX: 19 Beautiful
Variants These macros are written for plain TeX and can be used
with other packages like AmSTeX, eplain, etc. They allow you to
change the fonts (text and math) in your TeX document with only
one statement. Also different font sizes are available. All the
fonts called by these macro files are free and are included in
the present MiKTeX and TeX Live distributions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/font-change/font-change.tex
%{_texmfdistdir}/tex/plain/font-change/font_antp_euler.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt-condensed-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt-condensed-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt-condensed.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt.tex
%{_texmfdistdir}/tex/plain/font-change/font_arev.tex
%{_texmfdistdir}/tex/plain/font-change/font_artemisia_euler.tex
%{_texmfdistdir}/tex/plain/font-change/font_bera_concrete.tex
%{_texmfdistdir}/tex/plain/font-change/font_bera_euler.tex
%{_texmfdistdir}/tex/plain/font-change/font_bera_fnc.tex
%{_texmfdistdir}/tex/plain/font-change/font_bookman.tex
%{_texmfdistdir}/tex/plain/font-change/font_century.tex
%{_texmfdistdir}/tex/plain/font-change/font_charter.tex
%{_texmfdistdir}/tex/plain/font-change/font_cm.tex
%{_texmfdistdir}/tex/plain/font-change/font_cmbright.tex
%{_texmfdistdir}/tex/plain/font-change/font_concrete.tex
%{_texmfdistdir}/tex/plain/font-change/font_epigrafica_euler.tex
%{_texmfdistdir}/tex/plain/font-change/font_epigrafica_palatino.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-bold.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-condensed-bold.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-condensed-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-condensed-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-condensed.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona.tex
%{_texmfdistdir}/tex/plain/font-change/font_kp-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_kp.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-bold.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-condensed-bold.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-condensed-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-condensed-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-condensed.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier.tex
%{_texmfdistdir}/tex/plain/font-change/font_libertine_kp.tex
%{_texmfdistdir}/tex/plain/font-change/font_libertine_palatino.tex
%{_texmfdistdir}/tex/plain/font-change/font_libertine_times.tex
%{_texmfdistdir}/tex/plain/font-change/font_pagella.tex
%{_texmfdistdir}/tex/plain/font-change/font_palatino.tex
%{_texmfdistdir}/tex/plain/font-change/font_times.tex
%{_texmfdistdir}/tex/plain/font-change/font_utopia.tex
%doc %{_texmfdistdir}/doc/plain/font-change/README
%doc %{_texmfdistdir}/doc/plain/font-change/default-amssymbols.tex
%doc %{_texmfdistdir}/doc/plain/font-change/font-change.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2010.1-2
+ Revision: 752035
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2010.1-1
+ Revision: 718481
- texlive-font-change
- texlive-font-change
- texlive-font-change
- texlive-font-change

