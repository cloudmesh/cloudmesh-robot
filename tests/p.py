import sys
import time
# import requests
from pprint import pprint
from cloudmesh.common.Printer import Printer
import random
import time


class ggg(object):

    def __init__(self):
        self.g = {}

class BeaconSimulator(object):

    def get (addr):
        x = random.random() * 100.0
        y = random.random() * 100.0
        return (addr, x, y, time.now())

class PositioningSystem(object):

    def __init__(self):
        print("hallo")



a = ggg()
print (a.g)

b = PositioningSystem()

#print (b.tty)

'''

        self._tty = tty
        self.beacon = {}
        self.id = 0

    def status(self):
        # x,y
        pass

    # TODO: implement
    def export(self, filename):
        # file open or with statment
        for name in self.beacon:
            for element in ['name', 'x', 'y']:
                print (name,)
                print (x,)
                print (y)
                # change this at one point so it prints this to a file
                # close file

    def register(self, addr, name, kind='mobile'):
        self.beacon[name] = {
            'name': name,
            'kind': kind,
            'addr': addr,
            'x': x,
            'y': y,
            'id': self.id
        }
        self.id = self.id + 1

    def lookup(self, addr):
        for i in self.beacon:
            if self.beacon[i]['addr'] == addr:
                return self.beacon[i]
        return None

    def reset(self):
        # set all positions to some vale within the fixedbecona
        pass

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

    def probe (selfid):
        # similar to get but with more info get just gives xy
        pass

positions = PositioningSystem()

print (positions.tty)
print (positions.beacon)

positions.register("Hedge 1", "robi15")
positions.register("Hedge 3", "robi16")

print(positions.beacon)

print(Printer.dict(positions.beacon, order=['id', 'name', 'kind', 'x', 'y', 'addr']))

#
'''