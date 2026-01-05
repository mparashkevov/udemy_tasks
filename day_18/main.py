from ctypes import sizeof
import turtle as t
from turtle import Screen, color
import random

t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#Timmy the turtle will draw a square
# def draw_square(turtle):
#     for _ in range(4):
#         turtle.forward(100)
#         turtle.right(90)

# draw_square(turtle)

# Tim will draw a dashed line
# def draw_dashed_line(turtle):
#     for _ in range(15):
#         turtle.forward(10)
#         turtle.penup()
#         turtle.forward(10)
#         turtle.pendown()

# draw_dashed_line(turtle)

# Tim will draw different shapes

COLOURS_LIST = ["DeepSkyBlue", "DarkOrchid", "Crimson", "Gold", "LimeGreen", "Tomato", "OrangeRed"]

# def draw_shapes(turtle):
#     for shape_side_n in range(3, 11):
#         angle = 360 / shape_side_n
#         for _ in range(shape_side_n):
#             turtle.forward(100)
#             turtle.right(angle)
#         turtle.color(random.choice(colours_list))

# draw_shapes(turtle)

# Tim will draw a random walk
# DIRECTIONS = [0, 90, 180, 270]
# SPEED = [1, 3, 6, 9, 10]

# def random_walk(turtle):
#     line_width = 1
    
#     for _ in range(200):
#         rgb_colors = random_color()
#         turtle.color(rgb_colors)
#         turtle.pensize(10)
#         turtle.setheading(random.choice(DIRECTIONS))
#         turtle.forward(30)
#         #turtle.speed(random.choice(SPEED))
#         turtle.speed("fastest")
#         #line_width += 1
    

def draw_spirograph(size_of_gap):
    for i in range(int(360 // size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(int(input("Enter the size of gap: ")))

screen = Screen()
screen.exitonclick()
