import time
import requests
import os
from cloudmesh.common.hostlist import Parameter
import turtle
from multiprocessing import Process

def expand(robots):
    r = Parameter.expand(robots)
    return r


class Car(object):

    def __init__(self, id, name, ip, color, environment=None):
        self.car = turtle.Turtle()
        self.car.pencolor(color)
        self.name = name
        self.id = id
        self.ip = ip
        self.last = turtle.pos()

        if environment is None:
            self.environment = "turtle"
            self.DT = 1000.0
        self.mode(environment)


    def place(self,x,y):
        self.car.penup()
        self.car.setx(x)
        self.car.sety(y)
        self.car.pendown()
        self.last = turtle.pos()


    def mode(self, name):
        self.environment = name

    def distance(self, distance):
        self.DT = float(distance)

    def move(self, direction, unit):

        if self.environment is "robot":
            if direction == 'left':
                payload = {'LEFT': 'ON'}
            elif direction == 'right':
                payload = {'RIGHT': 'ON'}
            elif  direction == 'stop':
                payload = {'STOP': 'ON'}
            elif direction == 'forward':
                payload = {'FORWARD': 'ON'}
            elif direction == 'backward':
                payload = {'BACK': 'ON'}
            else:
                print ("ERROR: unkown direction:", direction)

            try:
                headers = {'User-Agent': "Car"}
                r = requests.get('http://' + ip, headers=headers, params=payload)
            except Exception as e:
                print (type(e), e)
        elif self.environment == "turtle":
            turtle.setpos(self.last)
            if direction == 'left':
                self.car.left(unit)
            elif direction == 'right':
                self.car.right(unit)
            elif  direction == 'stop':
                pass
            elif direction == 'forward':
                self.car.forward(int(self.DT*unit))
            elif direction == 'backward':
                self.car.forward(int(-1.0 * self.DT * unit))

            else:
                print ("ERROR: unkown direction:", direction)
            #self.last = turtle.pos()



                #for ip in ips:
            # self.move(ip, direction)

            #time.sleep(duration)
            #for ip in ips:
            #   self.move(ip, "stop")

        # direction = "stop"
        # for ip in ips:
        #    self.move(ip, direction)


class Cars(object):

    def __init__(self, ips):
        self.ips = ips
        self.cars = []
        self.lines = None


    def mode(self, name):
        self.environment = name

    def count(self):
        return len(self.ips)

    def name(self, id):
        return self.ips[id][0]

    def ip (self, id):
        return self.ips[id][1]

    def distance(self, distance):
        self.DT = float(distance)

    def __str__(self):
        lines = []
        for i in range(0,self.count()):
            line = "# Car {}: {} {}".format(i, self.ips[i][0], self.ips[i][1])
            lines.append(line)
        return '\n'.join(lines)

    def read_dance(self, filename):
        f = open(filename)
        self.lines = f.read().splitlines()
        f.close()
        print ("# SCRIPT")
        for line in self.lines:
            print ("#    ", line)
        print ("# END SCRIPT")

    def add(self, car):
        self.cars.append(car)

    def run(self):
        for line in self.lines:
            print ("#", line)
            if line == "\n" or line.startswith("#"):
                pass
            else:
                v = line.split()

                if "mode" in line:
                    command, m, robots = line.split()
                    for r in expand(robots):
                        self.cars[int(r)].mode(m)
                elif "distance" in line:
                    command, dt, robots = line.split()
                    self.distance(dt)
                    for r in expand(robots):
                        self.cars[int(r)].distance(dt)

                elif "place" in line:
                    command, x, y, robots = line.split()
                    for r in expand(robots):
                        self.cars[int(r)].place(float(x),float(y))


                elif "forward" in line or "backward" in line or "left" in line or "right" in line:
                    direction, duration, robots = line.strip().split(' ')
                    duration = float(duration)
                    distance = self.DT * duration

                    for r in expand(robots):
                        print (" ",  direction,  duration, r)
                        self.cars[int(r)].move(direction,duration)
                else:
                    pass

#def names(ips):
#    print (ips.keys())

if __name__ == "__main__":

    ips = [
        [1, '10.0.1.19'],
        [2, '10.0.1.20'],
        [3, '10.0.1.21'],
    ]

    colors = ['blue', 'red', 'green', 'oragne', 'gray', 'brown', 'cyan', 'pink', 'purple', 'tomato']

    cars = Cars(ips)

    print(cars)

    wn = turtle.Screen()        # creates a graphics window

    #def a():
    for i in range(0,len(ips)):
        car = Car(i, "robi" + str(i), ips[i], colors[i])
        cars.add(car)

    cars.read_dance('dance.txt')

    cars.run()

    wn.exitonclick()

