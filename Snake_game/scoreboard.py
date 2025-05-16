from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')

class Scoreboard(Turtle):
     def __init__(self):
          super().__init__()
          self.score = 0
          self.color('white')
          self.goto(0,260)
          self.hideturtle()
          self.add_score()
     
     def add_score(self):
          self.score+=1
          self.clear()
          self.write(f'Score : {self.score}', align=ALIGNMENT, font= FONT)
     
     def game_over(self):
          self.goto(0,0)
          self.write(f'GAME OVER', align=ALIGNMENT, font= FONT)
          