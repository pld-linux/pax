Summary:	POSIX File System Archiver
Summary(pl):	Archiwizer plików POSIX
Name:		pax
Version:	1.5
Release:	3
License:	BSD
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	%{name}_%{version}-2.tar.gz
# this file comes from slink, which no longer exists:
#Source0:	ftp://ftp.debian.org/debian/dists/slink/main/source/%{name}_%{version}-2.tar.gz
# newer debian-patched version:
#Source0:	ftp://ftp.debian.org/debian/dists/potato/main/source/%{name}_%{version}-8.tar.gz
# or original(?) archive from 1997:
#Source0:	http://www.netsw.org/system/tools/fileutils/archive/meta/%{name}-%{version}.tar.gz
Patch0:		%{name}-1.5-rh.patch
Patch1:		%{name}-1.5-time.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'pax' is the POSIX standard archive tool. It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

%description -l pl
'pax' jest standardowym narzêdziem archiwizuj±cym w standardzie POSIX.
Obs³uguje dwie najczê¶ciej wystêpuj±ce na uniksach postaci archiwów:
CPIO i TAR.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
%{__make} install bindir=$RPM_BUILD_ROOT%{_bindir} mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pax
%{_mandir}/man1/*
