import glob
import os
from subprocess import Popen, PIPE
from pprint import pprint
import sys
import requests

class Git(object):
    '''
    curl - i
    https://api.github.com/repos/roboedu/esp8266/git/trees/4e725210660730319241866a46a31b1c953dcccf?recursive=1
    '''

    def tree(self, url=None, prefix=None):

        if url is None:
            url = "https://api.github.com/repos/roboedu/esp8266/git/trees/4e725210660730319241866a46a31b1c953dcccf?recursive=1"

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
        os.system ("mkdir -p ~/.cloudmesh/roboedu/images")
        for f in self.files:
            os.system("cd ~/.cloudmesh/roboedu/images; wget https://github.com/roboedu/esp8266/raw/master/" + f)

class Probe(object):
    # !/usr/bin/env python

    def _run(self, command):
        command_list = command.split(" ")
        p = Popen(command_list, stdout=PIPE)
        poutput = p.stdout.readlines()
        output = [o.strip() for o in poutput]
        return output

    def __init__(self):
        tty = glob.glob("/dev/tty.wchusbserial*")

        if len(tty) > 1:
            print("ERROR: more than one tty found")
            print (tty)
            sys.exit(1)
        elif len(tty) == 0:
            print("ERROR: no tty found")
            sys.exit(1)
        self.tty = tty[0]


    def probe(self):

        id = self._run("esptool.py -p " + self.tty + " chip_id")
        mac = self._run("esptool.py -p " + self.tty + " read_mac")

        data = {
            "tty": self.tty,
            "chipid": str(id[2]).replace("Chip ID:", "").strip(),
            "mac": str(mac[2]).replace("MAC:", "").strip(),
        }
        return data


#p = Probe()

#data = p.probe(tty)
#pprint(data)
