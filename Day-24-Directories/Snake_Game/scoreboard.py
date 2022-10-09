from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        with open("high_score.txt") as highscore_file:
            self.high_score = highscore_file.read()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High-Score: {self.high_score}", align=ALIGNMENT, move=False, font=FONT)

    def add_point(self):
        self.score += 1

        self.update_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score.txt", mode="w") as highscore_file:
                highscore_file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
