%define sdevname %mklibname %{name} -d -s

Summary:	Commandline tool for mirroring remote files via FTP
Name:		fget
Version:	1.3.3
Release:	8
License:	GPLv2+
Group:		Networking/File transfer
Url:		http://www.feep.net/fget/
Source0:	ftp://ftp.feep.net/pub/software/fget/%{name}-%{version}.tar.bz2
Patch0:		fget-1.3.3-no-strip.patch

%description
fget is a commandline tool for mirroring remote files via FTP. It was designed
as an analog to the GNU wget utility. The fget package includes an FTP client
library, so that others can make use of FTP from within their own C programs.

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%package -n %{sdevname}
Summary:	Development library for fget
Group:		Development/Other
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name} < 1.3.3-6
Conflicts:	%{name}-devel < 1.3.3-6
Obsoletes:	%{name}-devel < 1.3.3-6

%description -n %{sdevname}
Development library for fget.

%files -n %{sdevname}
%{_includedir}/*.h
%{_libdir}/*.a
%{_mandir}/man3/*.3*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

