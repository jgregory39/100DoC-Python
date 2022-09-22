from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect Paddle collision
    if ball.xcor() > 320 or ball.xcor() < -320:
        if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
            ball.paddle_bounce()
            ball.inc_speed()
        elif ball.xcor() > 380:
            scoreboard.score_left()
            ball.reset()
        elif ball.xcor() < -380:
            scoreboard.score_right()
            ball.reset()

screen.exitonclick()
