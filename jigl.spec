%define name    jigl
%define version 2.0.1
%define release %mkrel 6
%define Summary A perl script that generates a static html photo gallery

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          Graphics
URL:            http://xome.net/projects/jigl/
Source0:        %name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildArch:      noarch
Requires:       imagemagick jhead 

%description
jigl (pronounced jiggle) is a perl script that generates a static
html photo gallery from one or more directories of gif/jpg/png images.
It supports themes and is very customizable. It includes the ability to
display comments and EXIF info for each image in a simple clean layout.

%prep
%setup -q

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp jigl.pl $RPM_BUILD_ROOT/%{_bindir}/jigl

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/jigl
%defattr(0644,root,root,0755) 
%doc ChangeLog INSTALL Themes Todo UPGRADING




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-6mdv2011.0
+ Revision: 619828
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.0.1-5mdv2010.0
+ Revision: 429619
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.0.1-4mdv2009.0
+ Revision: 247410
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.0.1-2mdv2008.1
+ Revision: 127378
- kill re-definition of %%buildroot on Pixel's request
- import jigl


* Fri Dec 16 2005 Michael Scherer <misc@mandriva.org> 2.0.1-2mdk
- Rebuild
- use mkrel

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 2.0.1-1mdk 
- uploaded to contribs
- from Dominik Grafenhofer <dominik@grafenhofer.at>
  - First build
