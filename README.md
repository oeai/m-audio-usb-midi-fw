# m-audio-usb-midi-fw
M-Audio USB MIDI Firmware Loaders for Linux

it's a fork of "USB MIDI Firmware Loaders" by Clemens Ladisch and Pedro Lopez-Cabanillas
- https://sf.net/p/usb-midi-fw

Changes made because of new udev and are described in bugs and mailing lists.
- https://sf.net/p/usb-midi-fw/bugs/?source=navbar


What's this?
------------

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

The project page is <http://usb-midi-fw.sf.net/>.


Prerequisites
-------------

- Linux kernel 3.x or later
- udev version 128 or later
- fxload (release dated 2002_04_11 or later)
  (you can get fxload from <http://linux-hotplug.sf.net/>)


Installing
----------

1) Run './configure'.

2) Run 'make'.

3) As root, run 'make install'.


Uninstalling
------------

As root, run 'make uninstall'.


Running
-------

The udev rules automatically load the firmware when a MidiSport device
is connected to the computer.


Contact
-------

For help, discussion or feedback, send a mail to the mailing list at
<usb-midi-fw-user@lists.sourceforge.net>.

written by Clemens Ladisch <clemens@ladisch.de>
