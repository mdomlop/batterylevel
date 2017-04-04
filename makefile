NAME='batterylevel'
PREFIX='/usr'
TEMPDIR := $(shell mktemp -u --suffix .$(NAME))

install:
	install -Dm755 src/$(NAME).py $(PREFIX)/bin/$(NAME)
	install -Dm644 src/$(NAME).ini $(PREFIX)/etc/$(NAME).ini
	install -Dm644 src/$(NAME).service $(PREFIX)/etc/systemd/system/$(NAME).service
	install -Dm644 src/$(NAME).timer $(PREFIX)/etc/systemd/system/$(NAME).timer
	install -Dm644 COPYING $(PREFIX)/share/licenses/$(NAME)/LICENSE
	install -Dm644 AUTHORS $(PREFIX)/share/doc/$(NAME)/AUTHORS
	install -Dm644 BUGS $(PREFIX)/share/doc/$(NAME)/BUGS
	install -Dm644 ChangeLog $(PREFIX)/share/doc/$(NAME)/ChangeLog
	install -Dm644 FAQ $(PREFIX)/share/doc/$(NAME)/FAQ
	install -Dm644 INSTALL $(PREFIX)/share/doc/$(NAME)/INSTALL
	install -Dm644 NEWS $(PREFIX)/share/doc/$(NAME)/NEWS
	install -Dm644 README $(PREFIX)/share/doc/$(NAME)/README
	install -Dm644 THANKS $(PREFIX)/share/doc/$(NAME)/THANKS
	install -Dm644 TODO $(PREFIX)/share/doc/$(NAME)/TODO
	install -Dm644 examples/batterylevel.ini $(PREFIX)/share/doc/$(NAME)/examples/batterylevel.ini
	install -Dm644 examples/batterylevel.service $(PREFIX)/share/doc/$(NAME)/examples/batterylevel.service
	systemctl daemon-reload
	@echo You may want to run make service-up to start and enable service.

uninstall: service-down
	rm -f $(PREFIX)/bin/$(NAME)
	rm -f $(PREFIX)/etc/$(NAME).ini
	rm -f $(PREFIX)/etc/systemd/system/$(NAME).service
	rm -f $(PREFIX)/etc/systemd/system/$(NAME).timer
	rm -f $(PREFIX)/share/licenses/$(NAME)/LICENSE
	rm -rf $(PREFIX)/share/doc/$(NAME)/

service-up:
	systemctl start $(NAME).timer
	systemctl enable $(NAME).timer
	systemctl daemon-reload

service-down:
	systemctl stop $(NAME).timer
	systemctl disable $(NAME).timer

togit: clean
	git add .
	git commit -m "Updated from makefile"
	git push origin

clean:
	rm -f packages/pacman/$(NAME)-*.pkg.tar.xz

pacman:
	mkdir $(TEMPDIR)
	cp packages/pacman/PKGBUILD $(TEMPDIR)/
	cp packages/pacman/$(NAME).install $(TEMPDIR)/
	cd $(TEMPDIR); makepkg -dr
	cp $(TEMPDIR)/$(NAME)-*.pkg.tar.xz packages/pacman/
	rm -rf $(TEMPDIR)
	@echo Package done!
	@echo Package is in `pwd`/packages/pacman/
