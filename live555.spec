Name:           live555
Version:        2020.07.09
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

BuildRequires:  gcc-c++
BuildRequires:  openssl-devel

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
%autosetup -p1 -n live
sed -i -e 's|-O2|%{optflags} -Wno-misleading-indentation|' config.linux-with-shared-libraries
cp %{SOURCE1} .

%build
./genMakefiles linux-with-shared-libraries
%make_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}

# Fix libraries permissions
chmod +x %{buildroot}%{_libdir}/*

%ldconfig_scriptlets libs

%files
%{_bindir}/MPEG2TransportStreamIndexer
%{_bindir}/live555HLSProxy
%{_bindir}/live555MediaServer
%{_bindir}/live555ProxyServer
%{_bindir}/mikeyParse
%{_bindir}/openRTSP
%{_bindir}/playSIP
%{_bindir}/registerRTSPStream
%{_bindir}/sapWatch
%{_bindir}/testAMRAudioStreamer
%{_bindir}/testDVVideoStreamer
%{_bindir}/testH264VideoStreamer
%{_bindir}/testH264VideoToHLSSegments
%{_bindir}/testH264VideoToTransportStream
%{_bindir}/testH265VideoStreamer
%{_bindir}/testH265VideoToTransportStream
%{_bindir}/testMKVSplitter
%{_bindir}/testMKVStreamer
%{_bindir}/testMP3Receiver
%{_bindir}/testMP3Streamer
%{_bindir}/testMPEG1or2AudioVideoStreamer
%{_bindir}/testMPEG1or2ProgramToTransportStream
%{_bindir}/testMPEG1or2Splitter
%{_bindir}/testMPEG1or2VideoReceiver
%{_bindir}/testMPEG1or2VideoStreamer
%{_bindir}/testMPEG2TransportReceiver
%{_bindir}/testMPEG2TransportStreamSplitter
%{_bindir}/testMPEG2TransportStreamTrickPlay
%{_bindir}/testMPEG2TransportStreamer
%{_bindir}/testMPEG4VideoStreamer
%{_bindir}/testOggStreamer
%{_bindir}/testOnDemandRTSPServer
%{_bindir}/testRTSPClient
%{_bindir}/testRelay
%{_bindir}/testReplicator
%{_bindir}/testWAVAudioStreamer
%{_bindir}/vobStreamer

%files libs
%license COPYING
%doc changelog.txt
%{_libdir}/libBasicUsageEnvironment.so.1
%{_libdir}/libBasicUsageEnvironment.so.1.0.1
%{_libdir}/libUsageEnvironment.so.3
%{_libdir}/libUsageEnvironment.so.3.1.0
%{_libdir}/libgroupsock.so.8
%{_libdir}/libgroupsock.so.8.2.4
%{_libdir}/libliveMedia.so.79
%{_libdir}/libliveMedia.so.79.1.3

%files devel
%{_includedir}/BasicUsageEnvironment
%{_includedir}/UsageEnvironment
%{_includedir}/groupsock
%{_includedir}/liveMedia
%{_libdir}/libBasicUsageEnvironment.so
%{_libdir}/libUsageEnvironment.so
%{_libdir}/libgroupsock.so
%{_libdir}/libliveMedia.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Jul 15 2020 Simone Caronni <negativo17@gmail.com> - 1:2020.07.09-1
- Update to 2020.07.09.

* Sun Jun 28 2020 Simone Caronni <negativo17@gmail.com> - 1:2020.06.25-1
- Update to 2020.06.25.
- Trim changelog.

* Sat May 23 2020 Simone Caronni <negativo17@gmail.com> - 1:2020.05.15-1
- Update to 2020.05.15.
- Update SPEC file.

* Sun Mar 15 2020 Simone Caronni <negativo17@gmail.com> - 1:2020.03.06-1
- Update to 2020.03.06.

* Thu Sep 05 2019 Simone Caronni <negativo17@gmail.com> - 1:2019.08.28-1
- Update to 2019.08.28.

* Sun Jul 07 2019 Simone Caronni <negativo17@gmail.com> - 1:2019.06.28-1
- Update to 2019.06.28.

* Tue Feb 26 2019 Simone Caronni <negativo17@gmail.com> - 1:2019.02.03-1
- Update to 2019.02.03.
