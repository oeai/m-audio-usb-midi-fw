## Process this file with automake to generate Makefile.in
AUTOMAKE_OPTIONS = foreign

udevrulesdir = @UDEV_RULES_DIR@
firmwaredir = $(datadir)/usb/maudio

udevrules_DATA = 42-midisport-firmware.rules
dist_firmware_DATA = MidiSportLoader.ihx \
		     MidiSport2x2.ihx \
		     MidiSport1x1.ihx \
		     MidiSportKS.ihx \
		     MidiSport4x4.ihx \
		     MidiSport8x8-2.10.ihx \
		     MidiSport8x8-2.21.ihx

MOSTLYCLEANFILES = 42-midisport-firmware.rules files.list
EXTRA_DIST = 42-midisport-firmware.rules.in LICENSE Changelog $(PACKAGE).spec.in $(PACKAGE).spec

all-local: files.list

42-midisport-firmware.rules: Makefile $(srcdir)/42-midisport-firmware.rules.in
	rm -f $@ $@.tmp
	sed -e 's,@firmwaredir\@,$(firmwaredir),g' \
		-e 's,@fxload\@,$(FXLOAD),g' \
		$(srcdir)/42-midisport-firmware.rules.in > $@.tmp
	mv $@.tmp $@

$(PACKAGE).spec: Makefile $(srcdir)/$(PACKAGE).spec.in
	rm -f $@ $@.tmp
	sed -e 's,@version@,$(VERSION),g' \
		$(srcdir)/$(PACKAGE).spec.in > $@.tmp
	mv $@.tmp $@

files.list: Makefile
	rm -f $@
	for i in $(udevrules_DATA); do \
		echo "$(udevrulesdir)/$$i"; \
	done >> $@
	for i in $(dist_firmware_DATA); do \
		echo "$(firmwaredir)/$$i"; \
	done >> $@
