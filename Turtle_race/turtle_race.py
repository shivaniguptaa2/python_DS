from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
is_race_on = False
# print(user_bet)
colors = ['red','blue','pink','orange','green','purple']
y_pos = [-70,-40,-10,20,50,80]
all_turtles = []
for num in range(0,6):
    new_turtle = Turtle(shape='turtle')  
    new_turtle.penup()
    new_turtle.goto(-230,y_pos[num])
    new_turtle.color(colors[num])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title = 'Make your bet', prompt='Which turtle will win the race? Choose a color: ')

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f'You have Won!! The {wining_color} turtle is winner.')
            else:
                print(f'You have lost!! The {wining_color} turtle is winner.')

        rand_move = random.randint(0,10)
        turtle.fd(rand_move) 








screen.exitonclick()