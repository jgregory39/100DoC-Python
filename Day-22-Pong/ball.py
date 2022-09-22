from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed = 10
        self.y_mirror = 1
        self.x_mirror = 1

    def move(self):
        new_x = self.xcor() + self.speed * self.x_mirror
        new_y = self.ycor() + self.speed * self.y_mirror
        self.goto((new_x, new_y))

    def inc_speed(self):
        self.speed += 1

    def reset(self):
        self.speed = 10
        self.goto(0, 0)
        self.paddle_bounce()

    def wall_bounce(self):
        self.y_mirror *= -1

    def paddle_bounce(self):
        self.x_mirror *= -1
