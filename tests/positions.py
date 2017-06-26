import sys
import time
# import requests
from pprint import pprint
from cloudmesh.common.Printer import Printer
import random
import time
#
# BUG marvelmind can not be found
#
# from marvelmindcoordinates import MarvelmindHedge

class BeaconSimulator():

    def get (addr):
        x = random.random() * 100.0
        y = random.random() * 100.0
        return (addr, x, y, time.now())

class PositioningSystem(object):

    def __init__(self, tty='/dev/tty.usbmodemFD121'):
        self.tty = tty
        self.beacon = {}
        self.id = 0
#       self.sensors =  MarvelmindHedge(self.tty)

    def pos(self, name):
        return self.beacon[name]['x'],self.beacon[name]['y']
        pass

    def export(self, filename):
        with open(filename, "w") as f:
            for name in self.beacon:
                element = "{name}, {x}, {y}".format(**self.beacon[name])
                f.write(element)
                f.write("\n")

    def update(self):
        pass

    def register(self, addr, name, kind='mobile'):
        self.beacon[name] = {
            'name': name,
            'kind': kind,
            'addr': addr,
            'x': 0.0,
            'y': 0.0,
            'id': self.id
        }
        self.id = self.id + 1

    def lookup(self, addr):
        for i in self.beacon:
            if self.beacon[i]['addr'] == addr:
                return self.beacon[i]
        return None

    def reset(self):
        for name in self.beacon:
            self.beacon[name]['x'] = 0.0
            self.beacon[name]['y'] = 0.0

    def info(self, kind='mobile'):
        # mobile, all, stationarty
        pass

        # dependent on type returns info about the beacons
        # not sure how to implement yet

    def count(self, type='mobile'):
        # retusn number of beacons found
        pass

    def set_count(self, type='mobile'):
        # instead of probing the beacons hard code the set count
        # so we can figure out if we have power issue
        pass


positions = PositioningSystem()

print (positions.tty)
print (positions.beacon)

positions.register("Hedge 1", "robi15")
positions.register("Hedge 3", "robi16")

print(positions.beacon)

positions.export('g.txt')

print(Printer.dict(positions.beacon, order=['id', 'name', 'kind', 'x', 'y', 'addr']))



sys.exit(0)


"""
# assume start at 0 0
move 0 1
move 1 1
move 5 5
"""


# def move(ip, direction, epsilon=0.0001):
#    if direction == 'left':
#        payload = {'LEFT': 'ON'}
#    elif direction == 'right':
#        payload = {'RIGHT': 'ON'}
#    elif  direction == 'stop':
#        payload = {'STOP': 'ON'}
#    elif direction == 'forward':
#        payload = {'FORWARD': 'ON'}
#    elif direction == 'backward':
#        payload = {'BACK': 'ON'}
#    else:
#        print ("ERROR: unkown direction:", direction)
#    try:
#        headers = {'User-Agent': "Car"}
#        r = requests.get('http://' + ip, headers=headers, params=payload)
#    except Exception as e:
#        print (type(e), e)
