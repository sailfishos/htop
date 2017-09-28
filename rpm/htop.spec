Name:       htop
Summary:    Interactive process viewer
Version:    2.0.2
Release:    1
Group:      System/Binaries
License:    GPL 2.0
URL:        http://hisham.hm/htop/
Source:     %{name}-%{version}.tar.gz
Patch0:     proper-icon-location.patch
Patch1:     run-with-fingerterm.patch
BuildRequires:  pkgconfig(ncursesw)
Requires:   fingerterm

%description
This is `htop`, an interactive process viewer.
It requires `ncurses`. It is developed primarily on Linux,
but we also have code for running under FreeBSD and Mac OS X
(help and testing are wanted for these platforms!)

%prep
%setup -q -n %{name}-%{version}/htop

%patch0 -p1
%patch1 -p1

%build
./autogen.sh
%configure
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/htop
%{_mandir}/man1/htop.1.gz
%{_datadir}/applications/htop.desktop
%{_datadir}/icons/hicolor/128x128/apps/htop.png
