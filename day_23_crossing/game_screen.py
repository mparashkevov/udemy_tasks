from turtle import Screen, Turtle

class GameScreen:

    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.title("Turtle Crossing")
        self.screen.setup(width=600, height=800)
        self.screen.tracer(0)

        # Precreate a turtle for endgame text
        self._game_over_writer = Turtle()
        self._game_over_writer.hideturtle()
        self._game_over_writer.color("white")

        # HUD writers for lives and level
        self._lives_writer = Turtle()
        self._lives_writer.hideturtle()
        self._lives_writer.color("white")
        self._lives_writer.penup()
        self._lives_writer.goto(170, 360)

        self._level_writer = Turtle()
        self._level_writer.hideturtle()
        self._level_writer.color("white")
        self._level_writer.penup()
        self._level_writer.goto(-170, 360)

    def draw_lanes(self, lane_height=40):
        painter = Turtle()
        painter.hideturtle()
        painter.penup()
        painter.speed(0)

        # Start just below the start line and repeat 3 road lanes + 1 grass lane until the finish line
        pattern = ["road", "road", "road", "grass"]
        colors = {"road": "#444444", "grass": "#0b6b0b"}
        current_y = 330  # leave a small gap below the start line at y=350
        finish_y = -350

        while current_y - lane_height >= finish_y:
            lane_type = pattern[0]
            pattern = pattern[1:] + [lane_type]
            fill_color = colors[lane_type]

            painter.goto(-300, current_y)
            painter.setheading(0)
            painter.fillcolor(fill_color)
            painter.pencolor(fill_color)
            painter.pendown()
            painter.begin_fill()
            painter.forward(600)
            painter.right(90)
            painter.forward(lane_height)
            painter.right(90)
            painter.forward(600)
            painter.right(90)
            painter.forward(lane_height)
            painter.end_fill()
            painter.penup()

            current_y -= lane_height

    def update(self):
        self.screen.update()
    def exitonclick(self):
        self.screen.exitonclick()

    def game_over(self):
        self._game_over_writer.clear()
        self._game_over_writer.penup()
        self._game_over_writer.goto(0, 0)
        self._game_over_writer.write("GAME OVER", align="center", font=("Courier", 48, "bold"))

    def update_hud(self, level: int, lives: int):
        self._lives_writer.clear()
        self._level_writer.clear()
        self._lives_writer.write(f"Lives: {lives}", align="left", font=("Courier", 16, "bold"))
        self._level_writer.write(f"Level: {level}", align="left", font=("Courier", 16, "bold"))

    # Draw the start line
    def draw_start_line(self):
        line = Turtle()
        line.color("white")
        line.penup()
        line.hideturtle()
        line.goto(-300, 350)
        line.setheading(0)
        line.pensize(5)
        for _ in range(30):
            line.pendown()
            line.forward(20)
            line.penup()
            line.forward(20)
    
    # Draw the finish line (bottom, below the last lane)
    def draw_finish_line(self):
        line = Turtle()
        line.color("white")
        line.penup()
        line.hideturtle()
        line.goto(-300, -370)
        line.setheading(0)
        line.pensize(5)
        for _ in range(30):
            line.pendown()
            line.forward(20)
            line.penup()
            line.forward(20)

    
