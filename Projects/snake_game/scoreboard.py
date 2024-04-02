from turtle import Turtle

FONT = ("courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(
            f"Score : {self.score} High Score : {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )
        self.hideturtle()

    def update_scorebaord(self):
        self.clear()
        self.write(
            f"Score : {self.score} High Score : {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scorebaord()

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_scorebaord()
