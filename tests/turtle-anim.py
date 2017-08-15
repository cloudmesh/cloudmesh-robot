from threading import Thread
import random
from gturtle import *

class TurtleAnimator(Thread):
    def __init__(self, turtle):
        Thread.__init__(self)
        self.t = turtle

    def run(self):
        while True:
            self.t.forward(150 * random.random())
            self.t.left(-180 + 360 * random.random())

tf = TurtleFrame()
john = Turtle(tf)
john.wrap()
laura = Turtle(tf)
laura.setColor("red")
laura.setPenColor("red")
laura.wrap()
thread1 = TurtleAnimator(john)
thread2 = TurtleAnimator(laura)
thread1.start() 
thread2.start()
