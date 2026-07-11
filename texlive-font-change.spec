%global tl_name font-change
%global tl_revision 40403

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2015.2
Release:	%{tl_revision}.1
Summary:	Macros to change text and mathematics fonts in plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/font-change
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/font-change.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/font-change.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Macros to Change Text and Mathematics fonts in TeX: 45 Beautiful
Variants The macros are written for plain TeX and may be used with other
packages like AmSTeX, eplain, etc. They also work with XeTeX. The macros
allow users to change the fonts (for both text and mathematics) in their
TeX document with only one statement. The fonts may be used readily at
various predefined sizes. All the fonts called by these macro files are
free and are included in current MiKTeX and TeX Live distributions.

