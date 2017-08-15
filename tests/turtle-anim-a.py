import turtle

screen = turtle.Screen() 
screen.register_shape("robi.gif")


robot = turtle.Turtle()


# turtle.shape("robi.gif")
turtle.shape("turtle")

robot.forward(50)
robot.right(90)     # Rotate clockwise by 90 degrees

robot.forward(50)
robot.right(90)

robot.forward(50)
robot.right(90)

robot.forward(50)
robot.right(90)

screen.exitonclick()

