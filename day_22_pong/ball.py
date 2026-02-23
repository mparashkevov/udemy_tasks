from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self, starting_speed=0.1):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        # Allow caller to control initial and reset speed
        self.starting_speed = starting_speed
        self.move_speed = starting_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self, paddle_y=None):
        self.x_move *= -1
        
        # Dynamic bounce angle based on where it hit the paddle
        if paddle_y is not None:
            difference = self.ycor() - paddle_y
            # If it hits the top of the paddle, increase upward speed
            # If it hits the bottom, increase downward speed
            self.y_move = difference / 5

        # Cap the maximum speed so the game remains playable
        if self.move_speed > 0.01:
            self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = self.starting_speed
        self.bounce_x()