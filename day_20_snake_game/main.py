from turtle import Screen
from snake_1 import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food_item = Food()
screen = Screen()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Main Game Loop

def main():
    game_on = True

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(score.game_reset, "r")

    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        

        # Detect collision with food
        if snake.head.distance(food_item) < 15:
            food_item.refresh()
            score.increase_score()
            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_on = False
            score.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                score.game_over()



if __name__ == "__main__":
    main()

screen.exitonclick()