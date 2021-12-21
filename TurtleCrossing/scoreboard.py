from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.goto(-280, 260)
        self.text = f"Level: {self.level}"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.text, font=FONT)

    def increase_score(self):
        self.level += 1
        self.text = f"Level: {self.level}"
        self.update_scoreboard()

    def game_over(self):
        self.text = "GAME OVER"
        self.goto(-70, 0)
        self.update_scoreboard()
