import time
from turtle import Turtle, Screen
import random

# -------------------- Constants -------------------- #
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BG_COLOR = "black"
SNAKE_COLOR = "white"
FOOD_COLOR = "red"
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# -------------------- Snake Class -------------------- #
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Add a segment to the snake at the last segment's position
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move from tail to head
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # move off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


# -------------------- Food Class -------------------- #
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-SCREEN_WIDTH // 2 + 20, SCREEN_WIDTH // 2 - 20)
        y = random.randint(-SCREEN_HEIGHT // 2 + 20, SCREEN_HEIGHT // 2 - 20)
        self.goto(x, y)


# -------------------- Scoreboard Class -------------------- #
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, SCREEN_HEIGHT // 2 - 40)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))

    def reset(self):
        self.score = 0
        self.update_scoreboard()


# -------------------- Main Game -------------------- #
def main():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(BG_COLOR)
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        x, y = snake.head.xcor(), snake.head.ycor()
        if x > SCREEN_WIDTH // 2 - 10 or x < -SCREEN_WIDTH // 2 + 10 or y > SCREEN_HEIGHT // 2 - 10 or y < -SCREEN_HEIGHT // 2 + 10:
            scoreboard.game_over()
            game_is_on = False

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False

    screen.exitonclick()


if __name__ == "__main__":
    main()