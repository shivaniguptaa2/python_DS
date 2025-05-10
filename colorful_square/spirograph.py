# from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.pensize(5)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

for i in range(40):
    tim.color(random_colors())
    tim.circle(100)
    poc = tim.heading()
    tim.setheading(poc+10)




screen = t.Screen()
screen.exitonclick()