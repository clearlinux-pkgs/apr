#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : apr
Version  : 1.5.2
Release  : 11
URL      : http://www.apache.org/dist/apr/apr-1.5.2.tar.gz
Source0  : http://www.apache.org/dist/apr/apr-1.5.2.tar.gz
Summary  : Apache Portable Runtime library
Group    : Development/Tools
License  : Apache-2.0 ISC
Requires: apr-bin
Requires: apr-lib
Requires: apr-data
BuildRequires : cmake
BuildRequires : pkgconfig(uuid)
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
Requires: apr-data

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
Requires: apr-lib
Requires: apr-bin
Requires: apr-data
Provides: apr-devel

%description dev
dev components for the apr package.


%package lib
Summary: lib components for the apr package.
Group: Libraries
Requires: apr-data

%description lib
lib components for the apr package.


%prep
%setup -q -n apr-1.5.2

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export CFLAGS="$CFLAGS -O3 -fno-semantic-interposition -ffunction-sections -flto "
export CXXFLAGS="$CXXFLAGS -O3 -fno-semantic-interposition -ffunction-sections -flto "
%configure --disable-static --enable-nonportable-atomics   --enable-threads
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/apr.exp

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
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
