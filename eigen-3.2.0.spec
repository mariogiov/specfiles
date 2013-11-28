#
# spec file for package samtools
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


# Following openSUSE guidelines here:
#   http://en.opensuse.org/openSUSE:Specfile_guidelines
# See here for a specfile template and some more guidlines:
#   https://fedoraproject.org/wiki/How_to_create_an_RPM_package#SPEC_templates_and_examples


Name:		eigen
Version:	3.2.0
Release:	1%{?dist}
Summary:    Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms

Group:		Productivity/Scientific/Other
License:	MPL2
URL:        http://eigen.tuxfamily.org/
Source:     http://bitbucket.org/%{name}/%{name}/get/%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATH!!

%prep
%setup -q -n eigen-eigen-ffa86ffb5570


%build
# Nothing to compile for eigen as it is only headers

%install
mkdir -p %{buildroot}%{_includedir}
cp -r Eigen %{buildroot}%{_includedir}/Eigen

#I believe the clean section is no longer necessary for the openSUSE Open Build Service
%clean
rm -rf %{buildroot}

# Here are listed the files created by the build that "belong" to the RPM that will be installed by the end-user
# There are sotred in %{buildroot} within the RPM, but the path following buildroot is where they will be installed on the system
# Note that if you write a directory /without/a/trailing/slash, you are saying that that directory and everything under it
# belong to the package; this is wrong if it is e.g. /usr/local
# If you want just the dir but not everything under it you must use the %dir directive, e.g. %dir /your/mom
%files
%defattr(-,root,root,-)
#%doc AUTHORS COPYING NEWS README THANKS
# NOTE {_bindir} becomes %{buildroot}/usr/bin or similar, see https://fedoraproject.org/wiki/Packaging:RPMMacros
%{_includedir}/Eigen

%changelog
* Thu Nov 28 2013 Mario Giovacchini <mario@scilifelab.se> - 1.0
- Intial version
