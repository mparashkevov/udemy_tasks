from turtle import Turtle, Screen
import time

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 40, "normal")
screen = Screen()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT , font=FONT)    

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.game_over_text()

    def flash_game_over(self):
        for _ in range(50):   # number of flashes
            self.clear()
            self.color("red")
            self.goto(0, 260)
            self.game_over_text()
            screen.update()
            time.sleep(0.2)

            self.clear()
            self.color("white")
            self.goto(0, 260)
            self.game_over_text()
            screen.update()
            time.sleep(0.2)

    def game_reset(self):
        self.score = 0
        self.update_scoreboard()

    def game_over_text(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)