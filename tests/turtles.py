import time
import requests
import os
from cloudmesh.common.hostlist import Parameter
import turtle
from multiprocessing import Process



class Car(object):

    def __init__(self, id, name, ip, color, environment=None):
        self.car = turtle.Turtle()
        self.car.pencolor(color)
        self.name = name
        self.id = id
        self.ip = ip

        if environment is None:
            self.environment = "turtle"
            self.DT = 1000.0
        self.mode(environment)

    def place(self,x,y):
        self.car.penup()
        self.car.setx(x)
        self.car.sety(y)
        self.car.pendown()

    def mode(self, name):
        environment = name

    def distance(self, distance):
        self.DT = float(distance)

    def move(self, direction, unit):
        print (self.environment)

        if self.environment is "robot":
            if direction == 'left':
                payload = {'LEFT': 'ON'}
            elif direction == 'right':
                payload = {'RIGHT': 'ON'}
            elif  direction == 'stop':
                payload = {'STOP': 'ON'}
            elif direction == 'forward':
                print ("R forward")
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
        elif self.environment is  "turtle":
            if direction == 'left':
                self.car.left(unit)
            elif direction == 'right':
                self.car.right(unit)
            elif  direction == 'stop':
                pass
            elif direction == 'forward':
                print ("T forward")
                self.car.forward(int(self.DT*unit))
            elif direction == 'backward':
                self.car.forward(int(-1.0 * self.DT * unit))

            else:
                print ("ERROR: unkown direction:", direction)

    def dance(self, filename):
        filename="dance.txt"
        f = open(filename)
        self.lines = f.read().splitlines()
        f.close()
        print ("LINES", self.lines)

    def run(self):
        for line in self.lines:

            if "mode" in line:
                command, m = line.split()
                self.mode(m)
            elif "distance" in line:
                command, dt = line.split()
                self.distance(dt)
            elif "place" in line:
                command, x, y = line.split()
                self.place(float(x),float(y))

            elif "forward" in line or "backward" in line or "left" in line or "right in line":
                direction, duration = line.strip().split(' ')
                duration = float(duration)
                distance = self.DT * duration
                print ("<", direction, "><", duration, ">", sep='')
                self.move(direction,duration)
            else:
                pass

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

    def count(self):
        return len(self.ips)

    def name(self, id):
        return self.ips[id][0]

    def ip (self, id):
        return self.ips[id][1]

    def __str__(self):
        lines = []
        for i in range(0,self.count()):
            line = "Car {}: {} {}".format(i, self.ips[i][0], self.ips[i][1])
            lines.append(line)
        return '\n'.join(lines)

def names(ips):
    print (ips.keys())

if __name__ == "__main__":

    ips = [
        [1, '10.0.1.19'],
        [2, '10.0.1.20']
    ]

    cars = Cars(ips)
    print(cars)


    print ("KKKK")

    wn = turtle.Screen()        # creates a graphics window

    #def a():
    car = Car(0, cars.name(0), cars.ip(0), "blue")
    car.place(0,0)
    car.dance("dance.txt")
    car.mode("turtle")
    car.run()

    #def b():
    car = Car(1, cars.name(1), cars.ip(1), "green")
    car.place(100,100)
    car.dance("dance.txt")
    car.mode("turtle")
    car.run()

    #c1 = Process(target=a)
    #c2 = Process(target=b)

    #c1.start()
    #c2.start()

    #c1.join()
    #c2.join()

    wn.exitonclick()

