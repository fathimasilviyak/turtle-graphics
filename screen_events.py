import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    tim.forward(10)


screen.listen()
# When a key is pressed do something
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()