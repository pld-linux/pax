Summary: POSIX File System Archiver
Name: pax
Version: 1.5
Release: 3
License: BSD
Group: Applications/Archiving
Source: %{name}_%{version}-2.tar.gz
Patch0: pax-1.5-rh.patch
Patch1: pax-1.5-time.patch
BuildRoot: %{_tmppath}/%{name}-root

%description
'pax' is the POSIX standard archive tool.  It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

%prep
%setup -q
%patch0 -p1 -b .rh
%patch1 -p1 -b .time

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
make install bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/pax
%{_mandir}/man1/*

%changelog
* Fri Feb 23 2001 Jakub Jelinek <jakub@redhat.com>
- make it build under glibc 2.2.2

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun 30 2000 Preston Brown <pbrown@redhat.com>
- debian version, which is a port from OpenBSD's latest.

* Tue Jun 13 2000 Preston Brown <pbrown@redhat.com>
- FHS paths

* Tue May 30 2000 Preston Brown <pbrown@redhat.com>
- adopted for Winston.
