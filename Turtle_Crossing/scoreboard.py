from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color('white')
        self.goto(-300,220)
        self.hideturtle()
        self.add_level()
    
    def add_level(self):
        self.level+=1
        self.clear()
        self.write(f'Level : {self.level}', align=ALIGNMENT, font= FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align=ALIGNMENT, font= FONT)