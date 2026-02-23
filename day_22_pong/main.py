from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)
    
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.start_up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")
screen.onkeypress(r_paddle.start_down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")

screen.onkeypress(l_paddle.start_up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")
screen.onkeypress(l_paddle.start_down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    r_paddle.move()
    l_paddle.move()
    ball.move()
    screen.update()

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

screen.exitonclick()