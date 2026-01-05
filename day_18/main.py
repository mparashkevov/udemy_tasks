
from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
tim.color("OliveDrab2")

#Timmy the turtle will draw a square
def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

draw_square(tim)



screen = Screen()
screen.exitonclick()
