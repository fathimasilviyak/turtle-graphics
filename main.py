# Import the class Turtle and Screen from turtle module,
# Screen represents the window on which the turtle going to show up
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

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

# Draw a square
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





def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color





# Create an object for the Screen class where the tutle will be shown
my_screen = Screen()

# Access the attribute of the screen object to show the screen and print screen height
print(my_screen.canvheight)

# Access the method of screen object to exit the window when the screen detects a click
my_screen.exitonclick()

# # Import another module heroes from pypi
# import heroes
# print(heroes.gen())



# Play with tuples
# my_tuple = (1, 2, 3)
# print(my_tuple[1])
# tuple_1 = (1,2,3)
# tuple_2 = (4,5,6)
# tuple_3 = tuple_1+tuple_2
# print(tuple_3)
# tuple_4 = list(tuple_2)
# print(tuple_4)
