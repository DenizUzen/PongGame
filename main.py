from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.tracer(0)


rPaddle = Paddle(350, 0)
lPaddle = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(key="Up", fun=rPaddle.go_up)
screen.onkey(key="Down", fun=rPaddle.go_down)

screen.onkey(key="w", fun=lPaddle.go_up)
screen.onkey(key="s", fun=lPaddle.go_down)



isGameOn = True

while isGameOn:
    time.sleep(0.08)
    screen.update()
    ball.move()

    #Detect collision with bounds
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.xcor() > 320 and ball.distance(rPaddle) < 50:
        ball.bounce_x()

    if ball.xcor() < -320 and ball.distance(lPaddle) < 50:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.resetposition()
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.resetposition()
        scoreboard.r_point()

screen.exitonclick()