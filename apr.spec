#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1E1F909911C78735 (wrowe@apache.org)
#
Name     : apr
Version  : 1.7.0
Release  : 47
URL      : http://www.apache.org/dist/apr/apr-1.7.0.tar.gz
Source0  : http://www.apache.org/dist/apr/apr-1.7.0.tar.gz
Source1  : http://www.apache.org/dist/apr/apr-1.7.0.tar.gz.asc
Summary  : Apache Portable Runtime library
Group    : Development/Tools
License  : Apache-2.0 ISC
Requires: apr-bin = %{version}-%{release}
Requires: apr-data = %{version}-%{release}
Requires: apr-lib = %{version}-%{release}
Requires: apr-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : sed
BuildRequires : util-linux-dev
Patch1: 0001-Fix-apr-pkgconfig-to-add-a-dependency-on-libuuid.patch

%description
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines, forming a system
portability layer to as many operating systems as possible,
including Unices, MS Win32, BeOS and OS/2.

%package bin
Summary: bin components for the apr package.
Group: Binaries
Requires: apr-data = %{version}-%{release}
Requires: apr-license = %{version}-%{release}

%description bin
bin components for the apr package.


%package data
Summary: data components for the apr package.
Group: Data

%description data
data components for the apr package.


%package dev
Summary: dev components for the apr package.
Group: Development
Requires: apr-lib = %{version}-%{release}
Requires: apr-bin = %{version}-%{release}
Requires: apr-data = %{version}-%{release}
Provides: apr-devel = %{version}-%{release}
Requires: apr = %{version}-%{release}

%description dev
dev components for the apr package.


%package lib
Summary: lib components for the apr package.
Group: Libraries
Requires: apr-data = %{version}-%{release}
Requires: apr-license = %{version}-%{release}

%description lib
lib components for the apr package.


%package license
Summary: license components for the apr package.
Group: Default

%description license
license components for the apr package.


%prep
%setup -q -n apr-1.7.0
cd %{_builddir}/apr-1.7.0
%patch1 -p1
pushd ..
cp -a apr-1.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661264808
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%configure --disable-static --enable-nonportable-atomics   --enable-threads --with-devrandom=/dev/urandom
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-nonportable-atomics   --enable-threads --with-devrandom=/dev/urandom
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
export SOURCE_DATE_EPOCH=1661264808
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/apr
cp %{_builddir}/apr-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/apr/2eae3e0a27a2e49e86a350c94513de0ddb1d2c98
cp %{_builddir}/apr-%{version}/NOTICE %{buildroot}/usr/share/package-licenses/apr/5d4e4cddd998a3f6e4603d6774c0cf766b317f26
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/apr.exp
/usr/lib64/glibc-hwcaps/x86-64-v3/apr.exp

%files bin
%defattr(-,root,root,-)
/usr/bin/apr-1-config

%files data
%defattr(-,root,root,-)
/usr/share/build-1/apr_rules.mk
/usr/share/build-1/libtool
/usr/share/build-1/make_exports.awk
/usr/share/build-1/make_var_export.awk
/usr/share/build-1/mkdir.sh

%files dev
%defattr(-,root,root,-)
/usr/include/apr.h
/usr/include/apr_allocator.h
/usr/include/apr_atomic.h
/usr/include/apr_cstr.h
/usr/include/apr_dso.h
/usr/include/apr_encode.h
/usr/include/apr_env.h
/usr/include/apr_errno.h
/usr/include/apr_escape.h
/usr/include/apr_file_info.h
/usr/include/apr_file_io.h
/usr/include/apr_fnmatch.h
/usr/include/apr_general.h
/usr/include/apr_getopt.h
/usr/include/apr_global_mutex.h
/usr/include/apr_hash.h
/usr/include/apr_inherit.h
/usr/include/apr_lib.h
/usr/include/apr_mmap.h
/usr/include/apr_network_io.h
/usr/include/apr_perms_set.h
/usr/include/apr_poll.h
/usr/include/apr_pools.h
/usr/include/apr_portable.h
/usr/include/apr_proc_mutex.h
/usr/include/apr_random.h
/usr/include/apr_ring.h
/usr/include/apr_shm.h
/usr/include/apr_signal.h
/usr/include/apr_skiplist.h
/usr/include/apr_strings.h
/usr/include/apr_support.h
/usr/include/apr_tables.h
/usr/include/apr_thread_cond.h
/usr/include/apr_thread_mutex.h
/usr/include/apr_thread_proc.h
/usr/include/apr_thread_rwlock.h
/usr/include/apr_time.h
/usr/include/apr_user.h
/usr/include/apr_version.h
/usr/include/apr_want.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libapr-1.so
/usr/lib64/libapr-1.so
/usr/lib64/pkgconfig/apr-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libapr-1.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libapr-1.so.0.7.0
/usr/lib64/libapr-1.so.0
/usr/lib64/libapr-1.so.0.7.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/apr/2eae3e0a27a2e49e86a350c94513de0ddb1d2c98
/usr/share/package-licenses/apr/5d4e4cddd998a3f6e4603d6774c0cf766b317f26
