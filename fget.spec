%define name	fget
%define version	1.3.3
%define release	%mkrel 4

%define	Summary	Commandline tool for mirroring remote files via FTP

Summary:	%Summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          Networking/File transfer
URL:            http://www.feep.net/fget/
Source0:        %name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-buildroot

%description
fget is a commandline tool for mirroring remote files via FTP. It was designed
as an analog to the GNU wget utility. The fget package includes an FTP client
library, so that others can make use of FTP from within their own C programs.

%package -n %name-devel
Summary:	Development library for fget
Group:		Development/Other

%description -n %name-devel
Development library for fget

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %buildroot
%makeinstall

%clean
rm -rf %buildroot

%files 
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc README INSTALL 
%{_mandir}/*/*

%files -n %name-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*

