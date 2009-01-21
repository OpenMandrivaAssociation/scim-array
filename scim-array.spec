%define scim_version	1.4.7

%define libname %mklibname %{name} 0

Name:		scim-array
Summary:	SCIM Array 30 Input Method Engine
Version:	1.0.1
Release:	%mkrel 1
Group:		System/Internationalization
License:	GPLv2+
URL:		http://scimarray.openfoundry.org/
Source:		http://of.openfoundry.org/download_path/scimarray/%{version}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	scim-devel >= %{scim_version}
Requires:	scim-client = %{scim_api}
Obsoletes:	%{libname}

%description
This input method engine  is developed to support the Array 30 input 
method in SCIM framework. SCIM Array 30 Input Method Engine provides
with all the functions of Array 30, including 1st and 2nd level 
short codes, special codes, and symbol input.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -f %buildroot%{scim_plugins_dir}/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING README AUTHORS ChangeLog
%_datadir/scim/icons/*
%_datadir/scim/Array
%{scim_plugins_dir}/*/*.so
