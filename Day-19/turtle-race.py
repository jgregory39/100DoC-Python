from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(rainbow[i])
    new_turtle.goto(x=-230, y=-125 + i * 50)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
