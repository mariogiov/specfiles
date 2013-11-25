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

Name:		tmux
Version:	1.8
Release:	1%{?dist}
Summary:	Multiprocessing

Group:		Productivity/Scientific/Other
License:	MIT
URL:		http://http://tmux.sourceforge.net/
Source:		http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build


%description

tmux is a "terminal multiplexer". It allows a number of terminals (or windows)
to be accessed and controlled from a single terminal. It is intended to be
a simple, modern, BSD-licensed alternative to programs such as GNU screen.

%prep
%setup -q

%build
%{configure}
make %{?_smp_mflags}


%install
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/tmux
%{_defaultdocdir}/tmux-1.6
%{_mandir}/man1/tmux.1.gz
%{_localstatedir}/run/tmux

%changelog
* Tue Nov 19 2013 Mario Giovacchini <mario@scilifelab.se> - 1.0
- Intial version
