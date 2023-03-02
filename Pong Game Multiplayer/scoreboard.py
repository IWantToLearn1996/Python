from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.update_score()


    def update_score(self):
        self.write(f"Score {self.score_left} : {self.score_right}", align="center", font=("Times New Roman", 20, "normal"))

    def increase_score_left(self):
        self.score_left += 1
        self.clear()
        self.update_score()

    def increase_score_right(self):
        self.score_right += 1
        self.clear()
        self.update_score()