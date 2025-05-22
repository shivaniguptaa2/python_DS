from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.left(90)
        self.goto(0,-230)
    
    def move_up(self):
        self.fd(20)
        
    def reset_pos(self):
        # self.left(90)
        self.goto(0,-230)