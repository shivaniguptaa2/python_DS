from turtle import Turtle, Screen
import random

colors = ['rosy brown','dark magenta','light coral','gold','dark goldenrod','chocolate','deep pink','lime green',
          'pale green','turquoise','steel blue','chartreuse']
tim = Turtle()
tim.width(5)
tim.speed('fast')
for i in range(100):
    tim.color(random.choice(colors))
    tim.fd(15)
    angle = random.randrange(0,360,90)
    tim.right(angle)


























screen = Screen()
screen.exitonclick()