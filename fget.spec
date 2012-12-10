%define name	fget
%define version	1.3.3
%define release	%mkrel 6

Summary:	Commandline tool for mirroring remote files via FTP
Name:           %name
Version:        %version
Release:        %release
License:        GPLv2+
Group:          Networking/File transfer
URL:            http://www.feep.net/fget/
Source0:        %{name}-%{version}.tar.bz2
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
%configure2_5x
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



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-6mdv2011.0
+ Revision: 610424
- rebuild

* Tue Feb 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.3-5mdv2010.1
+ Revision: 510216
- fix licence
- Use %%configure2_5x

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.3.3-4mdv2010.0
+ Revision: 428725
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3.3-3mdv2009.0
+ Revision: 245120
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.3.3-1mdv2008.1
+ Revision: 124974
- kill re-definition of %%buildroot on Pixel's request
- import fget


* Tue May 17 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 1.3.3-1mdk
- 1.3.3
- use mkrel macro

* Mon Nov 8 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.3.2-1mdk
- 1.3.2

* Tue Sep 21 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.3.1-1mdk
- 1.3.1
- updated URL

* Mon Jul 19 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.3.0-1mdk
- 1.3.0

* Wed Jan 14 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.2.9-1mdk
- initial contrib import
