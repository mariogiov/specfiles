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


# Following openSUSE guidelines here:
#   http://en.opensuse.org/openSUSE:Specfile_guidelines
# See here for a specfile template and some more guidlines:
#   https://fedoraproject.org/wiki/How_to_create_an_RPM_package#SPEC_templates_and_examples


# http://en.opensuse.org/openSUSE:Package_naming_guidelines
Name:		example
Version:	0.0.0
Release:	1%{?dist}
Summary:	A short descriptive sentence that ends without a period

# Non-standard group as required by http://en.opensuse.org/openSUSE:Package_group_guidelines
Group:		Productivity/Scientific/Other
License:	MIT
URL:		http://main.package.site/
Source:		http://path/to/raw/source/%{version}/package-%{version}.tar.bz2
# preferred path (as per http://en.opensuse.org/openSUSE:Specfile_guidelines)
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
#BuildRequires: zlib
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
A description:

- This
- can
- include
- lists, even ones
  that wrap as long as they start with two spaces

%prep
# Uses the setup RPM macro, which knows about tar archives, to extract the files (tar -xvf)
%setup -q

#Fix bad permissions
#chmod -x src/align_status.*
#chmod -x src/deletions.*
#chmod -x src/insertions.*


%build
# NOTE that the files produced by make will be in the directory {_builddir}
%configure
make %{?_smp_mflags}
make %{?_smp_mflags} razip


# NOTE that this install section is NOT run when the end-user installs a binary RPM;
#      it is only run when creating the package (i.e. on Open Build Service)
#      Essentially, your files get installed on the system in whatever comes after {buildroot} below
#      so e.g. %{buildroot}%{_bindir} installs the files on the system under /usr/bin
# NOTE This is generally when files move from {_builddir} to {buildroot}
#      but you have to make the destination directory under {buildroot} yourself if it doesn't exist
#      CWD at this point refers to {_builddir}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}I
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
%{_bindir}/samtools
%{_bindir}/bcftools
%{_bindir}/razip

%changelog
* Tue Nov 19 2013 Mario Giovacchini <mario@scilifelab.se> - 1.0
- Intial version
