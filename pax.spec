Summary:	POSIX File System Archiver
Name:		pax
Version:	1.5
Release:	3
License:	BSD
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	%{name}_%{version}-2.tar.gz
Patch0:		%{name}-1.5-rh.patch
Patch1:		%{name}-1.5-time.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'pax' is the POSIX standard archive tool. It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

%prep
%setup -q
%patch0 -p1 -b .rh
%patch1 -p1 -b .time

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
%{__make} install bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pax
%{_mandir}/man1/*
