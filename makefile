include makefile.in
AUTHORS.md: AUTHORS
	@cat AUTHORS > AUTHORS.md
BUGS.md: BUGS
	@cat BUGS > BUGS.md
ChangeLog.md: ChangeLog
	@cat ChangeLog > ChangeLog.md
CREDITS.md: CREDITS
	@cat CREDITS > CREDITS.md
FAQ.md: FAQ
	@cat FAQ > FAQ.md
INSTALL.md: INSTALL
	@cat INSTALL > INSTALL.md
NEWS.md: NEWS
	@cat NEWS > NEWS.md
README.md: README
	@cat README > README.md
THANKS.md: THANKS
	@cat THANKS > THANKS.md
TODO.md: TODO
	@cat TODO > TODO.md
doc: AUTHORS.md BUGS.md ChangeLog.md CREDITS.md FAQ.md INSTALL.md NEWS.md README.md THANKS.md TODO.md
