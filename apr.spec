#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1E1F909911C78735 (wrowe@apache.org)
#
Name     : apr
Version  : 1.6.5
Release  : 30
URL      : http://www.apache.org/dist/apr/apr-1.6.5.tar.gz
Source0  : http://www.apache.org/dist/apr/apr-1.6.5.tar.gz
Source99 : http://www.apache.org/dist/apr/apr-1.6.5.tar.gz.asc
Summary  : The Apache Portable Runtime
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
%setup -q -n apr-1.6.5
pushd ..
cp -a apr-1.6.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548257595
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --enable-nonportable-atomics   --enable-threads --with-devrandom=/dev/urandom
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --enable-nonportable-atomics   --enable-threads --with-devrandom=/dev/urandom
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
export SOURCE_DATE_EPOCH=1548257595
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/apr
cp LICENSE %{buildroot}/usr/share/package-licenses/apr/LICENSE
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/apr.exp

%files bin
%defattr(-,root,root,-)
/usr/bin/apr-1-config

%files data
%defattr(-,root,root,-)
/usr/share/build-1/apr_common.m4
/usr/share/build-1/apr_rules.mk
/usr/share/build-1/find_apr.m4
/usr/share/build-1/libtool
/usr/share/build-1/make_exports.awk
/usr/share/build-1/make_var_export.awk
/usr/share/build-1/mkdir.sh

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/haswell/libapr-1.so
/usr/lib64/libapr-1.so
/usr/lib64/pkgconfig/apr-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libapr-1.so.0
/usr/lib64/haswell/libapr-1.so.0.6.5
/usr/lib64/libapr-1.so.0
/usr/lib64/libapr-1.so.0.6.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/apr/LICENSE
