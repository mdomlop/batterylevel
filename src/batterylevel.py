#!/usr/bin/env python3
"""
Batterylevel
============

Watchs battery levels and performs some actions.

AUTHORS: Manuel Domínguez López. See AUTHORS file.

LICENSE: GPLv3+. Read LICENSE file.

Version: 0.3a 2017.01.18

Depends: beep pcspkr

"""

import sys
import os
import argparse
import configparser

PROGRAM_NAME = "BatteryLevel"
EXECUTABLE_NAME = "batterylevel"
DESCRIPTION = "Reads battery values, performs some actions and plays some sound alerts."
VERSION = "0.4.1a"
AUTHOR = "Manuel Domínguez López"  # See AUTHORS file
MAIL = "mdomlop@gmail.com"
SOURCE = "https://github.com/mdomlop/batterylevel"
LICENSE = "GPLv3+"  # Read LICENSE file.

COPYRIGHT = '''
Copyright: 2017 Manuel Domínguez López <mdomlop@gmail.com>
License: GPL-3.0+

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 .
 This package is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 .
 You should have received a copy of the GNU General Public License
 along with this program. If not, see <https://www.gnu.org/licenses/>.
 .
 On Debian systems, the complete text of the GNU General
 Public License version 3 can be found in "/usr/share/common-licenses/GPL-3".
'''

class Battery:
    pass


def version():
    print('''
BatteryLevel version 0.2a
Copyright (c) 2017  Manuel Domínguez López

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. See the file LICENSE for details.
''')


def loadconfig(cfile='/etc/batterylevel.ini'):
    global config
    config = configparser.ConfigParser()
    config['DEFAULT'] = {  # Hardcoding default settings values:
            'name': 'BAT0',
            'forced': 'False',

            'alarm_level': '10',
            'warning_level': '25',
            'info_level': '40',
            'safe_level': '90',
            'full_level': 'Full',

            'alarm_sound':
            'beep -f3000 -l100 -r3 -D100 -n -f2000 -l100 -r3 -D100',
            'warning_sound': 'beep -f3000 -r3 -D1000',
            'info_sound': 'beep -f100 -l50 -r2',
            'safe_sound': 'beep -f9000',
            'full_sound': 'beep -f9000 -r3',

            'alarm_command': 'systemctl poweroff',
            'warning_command': 'sync',
            'info_command': '',
            'safe_command': '',
            'full_command': ''
            }
    config.read(cfile)
    battery.cfile = cfile  # For debug


def set_settings():
    if settings.name:
        battery.name = settings.name
    else:
        battery.name = 'DEFAULT'

    if settings.cfile:
        loadconfig(settings.cfile)
        battery.cfile = settings.cfile  # For debug

    if battery.name not in config:
        print('No config for', battery.name)
        exit(2)

    info = {}
    battery.bfile = os.path.join('/sys/class/power_supply',
                                 config[battery.name]['name'], 'uevent')

    if os.path.isfile(battery.bfile):
        f = open(battery.bfile, "r")

        for i in f.readlines():
            (k, v) = i.split('=')
            info[k.strip()] = v.strip()
        f.close()

        ''' Set only relevant and common values '''
        battery.status = info['POWER_SUPPLY_STATUS']
        battery.present = int(info['POWER_SUPPLY_PRESENT'])
        battery.capacity = int(info['POWER_SUPPLY_CAPACITY'])
    else:
        if settings.verbose:
            print('Battery not found:', config[battery.name]['name'])
        exit(0)

    if settings.alarm_level:
        battery.alarm_level = settings.alarm_level
    else:
        battery.alarm_level = config[battery.name].getint('alarm_level')
    if settings.warning_level:
        battery.warning_level = settings.warning_level
    else:
        battery.warning_level = config[battery.name].getint('warning_level')
    if settings.info_level:
        battery.info_level = settings.info_level
    else:
        battery.info_level = config[battery.name].getint('info_level')
    if settings.safe_level:
        battery.safe_level = settings.safe_level
    else:
        battery.safe_level = config[battery.name].getint('safe_level')

    battery.full_level = config[battery.name]['full_level']

    battery.alarm_sound = config[battery.name]['alarm_sound']
    battery.warning_sound = config[battery.name]['warning_sound']
    battery.info_sound = config[battery.name]['info_sound']
    battery.safe_sound = config[battery.name]['safe_sound']
    battery.full_sound = config[battery.name]['full_sound']

    battery.alarm_command = config[battery.name]['alarm_command']
    battery.warning_command = config[battery.name]['warning_command']
    battery.info_command = config[battery.name]['info_command']
    battery.safe_command = config[battery.name]['safe_command']
    battery.full_command = config[battery.name]['full_command']
    battery.forced = config[battery.name].getboolean('forced')


def debug():
    print(
            '\n',
            'cfile:', battery.cfile, '\n',
            'Config Section:', battery.name, '\n',
            'name:', config[battery.name]['name'], '\n',
            'status', battery.status, '\n',
            'present', battery.present, '\n',
            'capacity', battery.capacity, '\n',
            'alarm_level', battery.alarm_level, '\n',
            'warning_level', battery.warning_level, '\n',
            'info_level', battery.info_level, '\n',
            'safe_level', battery.safe_level, '\n',
            'full_level', battery.full_level, '\n',
            'alarm_sound', battery.alarm_sound, '\n',
            'warning_sound', battery.warning_sound, '\n',
            'info_sound', battery.info_sound, '\n',
            'safe_sound', battery.safe_sound, '\n',
            'full_sound', battery.full_sound, '\n',
            'alarm_command', battery.alarm_command, '\n',
            'warning_command', battery.warning_command, '\n',
            'info_command', battery.info_command, '\n',
            'safe_command', battery.safe_command, '\n',
            'full_command', battery.full_command, '\n',
            'forced', battery.forced
            )


def parseargs():
    ''' Load settings from commandline.
    Overwrite values in Battery() '''
    global settings

    parser = argparse.ArgumentParser(
            prog='Batterylevel',
            description='Performs some actions based on battery level'
            )

    parser.add_argument('-n', '--name')
    parser.add_argument('-c', '--cfile')

    parser.add_argument('-a', '--alarm_level', type=int)
    parser.add_argument('-w', '--warning_level', type=int)
    parser.add_argument('-i', '--info_level', type=int)
    parser.add_argument('-s', '--safe_level', type=int)
    parser.add_argument('-f', '--full_level')

    parser.add_argument('-m', '--manager', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--version', action='store_true')

    parser.add_argument('--force', action='store_true')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('-d', '--daemon', type=int)

    settings = parser.parse_args()


def sound(cmd):
    test_beeper()
    os.system(cmd)


def actions():
    if battery.present == 1:
        if settings.verbose or not settings.manager:
            print('Battery is present: ' + config[battery.name]['name'])
            print('Capacity: ' + str(battery.capacity))
    else:
        if settings.verbose or not settings.manager:
            print('Battery is not present: ' + battery.name)
        exit(0)

    if battery.status == 'Discharging':
        if settings.verbose or not settings.manager:
            print('Status: discharging')
        if battery.capacity < battery.alarm_level:
            if settings.verbose or not settings.manager:
                print('Battery capacity is less than alarm level: ' +
                      str(battery.alarm_level))
            print('Alarm: Battery level too low!')
            if settings.manager:
                sound(battery.alarm_sound)
                if not settings.debug:
                    os.system(battery.alarm_command)
        elif battery.capacity < battery.warning_level:
            if settings.verbose or not settings.manager:
                print('Battery capacity is less than warning level: ' +
                      str(battery.warning_level))
            print('Warning: Battery level reaches the warning state')
            print('Connect the AC or the system will halt soon.')
            if settings.manager:
                sound(battery.warning_sound)
                if battery.warning_command:
                    os.system(battery.warning_command)
        elif battery.capacity < battery.info_level:
            if settings.verbose or not settings.manager:
                print('Battery capacity is less than info level: ' +
                      str(battery.info_level))
            print('Info: Battery low. Please connect the system to a AC.')
            if settings.manager:
                sound(battery.info_sound)
                if battery.info_command:
                    os.system(battery.info_command)
    elif battery.status == 'Charging':
        if settings.verbose or not settings.manager:
            print('Status: charging')
        if battery.capacity > battery.safe_level:
            if settings.verbose or not settings.manager:
                print('Battery capacity is more than safe level: ' +
                      str(battery.safe_level))
            print('Battery almost full. Please disconnect the system from AC.')
            if settings.manager:
                sound(battery.safe_sound)
                if battery.safe_command:
                    os.system(battery.safe_command)
        elif battery.capacity > 100:  # Yes. It is posible.
            if settings.verbose or not settings.manager:
                print('Battery capacity is over 100 %: ' +
                      str(battery.capacity))
            print('Battery almost full. Disconnect the system from AC.')
            if settings.manager:
                sound(battery.full_sound)
                if battery.full_command:
                    os.system(battery.full_command)
    elif battery.status == battery.full_level:
        print('Battery full. Please disconnect AC right now!')
        if settings.manager:
            sound(battery.full_sound)
            if battery.full_command:
                os.system(battery.full_command)
    else:
        print('UNKNOWN STATUS: ' + battery.status + 'PLEASE DEBUG!',
              file=sys.stderr)
        exit(4)


def test_beeper():
    ''' Test if pcspkr driver for beeper is loaded.
    Needed for sound alarms '''
    loaded = False
    module = 'pcspkr'
    f = open('/proc/modules', "r")
    for i in f.readlines():
        if i.startswith(module + ' '):
            loaded = True
            return
    f.close()

    if not loaded:
        if settings.force:
            ''' Will not effectively load the module. This is not a bug because
            one will want to force execution even if module fails. '''
            print('Forced module load:', module)
            os.system('modprobe pcspkr')
            battery.forced = True
        else:
            print('Sorry', module, 'not loaded. No sound alarm will output.')
            exit(3)  # Not exit if forced and NOT loaded


def main():
    global battery
    battery = Battery()

    parseargs()
    loadconfig()
    set_settings()

    if settings.debug:
        print('\nCommadline Settings:\n')
        print(settings)
        print('\nBattery information:')
        debug()
    if settings.version:
        version()
        exit(0)

    actions()

    if settings.manager and battery.forced:
        os.system('rmmod pcspkr')

    return 0


if __name__ == '__main__':
    main()
