#
# spec file for package <PACKAGE_NAME>
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


Name:		boost
Version:	1.55.0
Release:	1%{?dist}
Summary:	Boost provides free peer-reviewed portable C++ source libraries

# Should CHANGE this group
Group:		Productivity/Scientific/Other
License:	Boost
URL:		http://www.boost.org
Source:		http://sourceforge.net/projects/boost/files/boost/1.55.0/boost_1_55_0.tar.gz/download
# preferred path (as per http://en.opensuse.org/openSUSE:Specfile_guidelines)
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

BuildRequires: gcc-c++
#BuildRequires: bzip2-devel # not available for RHEL/CentOS in software.opensuse.org repos
# This is not strictly required but if you want to build Boost-Python it is
BuildRequires: python
BuildRequires: python-devel


%description
Boost provides free peer-reviewed portable C++ source libraries.

We emphasize libraries that work well with the C++ Standard Library. Boost libraries are intended to be widely useful, and usable across a broad spectrum of applications. The Boost license encourages both commercial and non-commercial use.

We aim to establish "existing practice" and provide reference implementations so that Boost libraries are suitable for eventual standardization. Ten Boost libraries are included in the C++ Standards Committee's Library Technical Report (TR1) and in the new C++11 Standard. C++11 also includes several more Boost libraries in addition to those from TR1. More Boost libraries are proposed for TR2.


%prep
%setup -q -n boost_1_55_0


%build
# build b2, bjam
sh bootstrap.sh

%install
rm -rf %{buildroot}
# prefix=/usr installs to /usr/include/boost
./b2 install --prefix=%{buildroot}%{_prefix} --toolset=gcc architecture=x86 link=static runtime-link=static stage install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
# /usr/include/boost
%{_includedir}/*
# /usr/lib, /usr/lib64
%{_libdir}/*
# /usr/share/docs
%{_docdir}/*

%changelog
* Wed Dec 4 2013 Mario Giovacchini <mario@scilifelab.se> - 1.0
- Intial version
