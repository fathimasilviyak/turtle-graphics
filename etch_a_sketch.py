import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_left():
    tim.setheading(tim.heading()+10)


def move_right():
    tim.setheading(tim.heading()-10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# w = forward
# s = backward
# a = counter-clockwise
# d = clockwise
# c = clear drawing

screen.listen()
# When a key is pressed do something
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
