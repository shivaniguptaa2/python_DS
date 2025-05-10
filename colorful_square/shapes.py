from turtle import Turtle, Screen
import random

tim = Turtle()
kim = Turtle()
tim.shape('turtle')
colors = ['red','pink','green','purple','orange','brown','blue','peru','cyan','dark magenta']

def draw_shape(length):
    angle = 360/length
    for i in range(length):
        tim.fd(100)
        tim.right(angle)

for shapes_side in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shapes_side)


"""Dashed line"""
def dashed_line():
    for i in range(15):
        tim.fd(10)
        tim.penup()
        tim.fd(10)
        tim.pendown()

def triangle():
    for i in range(3):
        tim.fd(100)
        tim.right(120)

"""Square with Turtle"""
def square():
    for i in range(4):
        tim.fd(100)
        tim.right(90)

def pentagon():
    for i in range(5):
        tim.fd(100)
        tim.right(72)

def hexagon():
    for i in range(6):
        tim.fd(100)
        tim.right(60)

def heptagon():
    for i in range(7):
        tim.fd(100)
        tim.right(51.43)

def octagon():
    for i in range(8):
        tim.fd(100)
        tim.right(45)


# draw_shape(3,120) #triangle
# draw_shape(4,90) #square
# draw_shape(5,72) #pentagon
# draw_shape(6,60) #hexagon
# draw_shape(7,51.43) #heptagon
# draw_shape(8,45) #octagon

















screen = Screen()
screen.exitonclick()