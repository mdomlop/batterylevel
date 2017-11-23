BatteryLevel
============

A python 3 script that reads battery values and plays
some sound alerts. If necessary performs some actions too,
like power off the the machine.

If you execute `batterylevel` you can obtain some info:

        $ batterylevel
        Battery is present: BAT0
        Capacity: 60
        Status: charging

You can start and enable the provided systemd timer. And then
it will perform some action based in your configuration file.

Configuration
-------------

Edit the configuration file at `/etc/batterylevel.ini`.

Her an example:

    [DEFAULT]
    name = BAT0
    forced = False

    alarm_level = 10
    warning_level = 25
    info_level = 40
    safe_level = 90
    full_level = Full

    alarm_sound = beep -f3000 -l100 -r3 -D100 -n -f2000 -l100 -r3 -D100
    warning_sound = beep -f3000 -r3 -D1000
    info_sound = beep -f100 -l50 -r2
    safe_sound = beep -f9000
    full_sound = beep -f9000 -r3

    alarm_command = systemctl poweroff
    warning_command = sync
    info_command =
    safe_command =
    full_command =

    [server]

    [laptop]


Every section must match with a hostname machine.

Installation
------------

### Dependencies:

To install and run batterylevel, you'll need the following packages:

* python >= 3 (3.6.0 is recommended)

Optionally you may want to provide:

* beep If you want sound alerts.

You can choose between different installation methods.

### Classic method ###

- Build and install:

        $ make
        # make install

- Uninstall:

        # make uninstall


### Arch Linux package ###

- Build and install:

        $ make pkg
        # pacman -U snapman-*.pkg.xz

- Uninstall:

        # pacman -Rsc snapman


### Debian package ###

- Build and install:

        $ make deb
        # dpkg -i snapman_*.deb

- Uninstall:

        # apt purge snapman
