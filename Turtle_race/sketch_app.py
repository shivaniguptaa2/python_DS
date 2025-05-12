from turtle import Turtle, Screen

tim = Turtle()
tim.penup()
tim.setheading(250)
tim.forward(300)
tim.setheading(0)
tim.pendown()
tim.speed('fastest')
screen = Screen()


def move_forward():
    tim.fd(20)

def move_backward():
    tim.backward(20)

def move_right():
    tim.right(90)

def move_left():
    tim.right(90)

def right_tilt():
    tim.right(45)

def left_tilt():
    tim.right(45)

def draw_circle():
    tim.circle(50)

def draw_semi():
    tim.circle(120,180)


screen.listen()
screen.onkey(key='W',fun=move_forward)
screen.onkey(key='D', fun=move_backward)
# screen.onkey(key='A', fun=move_right)
screen.onkey(key='X', fun=move_left)
screen.onkey(key='I', fun=left_tilt)
# screen.onkey(key='J', fun=right_tilt)
screen.onkey(key='L', fun=draw_circle)
screen.onkey(key='M', fun=draw_semi)
screen.exitonclick()