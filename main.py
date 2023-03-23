# Import the class Turtle and Screen from turtle module,
# Screen represents the window on which the turtle going to show up
from turtle import Turtle, Screen
import random

# Import module using alias
# import turtle as t

# Create an object for Turtle class
flippy = Turtle()
print(flippy)

# Make a turtle shape
flippy.shape("turtle")

# Change turtle color
flippy.color("chartreuse")

# Move the tutle forward by 100 place
# flippy.forward(100)

## Draw a square
# for i in range(4):
#     flippy.forward(100)
#     flippy.right(90)

# Move turtle to the origin
# flippy.home()

# Move turtle in other direction and draw lines
# flippy.fd(100)
# flippy.rt(90)
# flippy.penup()
# flippy.fd(100)
# flippy.rt(90)
# flippy.pendown()
# flippy.fd(100)
# flippy.rt(90)
# flippy.penup()
# flippy.fd(100)
# flippy.pendown()


# Draw a dashed line
# for i in range(15):
#     flippy.forward(10)
#     flippy.penup()
#     flippy.forward(10)
#     flippy.pendown()

colors = ["light sky blue", "red", "magenta", "yellow", "hot pink", "cyan", "blue", "green", "yellow green", "gold",
          "pink", "blue violet"]

# draw different shapes with different colors
def shape(num_sides):
    for i in range(num_sides):
        flippy.right(360 / num_sides)
        flippy.forward(100)


for i in range(3,11):
    shape(i)
    flippy.color(random.choice(colors))

# Create an object for the Screen class where the tutle will be shown
my_screen = Screen()

# Access the attribute of the screen object to show the screen and print screen height
print(my_screen.canvheight)

# Access the method of screen object to exit the window when the screen detects a click
my_screen.exitonclick()


# # Import another module heroes from pypi
# import heroes
# print(heroes.gen())
