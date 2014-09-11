%global debug_package   %{nil}
%global import_path     github.com/mreiferson/go-httpclient
%global commit          c121dfe45d66997e43e25a6823fbe7466c8403fe
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-mreiferson-go-httpclient
Version:        0
Release:        0.0.git%{shortcommit}%{?dist}
Summary:        A Go HTTP client library
License:        BSD
URL:            https://github.com/mreiferson/go-httpclient
Source0:        https://github.com/mreiferson/go-httpclient/archive/%{commit}/%{name}-%{commit}.tar.gz
ExclusiveArch:  %{go_arches} noarch

%description
Provides an HTTP Transport that implements the `RoundTripper` interface and
can be used as a built in replacement for the standard librarys.

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        A Go HTTP client library
Provides:       golang(%{import_path}) = %{version}-%{release}
BuildArch:      noarch

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.md
%dir %attr(755,root,root) %{gopath}/src/github.com/mreiferson
%dir %attr(755,root,root) %{gopath}/src/github.com/mreiferson/go-httpclient
%{gopath}/src/%{import_path}/*.go

%changelog
* Thu Jul 17 2014 Colin Walters <walters@verbum.org> - 0-0.0gitc121dfe
- Initial package
