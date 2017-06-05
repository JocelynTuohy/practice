# Python Turtle Optional Assignment

# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
DIST = 100
COLOR = ["orange","yellow","green","purple","black"]
for x in range(0,6):
    # print "x", x
    turtle.pencolor(COLOR[x])
    for y in range(1,5):
        # print "y", y
        # turn the pointer 90 degrees to the right
        turtle.right(40)
        turtle.forward(50)
        turtle.left(35)
        turtle.backward(35)
        turtle.left(50)
        turtle.speed(1)
        # advance according to set distance
        turtle.forward(DIST)
        turtle.speed(0)
        turtle.circle(5)
    # add to set distance
    DIST += 20
