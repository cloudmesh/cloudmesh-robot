from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.Shell import Shell, Brew, Pip
from cloudmesh.common.console import Console
from cloudmesh.common.error import Error
from cloudmesh.common.Printer import Printer
import os
import sys
from cloudmesh.robot.api import Probe, Git
from pprint import pprint
from ruamel import yaml
import json
import plistlib


class UsbCommand(PluginCommand):
    @command
    def do_usb(self, args, arguments):
        """
        ::

          Usage:
                usb list
                usb plist
                usb ioreg

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)

        if arguments.list:

            r = Shell.execute('system_profiler', 'SPUSBDataType')
            r = r.replace("\n\n", "\n")
            r = r.replace("        iBridge:", "      iBridge:")
            print(r)

            # d = yaml.load(r)

            # d = json.loads(r)

            # pprint(d)

        elif arguments.plist:

            r = Shell.execute('system_profiler', ["-xml", 'SPUSBDataType'])

            pprint(plistlib.loads(r))

        elif arguments.ioreg:

            # r = Shell.execute('ioreg', ["-p", "IOSUP", "-w0", "-l"])
            # r = Shell.execute('ioreg', ["-p", "IOSUP", "-w0", "-l"])

            r = Shell.execute("ioreg", ["-p", "IOUSB", "-b", "-n", "USB2.0-Serial"])
            print(r)

            print(r)

            # r = Shell.execute("ioreg",  ["-a", "-p", "IOUSB", "-w0", "-l", "-f"])
            # print(plistlib.loads(r))
