# Note: this file was written on a Slackware system.
# You might want to fix the remaining bugs before using it.  ;-)

Name: midisport-firmware
Version: 1.2
Release: 1
Summary: firmware for MidiSport devices
License: proprietary
Group: System Environment/Daemons
Source: %{name}-%{version}.tar.gz
URL: http://usb-midi-fw.sourceforget.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildArch: noarch

# fxload may be part of linux-hotplug
Requires: fxload udev

%description
This package allows you to use the MidiSport USB MIDI interfaces from
M-Audio/Midiman with Linux. It sets up udev rules to automatically load
the firmware into the device.

 Supported devices:
 - MidiSport 1x1
 - MidiSport 2x2
 - MidiSport 4x4
 - MidiSport 8x8
 - MidiSport Uno
 - Keystation
 - Oxygen
 - Radium

(You don't need a firmware download for the USB Audio Quattro, Duo, or
MidiSport 2x4.)

%prep
%setup

%build
%configure
make

%install
make DESTDIR=%{buildroot} install

%files -f files.list
%defattr(-,root,root)
%doc README LICENSE Changelog

%clean
rm -rf %{buildroot}

%changelog
* Sat Feb 11 2006 Clemens Ladisch <clemens@ladisch.de>
  created
