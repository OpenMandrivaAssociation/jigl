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


