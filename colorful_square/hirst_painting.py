import colorgram
import turtle as turtle_module
import random

"""Extract colors from any image"""
# rgb_colors = []
# colors = colorgram.extract('E:\python_DS\colorful_square\image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_bucket = [ (225, 233, 227), (207, 161, 83), (55, 89, 131), (145, 91, 40), (139, 27, 48), (221, 206, 110), (133, 176, 201), (156, 47, 83), (46, 55, 103), (169, 159, 40), (128, 188, 143), (83, 20, 44), (37, 42, 68), (185, 94, 106), (186, 140, 170), (84, 125, 181), (59, 39, 31), (79, 153, 164), (88, 157, 91), (192, 79, 73), (161, 201, 219), (45, 74, 77), (80, 73, 43), (56, 129, 126), (217, 176, 187), (169, 207, 165), (220, 181, 168)]
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed('fastest')
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def draw_painting(num_of_dots):
    for dots in range(1, num_of_dots+1):
        tim.dot(20, random.choice(color_bucket))
        tim.forward(50)
        if dots%10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

draw_painting(100)
# for i in range(0,5):
#     tim.forward(50)
#     tim.dot(20, random.choice(color_bucket))

screen = turtle_module.Screen()
screen.exitonclick()
