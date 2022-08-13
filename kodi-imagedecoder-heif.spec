%global aname imagedecoder.heif
%global kodi_version 19.0
%global kodi_codename Matrix

Name:           kodi-imagedecoder-heif
Version:        19.0.0
Release:        1%{?dist}
Summary:        HEIF/HEIC image support for Kodi
License:        GPLv2+
URL:            https://github.com/xbmc/imagedecoder.heif
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{aname}-%{version}-%{kodi_codename}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  libde265-devel
BuildRequires:  libheif-devel

Requires:       kodi >= %{kodi_version}

ExcludeArch:    %{power64}

%description
%{summary}.


%prep
%setup -q -n %{aname}-%{version}-%{kodi_codename}

# Fix spurious-executable-perm on debug package
find . -name '*.h' -or -name '*.cpp' | xargs chmod a-x


%build
%cmake3
%cmake3_build


%install
%cmake3_install

# Fix permissions at installation
find $RPM_BUILD_ROOT%{_datadir}/kodi/addons/ -type f -exec chmod 0644 {} \;


%files
%doc README.md
%license LICENSE.md
%{_libdir}/kodi/addons/%{aname}/
%{_datadir}/kodi/addons/%{aname}/


%changelog
* Sat Aug 13 2022 Avi Alkalay <avi@unix.sh> - 19.0.0-1
- First build attempt on Fedora 36
