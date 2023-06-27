from turtle import Turtle


class OutLine(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.pencolor("white")
        self.pensize(10)
        self.penup()
        self.goto(-550, -330)
        self.pendown()
        self.goto(-550, 350)
        self.goto(550, 350)
        self.goto(550, -330)
        self.goto(-550, -330)
        self.penup()
