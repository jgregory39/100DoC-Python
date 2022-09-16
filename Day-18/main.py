import turtle as t
import random

tim = t.Turtle()
# tim.shape("turtle")
# tim.color("#ffff00", "#a000ff")
t.colormode(255)
screen = t.Screen()
# screen.bgcolor("#1590a6")

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


def draw_shape(num_sides):
    angle = 360.0 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def draw_shape_onion(max_sides):
    for num_sides in range(3, max_sides + 1):
        tim.pencolor(random_color())
        draw_shape(num_sides)


def random_walk(duration):
    tim.width(15)
    tim.speed(0)
    for _ in range(duration):
        heading = random.choice([0, 90, 180, 270])
        tim.pencolor(random_color())
        tim.setheading(heading)
        tim.forward(50)


def draw_spirograph(radius, count):
    angle = 360.0 / count
    for _ in range(count):
        tim.pencolor(random_color())
        tim.circle(radius)
        tim.left(angle)


tim.speed(0)
draw_spirograph(100, 100)


screen.exitonclick()


