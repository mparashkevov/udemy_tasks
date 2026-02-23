from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.moving_up = False
        self.moving_down = False

    def start_up(self):
        self.moving_up = True

    def start_down(self):
        self.moving_down = True

    def stop_up(self):
        self.moving_up = False

    def stop_down(self):
        self.moving_down = False

    def move(self):
        if self.moving_up:
            self.goto(self.xcor(), self.ycor() + 20)
        if self.moving_down:
            self.goto(self.xcor(), self.ycor() - 20)