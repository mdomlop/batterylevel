PREFIX='/usr'
DESTDIR=''
PROGRAM_NAME := $(shell grep ^PROGRAM_NAME src/batterylevel.py | cut -d\" -f2)
EXECUTABLE_NAME := $(shell grep ^EXECUTABLE_NAME src/batterylevel.py | cut -d\" -f2)
DESCRIPTION := $(shell grep ^DESCRIPTION src/batterylevel.py | cut -d\" -f2)
VERSION := $(shell grep ^VERSION src/batterylevel.py | cut -d\" -f2)
AUTHOR := $(shell grep ^AUTHOR src/batterylevel.py | cut -d\" -f2)
MAIL := $(shell grep ^MAIL src/batterylevel.py | cut -d\" -f2)
LICENSE := $(shell grep ^LICENSE src/batterylevel.py | cut -d\" -f2)
TIMESTAMP = $(shell LC_ALL=C date '+%a, %d %b %Y %T %z')
TEMPDIR := $(shell mktemp -u --suffix .$(EXECUTABLE_NAME))

ChangeLog: changelog.in
	@echo "$(EXECUTABLE_NAME) ($(VERSION)) unstable; urgency=medium" > $@
	@echo >> $@
	@echo "  * Git build." >> $@
	@echo >> $@
	@echo " -- $(AUTHOR) <$(MAIL)>  $(TIMESTAMP)" >> $@
	@echo >> $@
	@cat $^ >> $@

install:
	install -Dm755 src/$(EXECUTABLE_NAME).py $(DESTDIR)/$(PREFIX)/bin/$(EXECUTABLE_NAME)
	install -Dm644 src/$(EXECUTABLE_NAME).ini $(DESTDIR)/etc/$(EXECUTABLE_NAME).ini
	install -Dm644 src/$(EXECUTABLE_NAME).service $(DESTDIR)/lib/systemd/system/$(EXECUTABLE_NAME).service
	install -Dm644 src/$(EXECUTABLE_NAME).timer $(DESTDIR)/lib/systemd/system/$(EXECUTABLE_NAME).timer
	install -Dm644 COPYING $(DESTDIR)/$(PREFIX)/share/licenses/$(EXECUTABLE_NAME)/LICENSE
	install -Dm644 AUTHORS $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/AUTHORS
	install -Dm644 BUGS $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/BUGS
	install -Dm644 ChangeLog $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/ChangeLog
	install -Dm644 FAQ $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/FAQ
	install -Dm644 INSTALL $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/INSTALL
	install -Dm644 NEWS $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/NEWS
	install -Dm644 README.md $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/README
	install -Dm644 THANKS $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/THANKS
	install -Dm644 TODO $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/TODO
	install -Dm644 examples/batterylevel.ini $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/examples/batterylevel.ini
	install -Dm644 examples/batterylevel.service $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/examples/batterylevel.service

uninstall: service-down
	rm -f $(PREFIX)/bin/$(EXECUTABLE_NAME)
	rm -f /etc/$(EXECUTABLE_NAME).ini
	rm -f /lib/systemd/system/$(EXECUTABLE_NAME).service
	rm -f /lib/systemd/system/$(EXECUTABLE_NAME).timer
	rm -f $(PREFIX)/share/licenses/$(EXECUTABLE_NAME)/LICENSE
	rm -rf $(PREFIX)/share/doc/$(EXECUTABLE_NAME)/

clean:
	rm -rf *.xz *.gz *.pot po/*.mo *.tgz *.deb *.rpm ChangeLog /tmp/tmp.*.$(EXECUTABLE_NAME) debian/changelog debian/README debian/files debian/$(EXECUTABLE_NAME) debian/debhelper-build-stamp debian/$(EXECUTABLE_NAME)*

deb: ChangeLog
	cp README.md debian/README
	cp ChangeLog debian/changelog
	#fakeroot debian/rules clean
	#fakeroot debian/rules build
	fakeroot debian/rules binary
	mv ../batterylevel_$(VERSION)_all.deb .
	@echo Package done!
	@echo You can install it as root with:
	@echo dpkg -i batterylevel_$(VERSION)_all.deb

pacman: clean
	mkdir $(TEMPDIR)
	tar cf $(TEMPDIR)/$(EXECUTABLE_NAME).tar ../$(EXECUTABLE_NAME)
	cp packages/pacman/local/PKGBUILD $(TEMPDIR)/
	cd $(TEMPDIR); makepkg
	cp $(TEMPDIR)/$(EXECUTABLE_NAME)-*.pkg.tar.xz .
	@echo Package done!
	@echo You can install it as root with:
	@echo pacman -U $(EXECUTABLE_NAME)-*.pkg.tar.xz
