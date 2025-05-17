from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 40, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score_update()
   
    def score_update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, font= FONT)
        self.goto(100,200)
        self.write(self.r_score, font= FONT)
    
    def l_score_update(self):
        self.l_score+=1
        self.score_update()
    
    def r_score_update(self):
        self.r_score+=1
        self.score_update()