from turtle import Turtle
from settings import ALIGNMENT, SCORE_FONT, GAME_OVER_FONT, HEIGHT


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.top = HEIGHT
        self.text = f"Score = {self.score}"
        self.goto(-int(len(self.text) / 2), int(self.top / 2) - 25)
        self.update_scoreboard()

    def game_over(self):
        self.goto(-5, 0)
        self.color("red")
        self.write("GAME OVER!", False, align=ALIGNMENT, font=GAME_OVER_FONT)

    def update_scoreboard(self):
        self.text = f"Score = {self.score}"
        self.write(self.text, False, align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        # print(f"Score increased to {self.text}")
