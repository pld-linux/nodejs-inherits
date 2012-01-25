%define		pkg	inherits
Summary:	A tiny simple way to do classic inheritance in js
Name:		nodejs-%{pkg}
Version:	1.0.0
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/inherits
Source0:	http://registry.npmjs.org/inherits/-/%{pkg}-%{version}.tgz
# Source0-md5:	ec96e0e077a0320f598975bae6000316
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tiny simple way to do classic inheritance in js.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
