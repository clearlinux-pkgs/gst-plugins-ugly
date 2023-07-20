#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
# Source0 file verified with key 0x5D2EEE6F6F349D7C (tim@centricular.com)
#
Name     : gst-plugins-ugly
Version  : 1.22.5
Release  : 55
URL      : https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-1.22.5.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-1.22.5.tar.xz
Source1  : https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-1.22.5.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gst-plugins-ugly-lib = %{version}-%{release}
Requires: gst-plugins-ugly-license = %{version}-%{release}
Requires: gst-plugins-ugly-locales = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
ASF Demuxer Plugin
==================
Overview
--------
This plugin is a demuxer for Microsoft's ASF Advanced Streaming Format
or ASF [1]. This demuxer only supports ASF v1.0 since the vast
majority of existing ASF files use that version. The specification
has been derived from a third party source [2] without reference to
the original.

%package lib
Summary: lib components for the gst-plugins-ugly package.
Group: Libraries
Requires: gst-plugins-ugly-license = %{version}-%{release}

%description lib
lib components for the gst-plugins-ugly package.


%package license
Summary: license components for the gst-plugins-ugly package.
Group: Default

%description license
license components for the gst-plugins-ugly package.


%package locales
Summary: locales components for the gst-plugins-ugly package.
Group: Default

%description locales
locales components for the gst-plugins-ugly package.


%prep
%setup -q -n gst-plugins-ugly-1.22.5
cd %{_builddir}/gst-plugins-ugly-1.22.5
pushd ..
cp -a gst-plugins-ugly-1.22.5 buildavx2
popd
pushd ..
cp -a gst-plugins-ugly-1.22.5 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689876040
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2
CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -Wl,-z,x86-64-v4 -O3 -mprefer-vector-width=512" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -Wl,-z,x86-64-v4 -mprefer-vector-width=512" LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx512
ninja -v -C builddiravx512

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gst-plugins-ugly
cp %{_builddir}/gst-plugins-ugly-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gst-plugins-ugly/545f380fb332eb41236596500913ff8d582e3ead || :
cp %{_builddir}/gst-plugins-ugly-%{version}/docs/random/LICENSE %{buildroot}/usr/share/package-licenses/gst-plugins-ugly/22990b105a08bb838c95fcc4bc5450c6dfdc79ac || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot}-v4 ninja -C builddiravx512 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gst-plugins-ugly-1.0
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gstreamer-1.0/libgstasf.so
/V3/usr/lib64/gstreamer-1.0/libgstdvdlpcmdec.so
/V3/usr/lib64/gstreamer-1.0/libgstdvdsub.so
/V3/usr/lib64/gstreamer-1.0/libgstrealmedia.so
/V4/usr/lib64/gstreamer-1.0/libgstasf.so
/V4/usr/lib64/gstreamer-1.0/libgstdvdlpcmdec.so
/V4/usr/lib64/gstreamer-1.0/libgstdvdsub.so
/V4/usr/lib64/gstreamer-1.0/libgstrealmedia.so
/usr/lib64/gstreamer-1.0/libgstasf.so
/usr/lib64/gstreamer-1.0/libgstdvdlpcmdec.so
/usr/lib64/gstreamer-1.0/libgstdvdsub.so
/usr/lib64/gstreamer-1.0/libgstrealmedia.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gst-plugins-ugly/22990b105a08bb838c95fcc4bc5450c6dfdc79ac
/usr/share/package-licenses/gst-plugins-ugly/545f380fb332eb41236596500913ff8d582e3ead

%files locales -f gst-plugins-ugly-1.0.lang
%defattr(-,root,root,-)

