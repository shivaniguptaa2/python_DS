from turtle import Turtle
import random
COLORS = ['rosy brown','dark magenta','light coral','gold','dark goldenrod','chocolate','deep pink','lime green',
          'pale green','turquoise','steel blue','chartreuse']
MOV = 5
INC = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
    
    def create_cars(self):
        num = random.randint(1,6) 
        if num == 6:     
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            y_pos = random.randint(-190,220)
            new_car.color(random.choice(COLORS))
            new_car.goto(230,y_pos)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(MOV)

    def car_speed(self):
        self.new_spd = MOV + INC
        