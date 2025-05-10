from turtle import Turtle, Screen

tim = Turtle()
kim = Turtle()
tim.shape('turtle')
tim.color('purple')
angle = 45

"""Dashed line"""
def dashed_line():
    for i in range(15):
        tim.fd(10)
        tim.penup()
        tim.fd(10)
        tim.pendown()

"""Square with Turtle"""
def square():
    for i in range(4):
        tim.fd(100)
        tim.right(90)

square()





screen = Screen()
screen.exitonclick()