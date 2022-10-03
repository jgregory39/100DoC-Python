from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)

        self.score = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", align='left', font=FONT)

    def inc_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
