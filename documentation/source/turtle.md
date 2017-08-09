 # Trutle Graphics

## Demo

Python comes with a nice demonstartion program that allows you to learn some simple programming concepts while movin a turtle on the screen. It can be started with 

    python -m turtledemo

## Program example

You can also create programs with your favorite editor and run it. Let us put the following code into the program turtle.py. 

    import turtle

    window = turtle.Screen() 
    robot = turtle.Turtle()

    robot.forward(50)
    robot.right(90)     # Rotate clockwise by 90 degrees

    robot.forward(50)
    robot.right(90)

    robot.forward(50)
    robot.right(90)

    robot.forward(50)
    robot.right(90)

    turtle.done()

    window.mainloop()
    
After saving it you can run it from a terminal with 

	$ python turtle.py

## Shape

    shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”


turtle.register_shape(name, shape=None)

turtle.addshape(name, shape=None)

There are three different ways to call this function:

name is the name of a gif-file and shape is None: Install the corresponding image shape.


    screen.register_shape("turtle.gif")

Note: Image shapes do not rotate when turning the turtle, so they do not display the heading of the turtle!

name is an arbitrary string and shape is a tuple of pairs of coordinates: Install the corresponding polygon shape.


    screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))

name is an arbitrary string and shape is a (compound) Shape object: Install the corresponding compound shape.

Add a turtle shape to TurtleScreen’s shapelist. Only thusly registered shapes can be used by issuing the command shape(shapename).

## Links

* http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
* [https://docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html)

# Robot Dance Simulator

    cms robot dance dance.txt


# Scratch

* [Scratch](https://scratch.mit.edu/scratchr2/static/sa/Scratch-456.0.2.dmg)

# MBlock


* [MBlock](http://www.mblock.cc/download/)
