# from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.pensize(2)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

def draw_spirogarph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() +size_of_gap)
z
draw_spirogarph(5)



screen = t.Screen()
screen.exitonclick()