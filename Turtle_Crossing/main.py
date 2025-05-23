from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(700,500)
screen.bgcolor('black')
screen.tracer(0)

line = Turtle()
line.pencolor('white')
line.penup()
line.goto(-330,-210)
for i in range(50):
    line.pendown()
    line.fd(10)
    line.penup()
    line.fd(10)

player = Player()
car = CarManager()
level = Scoreboard()
screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.reset_pos,"Down")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    # detect collision with cars
    for car_instance in car.all_cars:
        if player.distance(car_instance)<20 :
            is_game_on = False
            level.game_over()
    
    #completion of levels
    if player.ycor()>230:
        player.reset_pos()
        level.add_level()
        car.car_speed()

screen.exitonclick()