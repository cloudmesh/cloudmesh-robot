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

class RobotCommand(PluginCommand):

# characters from towel.blinkenlights.nl


    class Banner(object):

        @classmethod
        def show(cls):

            banner = textwrap.dedent("""
                +-----------------------------------+
                |                        /~\        |                  
                | Power us on!          |oo )       |
                |                       _\=/_       |                  
                |       ___            /  _  \      |                  
                |      /() \          |||/.\|||     |                  
                |    _|_____|_        || \_/ ||     |                  
                |   | | === | |       # |\ /| #     |                  
                |   |_|  O  |_|         \_ _/       |                  
                |    ||  O  ||          | | |       |                  
                |    ||__*__||          | | |       |                  
                |   |~ \___/ ~|         []|[]       |                  
                |   /=\ /=\ /=\         | | |       |                   
                +___[_]_[_]_[_]________/_]_[_\______+
                |          cloudmesh.robot          |
                +------------------------------------
                """)
            return banner



    @command
    def do_robot(self, args, arguments):
        """
        ::

          Usage:
                robot welcome
                robot osx install
                robot image fetch
                robot probe [--format=FORMAT]
                robot flash erase [--dryrun]
                robot flash python [--dryrun]
                robot test
                robot run PROGRAM
                robot credentials set SSID USERNAME PASSWORD
                robot credentials put
                robot credentials list
                robot login
                robot set PORT NOT IMPLEMENTED
                robot ls [PATH]
                robot put SOURCE [DESTINATION]
                robot get PATH
                robot rm PATH
                robot rmdir PATH
                
          This command does some useful things.

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

            p = Probe()
            Console.error("If you do not see a >>> please press the reset button.")
            os.system("picocom --imap lfcrlf -b 115200 " + p.tty)

        elif arguments.flash and arguments.erase:

            p = Probe()
            print (p.tty)
            print ("Please press the right buttons")

            _continue("continue?")
            command = "esptool.py --port {} erase_flash".format(p.tty)
            _run(command)

        elif arguments.flash and arguments.python:

            p = Probe()
            print (p.tty)
            print ("Please press the right buttons")

            _continue("continue?")

            d = {
                "baud": str(9600*6),
                "dir": ".",
                "image": "esp8266-20170108-v1.8.7.bin",
                "port": p.tty}

            command = "esptool.py --port {port} --baud {baud} write_flash --flash_size=detect -fm dio 0x00000 {image}".format(**d)
            _run(command)
            #"esptool.py --port /dev/tty.wchusbserial1410 --baud 9600 write_flash --flash_size=detect -fm dio 0x00000 esp8266-20170108-v1.8.7.bin"

        elif arguments.osx and arguments.install:

            o = sys.platform

            print (o)

            if sys.platform == 'darwin':
                if Shell.command_exists("brew"):
                   pass
                else:
                    os.system(
                        '/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

                for package in ["lua", "picocom", "wget"]:
                    print("installing", package)
                    Brew.install(package)

            if sys.platform == 'linux':
                Console.error("Linux not yet supported. Install lua and picocom.")
            return ""

        elif arguments.probe:

            output_format = arguments["--format"] or "table"
            try:
                p = Probe()
                d = p.probe()
                print (Printer.attribute(d, output=output_format))

            except Exception as e:

                Error.traceback(error=e, debug=True, trace=True)

            return ""

        elif arguments.image and arguments.fetch:

            try:

                if os.path.isfile("esp8266-20170108-v1.8.7.bin"):
                    print ("... image already downloaded")
                else:
                    os.system("wget http://micropython.org/resources/firmware/esp8266-20170108-v1.8.7.bin")

                #g = Git()
                #r = g.fetch()

            except Exception as e:

                Error.traceback(error=e, debug=True, trace=True)

            return ""

        elif arguments.run:

            p = Probe()
            d = {
                "port": p.tty,
                "program": arguments.PROGRAM
            }
            os.system("ampy --port {port} run {program}".format(**d))

        elif arguments.test:

            p = Probe()
            d = {"port": p.tty}
            test = textwrap.dedent("""
            n=3
            print('Count to', n)
            for i in range(1, n+1):
                print(i)
            """)
            with open("test.py", "w") as f:
                f.write(test)
            os.system("ampy --port {port} run test.py".format(**d))

        elif arguments.credentials and arguments.set:
            try:
                net = Network(ssid=arguments.SSID,
                              username=arguments.USERNAME,
                              password=arguments.PASSWORD)

                #print (net)
            except Exception as e:
                Error.traceback(e)

        elif arguments.credentials and arguments.put:
            try:
                filename = path_expand("~/.cloudmesh/robot/credentials.txt")
                p = Probe()
                #   print (p.tty)
                ampy = Ampy(p.tty)

                ampy.put(filename, "credentials.txt")
            except Exception as e:
                Error.traceback(e)

        elif arguments.credentials and arguments.list:
            try:
                p = Probe()
                ampy = Ampy(p.tty)
                filename = path_expand("~/.cloudmesh/robot/credentials.txt.robot")
                ampy.get("credentials.txt", filename)
                r = Shell.cat(filename)
                print (r)
                os.remove(filename)
            except Exception as e:
                Error.traceback(e)

        elif arguments.ls:
            try:
                p = Probe()
                ampy = Ampy(p.tty)
                r = ampy.ls()
                print (r)
            except Exception as e:
                Error.traceback(e)

        elif arguments.put:
            try:
                p = Probe()
                ampy = Ampy(p.tty)
                ampy.put(arguments.SOURCE, arguments.DESTINATION)
            except Exception as e:
                Error.traceback(e)

        elif arguments.rm:
            try:
                p = Probe()
                ampy = Ampy(p.tty)
                ampy.rm(arguments.PATH)
            except Exception as e:
                Error.traceback(e)

        elif arguments.rmdir:
            try:
                p = Probe()
                ampy = Ampy(p.tty)
                ampy.rmdir(arguments.PATH)
            except Exception as e:
                Error.traceback(e)

        elif arguments.mkdir:
            try:
                p = Probe()
                ampy = Ampy(p.tty)
                ampy.mkdir(arguments.PATH)
            except Exception as e:
                Error.traceback(e)

        '''
        elif arguments.image and arguments.list:

            try:
                prefix = 'images/'

                #link= "https://github.com/roboedu/esp8266/blob/master/images/esp8266-20170108-v1.8.7.bin"

                #os.system("wget " + link)

                g = Git()
                d = g.tree(prefix=prefix)
                r = g.dict(prefix=prefix)

                print (Printer.dict(r, order=["id", "image"]))
                #pprint (r)
            except Exception as e:

                Error.traceback(error=e, debug=True, trace=True)
            return ""

        '''