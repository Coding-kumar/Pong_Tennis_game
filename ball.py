from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(1)
        self.goto(0, 0)
        self.xmove = 10
        self.ymove = 10

    def ball_move(self):
        self.showturtle()
        self.setposition(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def ball_ybounce(self):
        self.ymove *= -1

    def ball_xbounce(self):
        self.xmove *= -1
