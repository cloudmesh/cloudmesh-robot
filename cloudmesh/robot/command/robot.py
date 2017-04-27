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
from cloudmesh.robot.api import Probe, Git
from pprint import pprint

class RobotCommand(PluginCommand):

    class ampy(object):


        def __init__(self, port=None):

            self.port = port

        def ls(self, path):
            self._execute("ls", path)

        def rm(self, path):
            self._execute("rm", path)

        def rmdir(self, path):
            self._execute("rmdir", path)

        def put(self, src, dest=None):
            return self._execute_src_dest("put", src, dest)

        def get(self, src, dest=None):
            return self._execute_src_dest("get", src, dest)

        def _execute_src_dest(self, cmd, src, dest=None):
            if dest is None:
                return Shell.execute('ampy', ['--port', self.port, cmd, src])
            else:
                return Shell.execute('ampy', ['--port', self.port, cmd, src, dest])

        def _execute(self, cmd, src):
            return Shell.execute('ampy', ['--port', self.port, cmd, src])


    @command
    def do_robot(self, args, arguments):
        """
        ::

          Usage:
                robot osx install
                robot image fetch
                robot probe [--format=FORMAT]
                robot flash erase [--dryrun]
                robot flash python [--dryrun]
                robot set PORT
                robot put PATH
                robot get PATH
                robot rm PATH
                robot rmdir PATH
                robot ls PATH
                
                
          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        pprint(arguments)

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

        if arguments.flash and arguments.erase:

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

            for package in ["esptool", "pyserial", "adafruit-ampy"]:
                print("installing", package)
                Pip.install(package)


            if sys.platform == 'darwin':
                if Shell.command_exists("brew"):
                   pass
                else:
                    os.system(
                        '/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

                for package in ["lua", "picocom"]:
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