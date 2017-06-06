import turtle
import threading

window = turtle.Screen()



class myTurtle (threading.Thread):
    def __init__(self,x,y):
        threading.Thread.__init__(self)
        self.noel = turtle.Turtle()
        self.x = x
        self.y = y
        
    def run(self):
        self.noel.penup()
        self.noel.setx(self.x)
        self.noel.sety(self.y)
        self.noel.pendown()
        self.noel.forward(100)
        self.noel.left(90)
        self.noel.forward(100)
        self.noel.left(90)
        self.noel.forward(100)
        self.noel.left(90)
        self.noel.forward(100)


t1 = myTurtle(0,0)
t2 = myTurtle(200,200)

t1.start()
t2.start()


window.exitonclick()
