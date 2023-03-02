from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.write(f"Level : {self.level}", align="center", font=("Times New Roman", 20, "normal"))

    # def game_over(self):
    #     self.write(f"GAME OVER", align="center", font=("Times New Roman", 20, "normal"))


    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()
