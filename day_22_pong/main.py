from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from game_screen import GameScreen
import time

screen = GameScreen()
screen.draw_net()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()
ball = Ball()

game_is_on = False

def start_game():
    global game_is_on
    if not game_is_on:
        screen.clear_start_text()
        game_is_on = True

screen.bind_keys(r_paddle, l_paddle, start_game)

while True:
    screen.update()
    if game_is_on:
        time.sleep(ball.move_speed)
        r_paddle.move()
        l_paddle.move()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0):
            ball.bounce_x(r_paddle.ycor())
        elif (ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0):
            ball.bounce_x(l_paddle.ycor())
        
        # Detect when right paddle misses
        if ball.xcor() > 380:
            score.increase_left_score()
            ball.reset_position()
            if score.check_winner():
                game_is_on = False
        
        # Detect when left paddle misses
        if ball.xcor() < -380:
            score.increase_right_score()
            ball.reset_position()
            if score.check_winner():
                game_is_on = False

screen.exitonclick()