from turtle import Turtle,Screen
import random

# screen = Screen()
# screen.tracer()
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.speed('fastest')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.refresh()
    
    def refresh(self):
        pos_x = random.randint(-280,280)
        pos_y = random.randint(-280,280)
        self.goto(pos_x,pos_y)
