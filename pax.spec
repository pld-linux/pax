Summary:	POSIX File System Archiver
Summary(pl):	Archiwizer plików POSIX
Name:		pax
Version:	1.5
Release:	7
License:	BSD
Group:		Applications/Archiving
# debian version:
Source0:	ftp://ftp.debian.org/debian/pool/main/p/pax/%{name}_%{version}.orig.tar.gz
# Source0-md5:	fc391481339c8222f40afae21b1188da
# or original(?) archive from 1997:
# Source0:	http://www.netsw.org/system/tools/fileutils/archive/meta/%{name}-%{version}.tar.gz
# Patch0:		%{name}-1.5-rh.patch
# Patch1:		%{name}-1.5-time.patch
Patch0:		ftp://ftp.debian.org/debian/pool/main/p/%{name}_%{version}-12.diff.gz
Patch1:		%{name}-DESTDIR_over_debian.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'pax' is the POSIX standard archive tool. It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

%description -l pl
'pax' jest standardowym narzêdziem archiwizuj±cym w standardzie POSIX.
Obs³uguje dwie najczê¶ciej wystêpuj±ce na uniksach postaci archiwów:
CPIO i TAR.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p1
%patch1 -p0

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -DNET2_STAT -D_PATH_DEFTAPE=\\\"/dev/rmt0\\\" -DLINUX -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc debian/copyright
%attr(755,root,root) %{_bindir}/pax
%{_mandir}/man1/*
