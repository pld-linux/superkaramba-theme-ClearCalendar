%define		theme	ClearCalendar

Summary:	superkaramba - Clear Calendar theme
Summary(pl):	superkaramba - motyw Clear Calendar
Name:		superkaramba-theme-%{theme}
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/20570-clear_cal.tar.gz
# Source0-md5:	9d570ed78587b6e304406c53ef9821f5
Patch0:		ubermon.theme.patch
URL:		http://www.kde-look.org/content/show.php?content=20570
Requires:	superkaramba
Requires:	util-linux
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a "clear" calendar to match the other clear themes. The icon
can be clicked to open Kontact. Enjoy!

%description -l pl
To jest przezroczysty kalendarz pasuj±cy do innych przezroczystych
motywów. Ikonê mo¿na klikn±æ, aby otworzyæ Kontact. Mi³ej zabawy!

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
