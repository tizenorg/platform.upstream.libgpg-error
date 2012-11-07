#
# spec file for package libgpg-error
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libgpg-error
Version:        1.10
Release:        0
License:        GPL-2.0+ ; LGPL-2.1+
Summary:        Library That Defines Common Error Values for All GnuPG Components
Url:            http://www.gnupg.org/
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Patch0:         %{name}-nld-build.diff
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
