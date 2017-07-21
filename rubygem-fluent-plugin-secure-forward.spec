# Generated from fluent-plugin-secure-forward-0.4.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-secure-forward

Name: rubygem-%{gem_name}
Version: 0.4.5
Release: 1%{?dist}
Summary: Fluentd input/output plugin to forward over SSL with authentications
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/tagomoris/fluent-plugin-secure-forward
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
Provides: rubygem(%{gem_name}) = %{version}
Requires: rubygem(proxifier)
Requires: rubygem(resolve-hostname)

# BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
Message forwarding over SSL with authentication.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{_bindir}/secure-forward-ca-generate
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_instdir}/example
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fluent-plugin-secure-forward.gemspec
%{gem_instdir}/test

%changelog
* Thu Jun 29 2017 Rich Megginson <rmeggins@redhat.com> - 0.4.5-1
- version 0.4.5

* Wed Aug 24 2016 Rich Megginson <rmeggins@redhat.com> - 0.4.3-2
- added Provides for rubygem(fluent-plugin-secure-forward)
- rubygem Requires must be in the format rubygem(gem_name) not the actual rpm package name

* Wed Aug 17 2016 Yanis Guenane <yguenane@redhat.com> - 0.4.3-1
- Initial package
