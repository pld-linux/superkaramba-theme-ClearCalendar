%define		theme	ClearCalendar

Summary:	superkaramba - Clear Calendar theme
Summary(pl.UTF-8):	superkaramba - motyw Clear Calendar
Name:		superkaramba-theme-%{theme}
Version:	2.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/CONTENT/content-files/20570-clear_cal.tar.gz
# Source0-md5:	d8327c3644074f6ada3af81ce5728c60
URL:		http://www.kde-look.org/content/show.php?content=20570
Requires:	superkaramba
Requires:	util-linux
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a "clear" calendar to match the other clear themes. The icon
can be clicked to open Kontact. Enjoy!

%description -l pl.UTF-8
To jest przezroczysty kalendarz pasujący do innych przezroczystych
motywów. Ikonę można kliknąć, aby otworzyć Kontact. Miłej zabawy!

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/%{theme}
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/%{theme}/icons
install clear_cal/icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/%{theme}/icons
install clear_cal/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/%{theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/superkaramba/%{theme}
