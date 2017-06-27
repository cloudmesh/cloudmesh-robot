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
        self.count = {
            'mobile': 0,
            'stationary' :0,
        }
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
            't': time.now()
            'id': self.id
        }
        self.count[kind] = self.count[kind] + 1
        self.id = self.id + 1

    def lookup(self, addr):
        for i in self.beacon:
            if self.beacon[i]['addr'] == addr:
                return self.beacon[i]
        return None

    def reset(self, kind):
        t = time.now()
        for name in self.beacon:
            if self.beacon[name]['kind'] == kind:
                self.set(0.0,0.0, t)

    def set(self, name, x, y, t=None):
        self.beacon[name]['x'] = x
        self.beacon[name]['y'] = y
        if t == None:
            self.beacon[name][t] = time.now()
        else:
            self.beacon[name][t] = t

    def info(self, dt=3.0, kind='mobile'):
        print ('Positioning System Information')
        print ('Stationary Beacons:', self.count['statinary'])
        print ('Mobile Beacons:    ', self.count['mobile'])
        # checks also if beacon was active and prints that
        data = dict(self.beacon)
        for name in data:
            # if time now - dt > time:
            data[name]['active'] = True
            #else
            # data[name]['active'] = False

        print(Printer.dict(positions.beacon, order=['id', 'name', 'kind', 'active', 'x', 'y', 'addr']))

        pass

    def count(self, kind='mobile'):
        return self.count[kind]

    def set_count(self, n, kind='mobile'):
        self.count[kind] = n

    def __str__(self):
        return Printer.dict(positions.beacon, order=['id', 'name', 'kind', 'x', 'y', 'addr'])

if __name__ == "__main__":

    positions = PositioningSystem()

    print (positions.tty)
    print (positions.beacon)


    positions.register("Hedge 1", "robi15")
    positions.register("Hedge 3", "robi16")

    print(positions.beacon)

    positions.export('g.txt')

    print(Printer.dict(positions.beacon, order=['id', 'name', 'kind', 'x', 'y', 'addr']))

    positions.info()


