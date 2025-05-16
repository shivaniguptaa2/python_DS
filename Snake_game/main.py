from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor('Black')
screen.title('My Snake Game')
"""tracer function is to stop the animation"""
screen.tracer(0)
is_game_on = True

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while is_game_on:
    screen.update() 
    time.sleep(0.1)
        #this update function will show animation we are calling it here so once all of them are created then we can see
    snake.move_snake()






screen.exitonclick()