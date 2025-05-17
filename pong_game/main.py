from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
RIGHT_PD = 475
LEFT_PD = -480

screen = Screen()
screen.setup(width = 1000, height= 600)
screen.bgcolor('Black')
screen.title('PinG PonG Game')
screen.tracer(0)

paddle_r = Paddle(RIGHT_PD)
paddle_l = Paddle(LEFT_PD)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.up,"Up")
screen.onkey(paddle_r.down,"Down")
screen.onkey(paddle_l.up, "a")
screen.onkey(paddle_l.down, "z")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(paddle_l) < 40 and ball.xcor()<-440 or ball.distance(paddle_r) < 40 and ball.xcor()>440:
        ball.bounce_x()

    #detect if R Paddle miss
    if ball.xcor()>490:
        ball.reset_position()
        scoreboard.l_score_update()

    #detect if L Paddle miss
    if ball.xcor()<-490:
        ball.reset_position()
        scoreboard.r_score_update()

screen.exitonclick()