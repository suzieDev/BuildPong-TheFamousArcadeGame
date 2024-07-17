
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()  # screen object
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # slow down the ball movement
    screen.update()
    """In each iteration of the game loop, the move() method is called. 
    This method updates the ball’s position based on its current coordinates (self.xcor() and self.ycor())
     and the movement attributes (self.x_move and self.y_move)."""
    ball.move()

    # Detect collision with wall (up and down)
    """When the ball bounces off a horizontal surface (top or bottom walls or paddles),
     self.y_move is reversed (self.y_move *= -1). 
     This changes the sign of self.y_move, effectively changing the direction of vertical movement."""
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Right paddle misses
    if ball.xcor() > 380:
        ball.reset_paddle()
        scoreboard.l_point()

    # Detect Left paddle misses
    if ball.xcor() < -380:
        # reset the ball to the center
        ball.reset_paddle()
        # if left paddle misses the ball, right paddle gets one point
        scoreboard.r_point()

screen.exitonclick()

