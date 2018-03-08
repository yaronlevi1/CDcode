# try this either as a .py file or in the python shell
import turtle
import random
# the distance we want the pointer to travel each time
DIST = 10
for x in range(6):
    for y in range(5):
        # turn the pointer 90 degrees to the right
        turtle.right(random.uniform(0, 360))
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
        DIST += 5