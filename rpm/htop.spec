Name:       htop
Summary:    Interactive process viewer
Version:    3.2.0
Release:    1
License:    GPLv2+
URL:        https://htop.dev/
Source:     %{name}-%{version}.tar.gz
Patch0:     proper-icon-location.patch
Patch1:     run-with-fingerterm.patch
Patch2:     show-alternative-keys-in-functionbar.patch
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  python3-base

%description
This is `htop`, an interactive process viewer.
It requires `ncurses`. It is developed primarily on Linux,
but we also have code for running under FreeBSD and Mac OS X
(help and testing are wanted for these platforms!)

%package desktop
Summary:    Desktop file for htop
BuildArch:  noarch
Requires:   htop >= %{version}
Requires:   fingerterm

%description desktop
Desktop file for starting htop from app grid.

%prep
%autosetup -p1 -n %{name}-%{version}/htop

%build
./autogen.sh
%configure
%make_build

%install
%make_install

# Remove man pages
rm -Rvf %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/htop

%files desktop
%defattr(-,root,root,-)
%{_datadir}/applications/htop.desktop
%{_datadir}/icons/hicolor/128x128/apps/htop.png
%{_datadir}/icons/hicolor/scalable/apps/htop.svg
