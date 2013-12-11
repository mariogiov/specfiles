#
# spec file for package BWA
#
# Copyright (c) 2013 Guillermo Carrasco <guillermo.carrasco@scilifelab.se>
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


# http://en.opensuse.org/openSUSE:Package_naming_guidelines
Name:		bwa
Version:	0.7.4
Release:	1%{?dist}
Summary:	BWA is a software for mapping low-divergent sequences against a large reference genome

# Non-standard group as required by http://en.opensuse.org/openSUSE:Package_group_guidelines
Group:		Scientific/Other
License:	GPL
URL:		http://bio-bwa.sourceforge.net/
Source:		http://downloads.sourceforge.net/project/bio-bwa/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-build


%description
BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome. It consists of three algorithms: BWA-backtrack, BWA-SW and BWA-MEM. The first algorithm is designed for Illumina sequence reads up to 100bp, while the rest two for longer sequences ranged from 70bp to 1Mbp. BWA-MEM and BWA-SW share similar features such as long-read support and split alignment, but BWA-MEM, which is the latest, is generally recommended for high-quality
queries as it is faster and more accurate. BWA-MEM also has better performance than BWA-backtrack for 70-100bp Illumina reads.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
cp bwa %{buildroot}%{_bindir}/bwa

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/bwa

%changelog
* Wed Dec 12 2013 Guillermo Carrasco <guillermo.carrasco@scilifelab.se> - 1.0
- Intial version
