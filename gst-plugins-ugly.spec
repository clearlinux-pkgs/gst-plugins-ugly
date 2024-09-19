#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v19
# autospec commit: f35655a
#
# Source0 file verified with key 0x5D2EEE6F6F349D7C (tim@centricular.com)
#
Name     : gst-plugins-ugly
Version  : 1.24.8
Release  : 70
URL      : https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-1.24.8.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-1.24.8.tar.xz
Source1  : https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-1.24.8.tar.xz.asc
Source2  : 5D2EEE6F6F349D7C.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gst-plugins-ugly-lib = %{version}-%{release}
Requires: gst-plugins-ugly-license = %{version}-%{release}
Requires: gst-plugins-ugly-locales = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gnupg
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Various Info
============
http://dvd.sourceforge.net/

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 5D2EEE6F6F349D7C' gpg.status
%setup -q -n gst-plugins-ugly-1.24.8
cd %{_builddir}/gst-plugins-ugly-1.24.8
pushd ..
cp -a gst-plugins-ugly-1.24.8 buildavx2
popd
pushd ..
cp -a gst-plugins-ugly-1.24.8 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726756588
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2
GOAMD64=v4
CFLAGS="$CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 " CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 " LDFLAGS="$LDFLAGS -march=x86-64-v4 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx512
ninja -v -C builddiravx512

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs
cd ../buildavx2;
meson test -C builddir --print-errorlogs || :
cd ../buildavx512;
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gst-plugins-ugly
cp %{_builddir}/gst-plugins-ugly-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gst-plugins-ugly/545f380fb332eb41236596500913ff8d582e3ead || :
cp %{_builddir}/gst-plugins-ugly-%{version}/docs/random/LICENSE %{buildroot}/usr/share/package-licenses/gst-plugins-ugly/22990b105a08bb838c95fcc4bc5450c6dfdc79ac || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v4
DESTDIR=%{buildroot}-v4 ninja -C builddiravx512 install
GOAMD64=v2
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

