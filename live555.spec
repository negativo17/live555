Name:           live555
Version:        2018.09.18
Release:        1%{?dist}
Epoch:          1
Summary:        RTP/RTCP, RTSP, SIP streaming tools
License:        LGPLv2+
URL:            http://live555.com/liveMedia/

Source0:        http://live555.com/liveMedia/public/live.%{version}.tar.gz
Source1:        http://live555.com/liveMedia/public/changelog.txt
# Rebase of:
# https://anonscm.debian.org/cgit/pkg-multimedia/liblivemedia.git/plain/debian/patches/add-pkgconfig-file.patch
Patch0:         2016.11.06-add-pkgconfig-file.patch

BuildRequires:  gcc

%description
This code forms a set of C++ libraries for multimedia streaming, using open
standard protocols (RTP/RTCP, RTSP, SIP).

The libraries can also be used to stream, receive, and process MPEG, H.265,
H.264, H.263+, DV or JPEG video, and several audio codecs. They can easily be
extended to support additional (audio and/or video) codecs, and can also be used
to build basic RTSP or SIP clients and servers.

%package        devel
Summary:        Development files for live555.com streaming libraries
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

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
Obsoletes:      %{name} < %{?epoch:%{epoch}:}2016.03.14

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
sed -i -e 's|-O2|%{optflags} -DXLOCALE_NOT_USED|' config.linux-with-shared-libraries
cp %{SOURCE1} .

%build
./genMakefiles linux-with-shared-libraries
%make_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}

# Fix libraries permissions
chmod +x %{buildroot}%{_libdir}/*

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/*

%files libs
%license COPYING
%doc changelog.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Oct 01 2018 Simone Caronni <negativo17@gmail.com> - 1:2018.09.18-1
- Update to 2018.09.18.

* Thu Sep 20 2018 Simone Caronni <negativo17@gmail.com> - 1:2018.08.05-2
- Add GCC build requirement.

* Wed Aug 22 2018 Simone Caronni <negativo17@gmail.com> - 1:2018.08.05-1
- Update to 2018.08.05.

* Fri Apr 27 2018 Simone Caronni <negativo17@gmail.com> - 1:2018.04.25-1
- Update to 2018.04.25.

* Wed Jan 10 2018 Simone Caronni <negativo17@gmail.com> - 1:2017.10.28-1
- Update to 2017.10.28.

* Tue Oct 24 2017 Simone Caronni <negativo17@gmail.com> - 1:2017.09.12-1
- Update to 2017.09.12.

* Tue Oct 24 2017 Simone Caronni <negativo17@gmail.com> - 1:2017.07.18-2
- Fix compilation with glibc 2.26+.

* Tue Aug 08 2017 Simone Caronni <negativo17@gmail.com> - 1:2017.07.18-1
- Update to 2017.07.18.

* Sun May 14 2017 Simone Caronni <negativo17@gmail.com> - 1:2017.04.26-1
- Update to 2017.04.26.

* Tue Feb 14 2017 Simone Caronni <negativo17@gmail.com> - 1:2017.01.26-1
- Update to 2017.01.26.

* Wed Jan 04 2017 Simone Caronni <negativo17@gmail.com> - 1:2016.11.28-1
- Update to version 2016.11.28.
- Add changelog.

* Fri Nov 11 2016 Simone Caronni <negativo17@gmail.com> - 1:2016.11.06-2
- Update Epoch.

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 2016.11.06-1
- Update to 2016.11.06.

* Fri Jul 22 2016 Simone Caronni <negativo17@gmail.com> - 2016.07.19-1
- Update to 2016.07.19.
- Add pkg-config patch from Debian.

* Tue May 24 2016 Simone Caronni <negativo17@gmail.com> - 2016.05.20-1
- Update to version 2016.05.20.

* Wed Mar 16 2016 Simone Caronni <negativo17@gmail.com> - 2016.03.14-2
- Fix libs subpackage rename.

* Tue Mar 15 2016 Simone Caronni <negativo17@gmail.com> - 2016.03.14-1
- First build.
