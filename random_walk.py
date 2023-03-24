import turtle
import turtle as t
import random

t.colormode(255)

flippy = turtle.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color

directions = [0, 90, 180, 270]
flippy.width(15)
flippy.speed("fastest")

for i in range(200):
    flippy.color(random_color())
    flippy.forward(30)
    flippy.setheading(random.choice(directions))

screen = turtle.Screen()
screen.exitonclick()