%define		kdeappsver	23.08.4
%define		qtver		5.15.2
%define		kaname		kgpg

Summary:	K Desktop Environment - interface for GnuPG
Summary(pl.UTF-8):	K Desktop Environment -  interfejs do GnuPG
Name:		ka5-%{kaname}
Version:	23.08.4
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	cae880e403ff58aeb0262b86f4b34671
URL:		https://www.kde.org/
BuildRequires:	gpgme-devel
BuildRequires:	ka5-akonadi-contacts-devel
BuildRequires:	ka5-akonadi-devel
BuildRequires:	ninja
BuildRequires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kgpg is a simple, free, open source KDE frontend for gpg. It features
- editor mode enables you to type/paste a text and
  encrypt/decrypt/sign/verify it
- key manager: import, export, delete, sign, generate and edit keys.
- integration with konqueror: left click on a file to decrypt/verify
  it, right click on a file to encrypt/sign it.
- encryption: support for symetric encryption. Multiple keys & default
  key encryption. Optional shredding of source files
- signatures: creation & verification of detached & cleartext
  signatures
- drag & drop encryption + clipboard en/decryption

%description -l pl.UTF-8
kgpg jest prostą, darmową, z otwartymi źródłami, graficzną
nakładką na gpg przeznaczoną dla KDE. Ma następujące
możliwości:
- tryb edytora umożliwiający napisanie/wklejenie tekstu oraz
  zaszyfrowanie/odszyfrowanie/podpisanie/sprawdzenie go,
- zarządzanie kluczami: import, eksport, usuwanie, podpisywanie,
  generowanie oraz edycję,
- integrację z Konquerorem: kliknięcie lewym przyciskiem na pliku w
  celu odszyfrowania/sprawdzenia go, kliknięcie prawym przyciskiem na
  pliku w celu zaszyfrowania/podpisania go,
- szyfrowanie: obsługa szyfrów symetrycznych; wiele kluczy i
  domyślne szyfrowanie kluczem; opcjonalnie niszczenie plików
  źródłowych,
- sygnatury: tworzenie i sprawdzanie oddzielonych i czysto tekstowych
  sygnatur,
- szyfrowanie metodą przeciągnij-i-upuść oraz szyfrowanie i
  odszyfrowywanie schowka.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%{?with_tests:%ninja_build test}

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgpg
/etc/xdg/autostart/org.kde.kgpg.desktop
%{_desktopdir}/org.kde.kgpg.desktop
%{_datadir}/config.kcfg/kgpg.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kgpg.Key.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_iconsdir}/hicolor/scalable/*/*.svgz
%{_datadir}/kgpg
%{_datadir}/kxmlgui5/kgpg
%{_datadir}/metainfo/org.kde.kgpg.appdata.xml
%{_datadir}/kio/servicemenus/kgpg_encryptfile.desktop
%{_datadir}/kio/servicemenus/kgpg_encryptfolder.desktop
%{_datadir}/kio/servicemenus/kgpg_viewdecrypted.desktop
%{_datadir}/qlogging-categories5/kgpg.categories
