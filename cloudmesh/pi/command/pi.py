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
from pprint import pprint
import textwrap
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.StopWatch import StopWatch
from ruamel import yaml

pi_image= """echo \"$(tput setaf 2)
   .~~.   .~~.
  '. \ ' ' / .'$(tput setaf 1)
   .~ .~~~..~.
  : .~.'~'.~. :
 ~ (   ) (   ) ~
( : '~'.~.'~' : )
 ~ .~ (   ) ~. ~
  (  : '~' :  ) $(tput sgr0)Raspberry Pi$(tput setaf 1)
   '~ .~~~. ~'\"
"""

banner = textwrap.dedent("""
       .~~.   .~~.
       '. \ ' ' / .'
        .~ .~~~..~.
       : .~.'~'.~. :
      ~ (   ) (   ) ~
     ( : '~'.~.'~' : )
      ~ .~ (   ) ~. ~
       (  : '~' :  ) 
        '~ .~~~. ~'
            '~'
        Raspberry Pi
    """)


class PiCommand(PluginCommand):

# characters from towel.blinkenlights.nl


    class Banner(object):

        @classmethod
        def show(cls):
            os.system(pi_image)
            #return banner
            return ""


    @command
    def do_pi(self, args, arguments):
        """
        ::

          Usage:
                pi welcome
                pi image fetch
                pi sd probe [--format=FORMAT]
                pi sd flash [--dryrun] NAME
                pi sd backup
                pi login NAME
                PI reboot NAME

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file
        """

        # pprint(arguments)

        # "wget http://micropython.org/resources/firmware/esp8266-20170108-v1.8.7.bin"

        arguments.dryrun = arguments["--dryrun"]

        def _run(command):
            print (command)
            if arguments.dryrun:
                print(command)
            else:
                os.system(command)

        def _continue(msg):
            if not arguments.dryrun:
                c = yn_choice(msg, default='y')

        if arguments.welcome:

            print(self.Banner.show())

        elif arguments.login:

            pass

        elif arguments.flash:

            pass


            # _continue("continue?")
            # command = "esptool.py --port {} erase_flash".format(p.tty)
            # _run(command)


        elif arguments.reboot:

            pass

        elif arguments.image and arguments.fetch:

            url = "https://downloads.raspberrypi.org/NOOBS_latest"

            if os.path.isfile("NOOBS_latest"):
                print("... image already downloaded")
            else:
                os.system("wget " + url)


            pass

