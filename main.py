# Import the class Turtle and Screen from turtle module,
# Screen represents the window on which the turtle going to show up
from turtle import Turtle, Screen

# Create an object for Turtle class
flippy = Turtle()
print(flippy)

# Make a turtle shape
flippy.shape("turtle")

# Change turtle color
flippy.color("chartreuse")

# Move the tutle forward by 100 place
flippy.forward(100)

# Draw a rectangle
for i in range(4):
    flippy.forward(50)
    flippy.right(90)


# Move turtle to the origin
flippy.home()

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

# Create an object for the Screen class where the tutle will be shown
my_screen = Screen()

# Access the attribute of the screen object to show the screen and print screen height
print(my_screen.canvheight)

# Access the method of screen object to exit the window when the screen detects a click
my_screen.exitonclick()

