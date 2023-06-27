from turtle import Turtle


class LineMan(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.pencolor("red")
        self.pensize(10)
        self.penup()
        self.goto(0, -330)
        self.pendown()
        self.goto(0, 350)
        self.penup()
        self.hideturtle()
