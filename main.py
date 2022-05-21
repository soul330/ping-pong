from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# SCREEN
game_screen = Screen()
game_screen.setup(width=800, height=600)
game_screen.title("Ping-Pong Game!")
game_screen.bgcolor("black")
game_screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



game_screen.listen()
game_screen.onkey(right_paddle.go_to_up, "Up")
game_screen.onkey(right_paddle.go_to_down, "Down")
game_screen.onkey(left_paddle.go_to_up, "w")
game_screen.onkey(left_paddle.go_to_down, "s")


game_turn_on = True
while game_turn_on:
    time.sleep(ball.speed_of_movement)
    game_screen.update()

    ball.move()

    # Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()


    # Detectong the riht_paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detectong the left_paddle misses.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()





game_screen.exitonclick()
