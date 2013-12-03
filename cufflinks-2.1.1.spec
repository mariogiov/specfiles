#
# spec file for package cufflinks
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


# http://en.opensuse.org/openSUSE:Package_naming_guidelines
Name:		cufflinks
Version:	2.1.1
Release:	1%{?dist}
Summary:	Transcript assembly, differential expression, and differential regulation for RNA-Seq

# Non-standard group as required by http://en.opensuse.org/openSUSE:Package_group_guidelines
Group:		Productivity/Scientific/Other
License:	MIT
URL:		http://cufflinks.cbcb.umd.edu/
Source:		http://cufflinks.cbcb.umd.edu/downloads/%{name}-%{version}.tar.gz
# preferred path (as per http://en.opensuse.org/openSUSE:Specfile_guidelines)
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

# BuildRequires are packages needed to actually build binaries form source
BuildRequires: boost
BuildRequires: eigen
BuildRequires: samtools


%description
Cufflinks assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples. It accepts aligned RNA-Seq reads and assembles the alignments into a parsimonious set of transcripts. Cufflinks then estimates the relative abundances of these transcripts based on how many reads support each one, taking into account biases in library preparation protocols. 

Cufflinks is a collaborative effort between the Laboratory for Mathematical and Computational Biology, led by Lior Pachter at UC Berkeley, Steven Salzberg's Center for Computational Biology at the Institute of Genetic Medicine at Johns Hopkins University, and Barbara Wold's lab at Caltech.


%prep
#%setup -q --with-eigen=/usr/include/Eigen --prefix=%%{buildroot}
# I know, the capital E in Eigen makes me uncomfortable too. That's how they set the default.
%setup


%build
%configure -q --prefix=/usr/local --with-eigen=/usr/include/eigen --with-boost=/usr/include/boost --with-boost-thread=/usr/lib/libboost_thread.so
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

#I believe the clean section is no longer necessary for the openSUSE Open Build Service
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
#%doc AUTHORS COPYING NEWS README THANKS
%{_bindir}/*


%changelog
* Wed Dec 04 2013 Mario Giovacchini <mario@scilifelab.se> - 1.0
- Intial version
