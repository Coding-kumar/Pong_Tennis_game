from turtle import Turtle


class Player(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")

        self.shapesize(5, 1)
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.showturtle()

    def move_up(self):
        c_y = self.ycor()
        if c_y <= 280:
            self.sety(c_y + 40)

    def move_down(self):
        c_y = self.ycor()
        if c_y >= -250:
            self.sety(c_y - 40)
