from turtle import Turtle
from conf import HEIGHT

FONT_SIZE = 30


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.p1_score = 0
        self.p2_score = 0
        self.top = HEIGHT
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        text = f"{self.p1_score} | {self.p2_score}"
        self.goto(-int(len(text) / 2) * FONT_SIZE, int(self.top / 2) - FONT_SIZE - 10)
        self.write(text, False, font=("Courier", FONT_SIZE, "bold"))

    def update_score(self, player):
        if player == "player1":
            self.p1_score += 1
            self.update_scoreboard()
        elif player == "player2":
            self.p2_score += 1
            self.update_scoreboard()
