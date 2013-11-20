#
# spec file for package Python
#
# Copyright (c) 2013 Mario Giovacchini <mario@scilifelab.se>
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


Name:		python
Version:	2.7.6
Release:	1%{?dist}
Summary:	An interpreted, interactive, object-oriented programming language

Group:		Development/Languages/Python
License:	Python
URL:		http://www.python.org/
Source:		http://path/to/raw/source/%{version}/package-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-build


BuildRequires: sqlite3
#BuildRequires: libsqlite3
BuildRequires: sqlite-devel
#BuildRequires: libsqlite-devel


%description
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python
includes modules, classes, exceptions, very high level dynamic
data types and dynamic typing. Python supports interfaces to many
system calls and libraries, as well as to various windowing
systems (X11, Motif, Tk, Mac and MFC).

Programmers can write new built-in modules for Python in C or C++.
Python can be used as an extension language for applications that
need a programmable interface. This package contains most of the
standard Python modules, as well as modules for interfacing to the
Tix widget set for Tk and RPM.

Note that documentation for Python is provided in the python-docs
package.


%prep
# Uses the setup RPM macro, which knows about tar archives, to extract the files (tar -xvf)
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}I


%clean
rm -rf %{buildroot}


%files
# defattr no longer needed?
%defattr(-,root,root,-)
# doc has some special magic that's probably worth reading about
#%doc AUTHORS COPYING NEWS README THANKS
# NOTE {_bindir} becomes /usr/bin or similar, see https://fedoraproject.org/wiki/Packaging:RPMMacros
# NOTE all paths starting with / or expanded from macro start from {buildroot}
%{_bindir}/*
%{_includedir}/python2.7
%{_libdir}/*
%{_mandir}/*

%changelog
* Wed Nov 20 2013 Mario Giovacchini <mario@scilifelab.se> - 1.0
- Intial version
