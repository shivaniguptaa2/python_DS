from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor('Black')
screen.title('My Snake Game')
"""tracer function is to stop the animation"""
screen.tracer(0)
is_game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while is_game_on:
    screen.update() #this update function will show animation we are calling it here so once all of them are created then we can see
    time.sleep(0.1)
    snake.move_snake()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_game_on = False
        scoreboard.game_over()

    # detect collision with own tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # using python slicing to avoid this code
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()