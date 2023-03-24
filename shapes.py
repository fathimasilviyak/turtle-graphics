import turtle
import random

turtle.colormode(255)

flippy = turtle.Turtle()

colors = ["light sky blue", "red", "magenta", "yellow", "hot pink", "cyan", "blue", "green", "yellow green", "gold",
         "pink", "blue violet"]


def shape(num_sides):
    for i in range(num_sides):
        flippy.right(360 / num_sides)
        flippy.forward(100)

for i in range(3, 11):
    shape(i)
    flippy.color(random.choice(colors))


screen = turtle.Screen()
screen.exitonclick()