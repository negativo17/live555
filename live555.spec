Name:           live555
Version:        2016.07.19
Release:        1%{?dist}
Summary:        RTP/RTCP, RTSP, SIP streaming tools
License:        LGPLv2+
URL:            http://live555.com/liveMedia/

Source0:        http://live555.com/liveMedia/public/live.%{version}.tar.gz
Patch0:         https://anonscm.debian.org/cgit/pkg-multimedia/liblivemedia.git/plain/debian/patches/add-pkgconfig-file.patch

%description
This code forms a set of C++ libraries for multimedia streaming, using open
standard protocols (RTP/RTCP, RTSP, SIP).

The libraries can also be used to stream, receive, and process MPEG, H.265,
H.264, H.263+, DV or JPEG video, and several audio codecs. They can easily be
extended to support additional (audio and/or video) codecs, and can also be used
to build basic RTSP or SIP clients and servers.

%package        devel
Summary:        Development files for live555.com streaming libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
This code forms a set of C++ libraries for multimedia streaming, using open
standard protocols (RTP/RTCP, RTSP, SIP).

The libraries can also be used to stream, receive, and process MPEG, H.265,
H.264, H.263+, DV or JPEG video, and several audio codecs. They can easily be
extended to support additional (audio and/or video) codecs, and can also be used
to build basic RTSP or SIP clients and servers.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        RTP/RTCP, RTSP, SIP streaming libraries
# Obsolete base live555 just once, when upgrading to this release
Obsoletes:      %{name} < 2016.03.14

%description	libs
This code forms a set of C++ libraries for multimedia streaming, using open
standard protocols (RTP/RTCP, RTSP, SIP).

The libraries can also be used to stream, receive, and process MPEG, H.265,
H.264, H.263+, DV or JPEG video, and several audio codecs. They can easily be
extended to support additional (audio and/or video) codecs, and can also be used
to build basic RTSP or SIP clients and servers.

This package contains libraries for applications that use %{name}.

%prep
%setup -q -n live
%patch0 -p1
sed -i -e 's|-O2|%{optflags}|' config.linux-with-shared-libraries

%build
./genMakefiles linux-with-shared-libraries
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir}

# Fix libraries' permissions
chmod +x %{buildroot}%{_libdir}/*

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/*

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jul 22 2016 Simone Caronni <negativo17@gmail.com> - 2016.07.19-1
- Update to 2016.07.19.
- Add pkg-config patch from Debian.

* Tue May 24 2016 Simone Caronni <negativo17@gmail.com> - 2016.05.20-1
- Update to version 2016.05.20.

* Wed Mar 16 2016 Simone Caronni <negativo17@gmail.com> - 2016.03.14-2
- Fix libs subpackage rename.

* Tue Mar 15 2016 Simone Caronni <negativo17@gmail.com> - 2016.03.14-1
- First build.
