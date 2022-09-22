from turtle import Turtle
FONT = ('Courier', 48, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 220)
        self.write(f"{self.l_score}\t{self.r_score}", align='center', font=FONT)

    def score_right(self):
        self.r_score += 1
        self.update_score()

    def score_left(self):
        self.l_score += 1
        self.update_score()
