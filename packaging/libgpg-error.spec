Name:           libgpg-error
Version:        1.10
Release:        0
License:        GPL-2.0+ ; LGPL-2.1+
Summary:        Library That Defines Common Error Values for All GnuPG Components
Url:            http://www.gnupg.org/
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon, and possibly more in the future.

%package devel
License:        GPL-2.0+ ; LGPL-2.1+ ; MIT
Summary:        Development package for libgpg-error
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libgpg-error = %{version}

%description devel
Files needed for software development using libgpg-error.

%prep
%setup -q -n libgpg-error-%{version}

%build
autoreconf -fiv
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
%make_install
# Drop the lisp stuff, it depends on ASDF and CFFI
# which needs to be packaged first
rm -r %{buildroot}%{_datadir}/common-lisp
%find_lang %{name}

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files  -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/libgpg-error*.so.*

%files devel
%defattr(-,root,root)
%doc README NEWS ChangeLog COPYING.LIB COPYING AUTHORS ABOUT-NLS
%{_datadir}/aclocal/gpg-error.m4
%{_includedir}/*
%{_bindir}/*
%{_libdir}/libgpg-error*.so

%changelog
