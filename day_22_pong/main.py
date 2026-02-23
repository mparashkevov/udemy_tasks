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

screen.display.listen()
screen.display.onkeypress(r_paddle.start_up, "Up")
screen.display.onkeyrelease(r_paddle.stop_up, "Up")
screen.display.onkeypress(r_paddle.start_down, "Down")
screen.display.onkeyrelease(r_paddle.stop_down, "Down")

screen.display.onkeypress(l_paddle.start_up, "w")
screen.display.onkeyrelease(l_paddle.stop_up, "w")
screen.display.onkeypress(l_paddle.start_down, "s")
screen.display.onkeyrelease(l_paddle.stop_down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    r_paddle.move()
    l_paddle.move()
    ball.move()
    screen.display.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0):
        ball.bounce_x()
    
    # Detect when right paddle misses
    if ball.xcor() > 380:
        score.increase_left_score()
        ball.reset_position()
    
    # Detect when left paddle misses
    if ball.xcor() < -380:
        score.increase_right_score()
        ball.reset_position()

screen.display.exitonclick()