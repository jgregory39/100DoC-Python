# import colorgram
#
# colors = colorgram.extract('hirst_original.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
color_list = [(244, 235, 46), (196, 12, 34), (221, 159, 69),
              (43, 80, 178), (238, 39, 143), (40, 215, 68), (238, 229, 5), (30, 40, 154), (23, 147, 26), (207, 74, 22),
              (202, 34, 91), (186, 16, 9), (19, 18, 42), (216, 141, 191), (57, 15, 10), (88, 8, 28), (227, 161, 9),
              (78, 212, 157), (67, 73, 221), (13, 95, 61), (78, 194, 225), (239, 158, 215), (94, 233, 204),
              (220, 76, 48),
              (15, 67, 46), (7, 226, 238)]

hirst = t.Turtle()
screen = t.Screen()

hirst.speed(0)
hirst.pu()
hirst.setpos(-225.0, -225.0)

for row in range(10):
    for _ in range(10):
        hirst.dot(20, random.choice(color_list))
        hirst.forward(50)
    hirst.setheading(90)
    hirst.forward(50)
    hirst.setheading(0)
    hirst.back(500)

hirst.hideturtle()
screen.exitonclick()