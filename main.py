from turtle import Screen
from Scoreboard import ScoreCard
from line import LineMan
from outterwall import OutLine
from player import Player
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.listen()
score1 = ScoreCard()
score2 = ScoreCard()
line = LineMan()
outline = OutLine()
POS1=(-500, 0)
POS2=(500, 0)
player_one = Player(POS1)
player_two = Player(POS2)
ball = Ball()

screen.setup(1100, 660)
screen.bgcolor("black")
screen.title("Pong Game")
screen.onkey(player_two.move_up, "Up")
screen.onkey(player_two.move_down, "Down")
screen.onkey(player_one.move_up, "w")
screen.onkey(player_one.move_down, "s")
score1_x = -50
score2_x = 50

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()
    if ball.ycor() > 320 or ball.ycor() < -300:
        ball.ball_ybounce()

    if ball.xcor() > 450 and ball.distance(player_two) < 50 or ball.xcor() < -450 and ball.distance(player_one) < 50:
        ball.ball_xbounce()

    if ball.xcor() > 530:
        score1.score_display1(score1_x)
        ball.setposition(0, 0)
    elif ball.xcor() < -530:
        score2.score_display2(score2_x)
        ball.setposition(0, 0)

screen.exitonclick()
