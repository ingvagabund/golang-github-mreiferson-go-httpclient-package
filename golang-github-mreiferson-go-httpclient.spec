%global debug_package   %{nil}
%global import_path     github.com/mreiferson/go-httpclient
%global gopath          %{_datadir}/gocode
%global commit          c121dfe45d66997e43e25a6823fbe7466c8403fe
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-mreiferson-go-httpclient
Version:        0
Release:        0.0.git%{shortcommit}%{?dist}
Summary:        A Go HTTP client library
License:        BSD
URL:            https://github.com/mreiferson/go-httpclient
Source0:        https://github.com/mreiferson/go-httpclient/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:      noarch

%description
Provides an HTTP Transport that implements the `RoundTripper` interface and
can be used as a built in replacement for the standard librarys.

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        A Go HTTP client library
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -n %{name}-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.md
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/github.com
%dir %attr(755,root,root) %{gopath}/src/github.com/mreiferson
%dir %attr(755,root,root) %{gopath}/src/github.com/mreiferson/go-httpclient
%{gopath}/src/%{import_path}/*.go

%changelog
* Thu Jul 17 2014 Colin Walters <walters@verbum.org>
- Initial package
