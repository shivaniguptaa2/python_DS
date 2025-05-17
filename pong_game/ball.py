from turtle import Turtle
import random
random_x = random.randint(-490,490)
random_y = random.randint(-300,300)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.move_speed = 0.1
        # self.goto(random_x,random_y)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1
