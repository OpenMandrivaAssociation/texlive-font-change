Name:		texlive-font-change
Version:	40403
Release:	1
Summary:	Macros to Change Text and Math fonts in plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/font-change
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/font-change.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/font-change.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/plain/font-change
%doc %{_texmfdistdir}/doc/plain/font-change

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
