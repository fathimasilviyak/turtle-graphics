import turtle as t
import random

t.colormode(255)

flippy = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


def spirograph(size_of_gap):
    flippy.speed("fastest")
    for i in range(int(360 / size_of_gap)):
        flippy.color(random_color())
        flippy.circle(100)
        flippy.setheading(flippy.heading() + size_of_gap)


spirograph(5)

screen = t.Screen()
screen.exitonclick()