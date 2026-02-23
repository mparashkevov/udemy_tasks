from turtle import Screen, Turtle

class GameScreen:

    def __init__(self):
        self.display = Screen()
        self.display.bgcolor("black")
        self.display.title("P O N G")
        self.display.setup(width=800, height=600)
        self.display.tracer(0)
        
        # Start Screen Menu
        self.start_text = Turtle()
        self.start_text.color("white")
        self.start_text.penup()
        self.start_text.hideturtle()
        self.start_text.goto(0, 0)
        self.start_text.write("Press SPACE to Start", align="center", font=("Courier", 40, "normal"))

    def clear_start_text(self):
        self.start_text.clear()

    def bind_keys(self, r_paddle, l_paddle, start_game_func):
        self.display.listen()
        self.display.onkeypress(r_paddle.start_up, "Up")
        self.display.onkeyrelease(r_paddle.stop_up, "Up")
        self.display.onkeypress(r_paddle.start_down, "Down")
        self.display.onkeyrelease(r_paddle.stop_down, "Down")

        self.display.onkeypress(l_paddle.start_up, "w")
        self.display.onkeyrelease(l_paddle.stop_up, "w")
        self.display.onkeypress(l_paddle.start_down, "s")
        self.display.onkeyrelease(l_paddle.stop_down, "s")
        
        self.display.onkeypress(start_game_func, "space")

    def update(self):
        self.display.update()

    def exitonclick(self):
        self.display.exitonclick()

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
