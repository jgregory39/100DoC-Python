from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()


def move_forward():
    etch.forward(10)


def move_backward():
    etch.back(10)


def turn_right():
    etch.right(15)


def turn_left():
    etch.left(15)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=etch.reset)
screen.exitonclick()
