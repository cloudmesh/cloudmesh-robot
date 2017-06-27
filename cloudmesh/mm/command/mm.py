from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.Shell import Shell, Brew, Pip
from cloudmesh.common.console import Console
from cloudmesh.common.error import Error
from cloudmesh.common.Printer import Printer
from cloudmesh.common.util import yn_choice, path_expand
import os
import sys
from cloudmesh.robot.api import Probe, Git, Network, Ampy
from pprint import pprint
import textwrap
from cloudmesh.common.hostlist import Parameter
from cloudmesh.common.StopWatch import StopWatch
from ruamel import yaml

class MmCommand(PluginCommand):

# characters from towel.blinkenlights.nl


    @command
    def do_mm(self, args, arguments):
        """
        ::
    
          Usage:
                mm [--tty=TTY]
    
          Options:
              --tty=TTY    the usb device for mm. [default: /dev/ABC].

        """

        print(arguments)

        print("mm command")
