exe='batterylevel'

install:
	install -Dm755 "src/$(pkgname).py" "/usr/bin/$(pkgname).py"
	install -Dm644 "src/$(pkgname)rc" "/etc/$(pkgname)rc"
	install -Dm644 "src/$(pkgname).service" "/etc/systemd/system/$(pkgname).service"
	install -Dm644 "src/$(pkgname).timer" "/etc/systemd/system/$(pkgname).timer"
	install -Dm644 LICENSE "/usr/share/licenses/$(pkgname)/LICENSE"
uninstall:
	rm "$(pkgdir)/usr/bin/$(pkgname).py"
	rm "$(pkgdir)/etc/$(pkgname)rc"
	rm "$(pkgdir)/etc/systemd/system/$(pkgname).service"
	rm "$(pkgdir)/etc/systemd/system/$(pkgname).timer"
	rm "$(pkgdir)/usr/share/licenses/$(pkgname)/LICENSE"
togit:
	git add .
	git commit -m "Updated from makefile"
	git push origin
