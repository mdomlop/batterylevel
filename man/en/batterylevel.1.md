batterylevel(1) -- Performs some actions based on battery levels
================================================================

## SINOPSIS

`batterylevel` [*OPTION*...]

## DESCRIPCTION


`batterylevel` reads battery information from /sys filesystem and performs some
actions based on it.

When `batterylevel` is executed without options it will read the config file in
`/etc/batterylevel.ini` and will print text advices to stdout. It also plays
some sounds through beep speaker if the necessary module (pcspkr) are avaible.
Is posible to set a specific command for custom actions in configuration file.
By default custom actions are poweroff the system for alarm status and sync for
warning status.

If there are not a configuration file the program will catch the default options
hardcoded in source. Commandline options will overwrite the precedent values.

Read batterylevel(5) for futher information.

There are some configuration files avaibles in
`/usr/share/batterylevel/examples`. Adapt whatever of they to your system needs
if you pretend it more easy.


`batterylevel` is primarily thinked to be periodically executed by itself (not
implemented yet) o by another agent like cron or a systemd timer.


## PERIODICALLY EXECUTION WITH SYSTEMD

The developer source provides a service and a timer for systemd but the is
disabled by default. You will start and enable it. Read `systemd.timer(5)` for
futher information.


## PERIODICALLY EXECUTION WITH CRON

Not covered in this manual page. Please read `crontab(5)`


## PERIODICALLY EXECUTION IN DAEMON MODE *(Not implemented yet)*

Provided by commandlne option `-d` or `--daemon`.
See more in [OPCIONES] section.


## OPTIONS

There are the avaible commandlne options:

**Warning:** *Not fully implemented yet*.

* `-c`, `--cfile`=[<file>]:
    Indicates what *file* will be used as configuration instead of
    predeterminated `/etc/batterylevel.ini`. The program will get values from
    it. Please `batterylevel.ini(5)` for additional information.

* `-n`, `--name`=[<name>]:
    Indicates name of the section to use from configuration. Not Indicates the
    name of the battery. This is inside of section configuration as:
    CONFIGURATION.INI->[SECTION-NAME]->NAME=BATX

* `-a`, `--alarm_level`=[<int>]:
    Set a custom integer number instead of the established in configuration file
    or the hardcoded one. When the system are not connected to AC and the
    battery capacity is lower than it, the alarm sound will be played, a text
    adverteance will print out to standard output and the system will poweroff.

* `-w`, `--warning_level`=[<int>]:
    Set a custom integer number instead of the established in configuration file
    or the hardcoded one. When the system are not connected to AC and the
    battery capacity is lower than it, the warning sound will be played and a
    text adverteance will print out to standard output.

* `-i`, `--info_level`=[<int>]:
    Set a custom integer number instead of the established in configuration file
    or the hardcoded one. When the system are not connected to AC and the
    battery capacity is lower than it, the info sound will be played and a
    text adverteance will print out to standard output.

* `--force`:
    Forces adding required pcspkr module to the linux kernel if it is not
    already loaded into the system.

    This option has not short option equivalent.

* `-v`, `--verbose`:
    Print out some additional info about battery status and charge.

    This option has not short option equivalent.

* `--version`:
    Print out information about version of the program and exit.

* `--debug`:
    Indicates debug mode for print more info suitable for debug proposites.

    This option has not short option equivalent.

* `-d`, `--daemon`=[<time>]: ***Not implemented yet***
    Starts `batterylevel`  in daemon mode (system service). The *time* value is
    required for indicate the periodicity in seconds for executing the program.


## RETURN VALUE
BatteryLevel exit code indicates whether it was able  to  successfully  perform
the requested operation, and if not, what kind of error occurred.

* 0:
    Successful termination. Or there is a battery but its prestent state is `0`.

* 1:
    Not adecuated power supply with the indicated name in settings,
    configuration file or hardcoded.

* 2:
    No section found with this name in settings, configuration file or
    hardcoded.

* 3:
    No module (pcspkr) load. Since it is needed for play sounds the program will
    exits unless `--force` option was present.

* 4:
    Battery with unknown status.


## FILES
`/etc/batterylevel.ini`
    Configuration file. Stores default configuration.
`/etc/systemd/system/batterylevel.service`
    Systemd service. It will be periodically executed by `batterylevel.timer`.
`/etc/systemd/system/batterylevel.timer`
    Systemd timer. It will periodically execute `batterylevel.service`.


## AUTOR

This manual page was writed by the original author of the program. Manuel
Domínguez López mdomlop@gmail.com.


## BUGS
Please if you found one, let me know.


## REPORTING BUGS
Report bugs to <mdomlop@gmail.com>


## COPYRIGHT
GPLv3


## SEE ALSO

batterylevel.ini(5) systemd(1) systemd.service(5) systemd.timer(5) beep(1)

