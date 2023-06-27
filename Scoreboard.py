from turtle import Turtle


class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 320)
        self.pendown()
        self.score1 = 0
        self.score2 = 0

    def score_display1(self, po1):
        self.score1 += 1
        self.setx(po1)
        self.clear()
        self.write(f"Score A:{self.score1} ", align="center", font=("arial", 12, "normal"))

    def score_display2(self, po2):
        self.score2 += 1
        self.setx(po2)
        self.clear()
        self.write(f" Score B:{self.score2}", align="center", font=("arial", 12, "normal"))
