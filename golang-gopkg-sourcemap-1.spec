# Run tests in check section
%bcond_without check

%global goipath         gopkg.in/sourcemap.v1
%global forgeurl        https://github.com/go-sourcemap/sourcemap
Version:                1.0.5

%global common_description %{expand:
Source Maps consumer for Golang.}

%gometa

Name:    %{goname}
Release: 4%{?dist}
Summary: Source Maps consumer for Golang
License: BSD
URL:     %{gourl}
Source:  %{gosource}

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch

Provides: golang-gopkg-sourcemap-devel = %{version}-%{release}
Obsoletes: golang-gopkg-sourcemap-devel < 1.0.5-3
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.5-3
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.5-1
- First package for Fedora

