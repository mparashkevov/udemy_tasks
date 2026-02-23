from turtle import Screen, Turtle

class GameScreen:

    def __init__(self):
        self.display = Screen()
        self.display.bgcolor("black")
        self.display.title("P O N G")
        self.display.setup(width=800, height=600)
        self.display.tracer(0)

        # Draw the net
    def draw_net(self):
        net = Turtle()
        net.color("white")
        net.penup()
        net.hideturtle()
        net.goto(0, -300)
        net.setheading(90)
        net.pensize(3)
        for _ in range(30):
            net.pendown()
            net.forward(10)
            net.penup()
            net.forward(10)
