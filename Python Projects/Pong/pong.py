from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen= Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()
ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game =True

while(game):
    time.sleep(0.1)
    screen.update()
    ball.move()

    if(ball.ycor()>280 or ball.ycor()<-280):
        ball.bounce()

    if(ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.hit()

    if(ball.xcor()>380):
        ball.reset_pos()
        scoreboard.lpoint()
        time.sleep(1.5)

    if(ball.xcor()<-380):
        ball.reset_pos()
        scoreboard.rpoint()
        time.sleep(1.5)

screen.exitonclick()