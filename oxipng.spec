%global debug_package %{nil}

Name:		oxipng
Version:	9.1.5
Release:	1
Source0:	https://github.com/shssoichiro/oxipng/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	Multithreaded PNG optimizer
URL:		https://github.com/shssoichiro/oxipng
License:	GPL
Group:		Application/Graphics

BuildRequires:	cargo

%description
%summary

%prep
%autosetup -p1
tar -zxf %{SOURCE1}
mkdir -p .cargo
cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
cargo build --frozen --release

%install
cargo install --locked --root %{buildroot}/usr --path .
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}
rm %{buildroot}/usr/.crates.toml
rm   %{buildroot}/usr/.crates2.json

%files
%license %{_datadir}/licenses/%{name}
%{_bindir}/%{name}
