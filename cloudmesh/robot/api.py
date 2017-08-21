import glob
import os
from subprocess import Popen, PIPE
from pprint import pprint
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import path_expand
import sys
import requests
from cloudmesh.common.console import Console


class Ampy(object):
    def __init__(self, port=None):
        self.port = port

    def ls(self, path=None):
        if path is None:
            path = "/"
        return self._execute("ls", path)

    def rm(self, path):
        self._execute("rm", path)

    def rmdir(self, path):
        self._execute("rmdir", path)

    def mkdir(self, path):
        self._execute("mkdir", path)

    def put(self, src, dest=None, optimize=False):
        if optimize:
            print("optimize")
            data = {
                'src': src,
                'dest': dest,
                'opt': src + '-opt'
            }
            command = "pyminifier -o {opt} {src}".format(**data)
            os.system(command)
            src = data['opt']
            dest = os.path.basename(src.replace('-opt', ''))
        else:
            print("normal")
        if dest is None:
            dest = os.path.basename(src)

        print(src, '->', dest)

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


class Git(object):
    '''
    curl - i
    https://library.github.com/repos/roboedu/esp8266/git/trees/4e725210660730319241866a46a31b1c953dcccf?recursive=1
    '''

    def tree(self, url=None, prefix=None):

        if url is None:
            url = "https://library.github.com/repos/roboedu/esp8266/git/trees/4e725210660730319241866a46a31b1c953dcccf?recursive=1"

        r = requests.get(url)
        d = r.json()

        self.files = []
        for element in d['tree']:
            path = element['path']
            if prefix is not None:
                if path.startswith(prefix):
                    self.files.append(path)
            else:
                self.files.append(path)
        return self.files

    def dict(self, prefix=None):

        r = {}
        i = 0
        for e in self.files:
            if prefix is None:
                r[str(i)] = {
                    "id": str(i),
                    "image": e}
            else:
                r[str(i)] = {
                    "id": str(i),
                    "image": e.replace(prefix, "")}
            i = i + 1
        return r

    def fetch(self):
        self.tree(prefix="images/")
        os.system("mkdir -p ~/.cloudmesh/roboedu/images")
        for f in self.files:
            os.system("cd ~/.cloudmesh/roboedu/images; wget https://github.com/roboedu/esp8266/raw/master/" + f)


class ProbeException(Exception):
    pass


class Probe(object):
    # !/usr/bin/env python

    def _run(self, command):
        command_list = command.split(" ")
        p = Popen(command_list, stdout=PIPE)
        poutput = p.stdout.readlines()
        output = [o.strip() for o in poutput]
        return output

    def __init__(self):
        tty = glob.glob("/dev/tty.SLAB_USBtoUART") + glob.glob("/dev/tty.wchusbserial*")

        if len(tty) > 1:
            Console.error("ERROR: more than one tty found")
            print("TTY:", tty)
            # raise  ProbeException("ERROR: tty not found")
            sys.exit(1)
        elif len(tty) == 0:
            # raise  ProbeException("ERROR: tty not found")
            Console.error("ERROR: no tty found")
            sys.exit(1)
        self.tty = tty[0]

    def probe(self):

        id = self._run("esptool.py -p " + self.tty + " chip_id")
        mac = self._run("esptool.py -p " + self.tty + " read_mac")

        for i in range(0, len(id)):
            if id[i].startswith(b'Chip ID:'):
                found_id = id[i]
                break

        for i in range(0, len(mac)):
            if mac[i].startswith(b'MAC:'):
                found_mac = mac[i]
                break

        data = {
            "tty": self.tty,
            "chipid": str(found_id.decode('ascii')).replace("Chip ID:", "").strip(),
            "mac": str(found_mac.decode('ascii')).replace("MAC:", "").strip(),
        }
        return data


class Network(object):
    def __init__(self, ssid=None, username=None, password=None):
        self.filename = path_expand("~/.cloudmesh/robot/credentials.txt")
        Shell.mkdir(path_expand("~/.cloudmesh/robot"))
        self.credentials = {
            'ssid': ssid,
            'username': username,
            'password': password,
        }
        with open(self.filename, 'w') as f:
            for e in self.credentials:
                f.write(e + ": " + self.credentials[e] + "\n")

    def __str__(self):
        with open(self.filename, 'r') as f:
            contents = f.read()

        print(contents)

# p = Probe()

# data = p.probe(tty)
# pprint(data)
