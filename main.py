# Creating a Ping Pong Game
from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
l_paddle = Paddles((-350, 0))
r_paddle = Paddles((350, 0))

ball = Ball()
score = Scoreboard()
"""Assigning keyboard control to each Paddle"""
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    """Detecting collision with wall"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    """Detecting collision with Paddle"""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    """Detecting if Ball doesn't hit R Paddle"""
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    """Detecting if Ball doesn't hit L Paddle"""
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
