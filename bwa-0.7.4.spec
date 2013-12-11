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


# Following openSUSE guidelines here:
#   http://en.opensuse.org/openSUSE:Specfile_guidelines
# See here for a specfile template and some more guidlines:
#   https://fedoraproject.org/wiki/How_to_create_an_RPM_package#SPEC_templates_and_examples


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

# BuildRequires are packages needed to actually build binaries form source
# The procedure for doing this is a little tricky:
#   - you must find the name using for instance
#	osc ls -b -r standard RedHat:RHEL-6 | grep sqlite
#     then create a file named _link containing
#	<link project='RedHat:RHEL-6' package='sqlite3'/>
#     and add that file to your project
# See http://en.opensuse.org/openSUSE:Build_Service_Tips_and_Tricks#Find_Packages_in_a_Project
# To be honest this part is still a little confusing for me
#BuildRequires: ncurses
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	python-devel
#BuildRequires:	samtools-devel
#BuildREquires:	zlib-devel
#BuildRequires:	dos2unix

# Requires are generally handled by rpmbuild or similar
#Requires:	bowtie


%description
BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome. It consists of three algorithms: BWA-backtrack, BWA-SW and BWA-MEM. The first algorithm is designed for Illumina sequence reads up to 100bp, while the rest two for longer sequences ranged from 70bp to 1Mbp. BWA-MEM and BWA-SW share similar features such as long-read support and split alignment, but BWA-MEM, which is the latest, is generally recommended for high-quality
queries as it is faster and more accurate. BWA-MEM also has better performance than BWA-backtrack for 70-100bp Illumina reads.

%prep
# Uses the setup RPM macro, which knows about tar archives, to extract the files (tar -xvf)
%setup -q

#Fix bad permissions
#chmod -x src/align_status.*
#chmod -x src/deletions.*
#chmod -x src/insertions.*


%build
# NOTE that the files produced by make will be in the directory {_builddir}
make %{?_smp_mflags}


# NOTE that this install section is NOT run when the end-user installs a binary RPM;
#      it is only run when creating the package (i.e. on Open Build Service)
#      Essentially, your files get installed on the system in whatever comes after {buildroot} below
#      so e.g. %{buildroot}%{_bindir} installs the files on the system under /usr/bin
# NOTE This is generally when files move from {_builddir} to {buildroot}
#      but you have to make the destination directory under {buildroot} yourself if it doesn't exist
#      CWD at this point refers to {_builddir}
%install
mkdir -p %{buildroot}%{_bindir}
cp bwa %{buildroot}%{_bindir}/bwa

# e.g. samtools does not have a make install but instead packages are manually copied into place
# technically I think this mkdir stuff is very small security risk as we're generally writing to /tmp or /var
# mkdir -p %{buildroot}%{_bindir}
#cp samtools %{buildroot}%{_bindir}/samtools
#cp bcftools/bcftools %{buildroot}%{_bindir}/bcftools
#cp razip %{buildroot}%{_bindir}/razip

#I believe the clean section is no longer necessary for the openSUSE Open Build Service but rpmlint complains if it's not here
%clean
rm -rf %{buildroot}

# Here are listed the files created by the build that "belong" to the RPM, the files that will be installed by the end-user via rpm or yum
# If the pattern begins with a "/" (or when expanded from the macro) then it is taken from the %{buildroot} directory. Otherwise, the file
# is presumed to be in the current directory (e.g. inside %{_builddir}, such as documentation files that you wish to include).
%files
# defattr no longer needed?
%defattr(-,root,root,-)
# doc has some special magic that's probably worth reading about
#%doc AUTHORS COPYING NEWS README THANKS
# NOTE {_bindir} becomes /usr/bin or similar, see https://fedoraproject.org/wiki/Packaging:RPMMacros
#%{_bindir}/*
%{_bindir}/bwa

%changelog
* Wed Dec 12 2013 Guillermo Carrasco <guillermo.carrasco@scilifelab.se> - 1.0
- Intial version
