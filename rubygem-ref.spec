#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-ref
Version  : 1.0.5
Release  : 5
URL      : https://rubygems.org/downloads/ref-1.0.5.gem
Source0  : https://rubygems.org/downloads/ref-1.0.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
This library provides object references for Ruby as well as some common utilities for working with references. Object references are used to point to other objects and come in three distinct flavors that interact differently with the garbage collector.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ref-1.0.5
gem spec %{SOURCE0} -l --ruby > rubygem-ref.gemspec

%build
gem build rubygem-ref.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
ref-1.0.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/ref-1.0.5
ruby -v -I.:lib test*/test_*.rb
ruby -v -I.:lib test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/ref-1.0.5.gem
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/cdesc-AbstractReferenceKeyMap.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/clear-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/keys-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/merge%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/ref_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/remove_reference_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceKeyMap/to_a-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/cdesc-AbstractReferenceValueMap.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/clear-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/merge%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/remove_reference_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/to_a-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/AbstractReferenceValueMap/values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/MockReference/cdesc-MockReference.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/MockSoftReference/cdesc-MockSoftReference.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/MockWeakReference/cdesc-MockWeakReference.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/ObjectSpace/cdesc-ObjectSpace.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/ObjectSpace/define_finalizer-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/ObjectSpace/define_finalizer_with_mock_reference-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/ObjectSpace/define_finalizer_without_mock_reference-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/SoftReference/cdesc-SoftReference.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/SoftReference/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/SoftReference/new_with_mock_reference-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/SoftReference/new_without_mock_reference-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/WeakReference/cdesc-WeakReference.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/WeakReference/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/WeakReference/new_with_mock_reference-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/WeakReference/new_without_mock_reference-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/cdesc-Mock.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/cleanup-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/gc-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/setup-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Mock/use-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/ObjectSpace/cdesc-ObjectSpace.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Reference/cdesc-Reference.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Reference/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Reference/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Reference/object-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/Reference/referenced_object_id-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/ReferenceQueue/cdesc-ReferenceQueue.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/ReferenceQueue/empty%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/ReferenceQueue/monitor-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/ReferenceQueue/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/ReferenceQueue/pop-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/ReferenceQueue/push-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/ReferenceQueue/shift-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/ReferenceQueue/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/SafeMonitor/cdesc-SafeMonitor.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/SafeMonitor/lock-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/SafeMonitor/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/SafeMonitor/synchronize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/SafeMonitor/unlock-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/SoftKeyMap/cdesc-SoftKeyMap.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/SoftReference/cdesc-SoftReference.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/SoftReference/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/SoftReference/object-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/SoftValueMap/cdesc-SoftValueMap.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/StrongReference/cdesc-StrongReference.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/StrongReference/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/StrongReference/object-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/WeakKeyMap/cdesc-WeakKeyMap.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/WeakReference/ReferencePointer/cdesc-ReferencePointer.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/WeakReference/ReferencePointer/cleanup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/WeakReference/ReferencePointer/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/WeakReference/ReferencePointer/object-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/WeakReference/ReferencePointer/supports_backreference%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/WeakReference/cdesc-WeakReference.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/WeakReference/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/WeakReference/object-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/WeakValueMap/cdesc-WeakValueMap.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/Ref/cdesc-Ref.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/ref-1.0.5/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/MIT_LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/VERSION
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/ext/java/org/jruby/ext/ref/ReferencesService.java
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/ext/java/org/jruby/ext/ref/RubySoftReference.java
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/ext/java/org/jruby/ext/ref/RubyWeakReference.java
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/org/jruby/ext/ref/references.jar
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/abstract_reference_key_map.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/abstract_reference_value_map.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/mock.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/reference.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/reference_queue.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/safe_monitor.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/soft_key_map.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/soft_reference.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/soft_value_map.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/strong_reference.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/weak_key_map.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/weak_reference.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/weak_reference/iron_ruby.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/weak_reference/pure_ruby.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/weak_reference/weak_ref.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/lib/ref/weak_value_map.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/mock_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/mock_test.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/reference_key_map_behavior.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/reference_key_map_behavior.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/reference_queue_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/reference_queue_test.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/reference_value_map_behavior.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/reference_value_map_behavior.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/soft_key_map_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/soft_key_map_test.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/soft_reference_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/soft_reference_test.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/soft_value_map_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/soft_value_map_test.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/strong_reference_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/strong_reference_test.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/test_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/test_helper.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/weak_key_map_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/weak_key_map_test.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/weak_reference_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/weak_reference_test.rbc
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/weak_value_map_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ref-1.0.5/test/weak_value_map_test.rbc
/usr/lib64/ruby/gems/2.2.0/specifications/ref-1.0.5.gemspec
