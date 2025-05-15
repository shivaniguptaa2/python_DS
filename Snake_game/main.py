from turtle import Turtle, Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor('Black')
screen.title('My Snake Game')

square_positions = [(0,0),(-20,0),(-40,0)]
for positions in square_positions:
    segment = Turtle('square')
    segment.color('white')
    segment.goto(positions)












screen.exitonclick()