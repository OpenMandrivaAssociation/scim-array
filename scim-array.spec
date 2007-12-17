%define scim_version	1.4.7

%define libname %mklibname %{name} 0

Name:		scim-array
Summary:	SCIM Array 30 Input Method Engine
Version:	0.0.2
Release:	%mkrel 1
Group:		System/Internationalization
License:	GPL
URL:		http://scimarray.openfoundry.org/
Source:		http://rt.openfoundry.org/Foundry/Project/Download/Attachment/91593/62957/%{name}-%{version}.tar.gz
BuildRequires:	scim-devel >= %{scim_version}
Requires:	scim >= %{scim_version}
Requires:	%{libname} = %{version}-%{release}

%description
This input method engine  is developed to support the Array 30 input 
method in SCIM framework. SCIM Array 30 Input Method Engine provides
with all the functions of Array 30, including 1st and 2nd level 
short codes, special codes, and symbol input.

%package -n	%{libname}
Summary:	Scim-array library
Group:		System/Internationalization

%description -n %{libname}
Scim-array library.

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

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING README AUTHORS ChangeLog
%_datadir/scim/icons/*
%_datadir/scim/Array

%files -n %{libname}
%defattr(-,root,root)
%{scim_plugins_dir}/*/*.so
