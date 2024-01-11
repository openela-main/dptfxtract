Summary: dptfxtract utility

Name:		dptfxtract
Version:	1
Release:	2%{?dist}
Group:		Development/Libraries
License:	Intel
Source0:	dptfxtract.tar.bz2
URL:		https://github.com/intel/dptfxtract
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch:	x86_64

%description
This is a companion tool to Linux Thermal Daemon (thermald). This tool tries to
reuse some of the tables used by "Intel ® Dynamic Platform and Thermal
Framework (Intel® DPTF)" by converting to the thermal_conf.xml format used by
thermald.

%global debug_package %{nil}

%prep
%autosetup

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/dptfxtract
install -m 755 dptfxtract $RPM_BUILD_ROOT/%{_sbindir}/dptfxtract
install -m 644 COPYING $RPM_BUILD_ROOT/usr/share/doc/dptfxtract/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sbindir}/dptfxtract
/usr/share/doc/dptfxtract/COPYING

%changelog
* Sun Sep 30 2018 Prarit Bhargava <prarit@redhat.com> 1.2
- Make dptfxtract executable [1493839]
- add %{?dist} to release [1493839]
* Wed Sep 26 2018 Prarit Bhargava <prarit@redhat.com> 1.1
- Add COPYING license [1493839]
- Switch to autosetup in rpm prep stage [1493839]
* Tue Aug 28 2018 Prarit Bhargava <prarit@redhat.com> 1.0
- Initial version [1493839]
