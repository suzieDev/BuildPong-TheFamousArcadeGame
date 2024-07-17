from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # self.ycor() - self.y_move # the same as self.y_move *= -1
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # each time the ball bounce the paddle, it increases the ball speed
        self.move_speed *= 0.9

    def reset_paddle(self):
        self.goto(0, 0)
        # after reset the ball position, also reset the ball original speed
        self.move_speed = 0.1
        self.x_move *= -1


"""
Example of Distance and Direction Change:
•	Initial Movement:
•	Suppose self.x_move = 10 and self.y_move = 10. 
This means the ball initially moves 10 units in the x and y directions per move() call.
•	Bouncing Off a Paddle:
•	If the ball collides with a paddle (ball.bounce_x()), self.x_move might change to -10
(or another value depending on implementation),
causing the ball to reverse its x-direction in subsequent move() calls.
•	Adjusting Speed:
•	Initially, self.move_speed = 0.1. This slows down the ball’s movement (time.sleep(0.1) between movements).
•	After ball.bounce_x(), self.move_speed decreases (self.move_speed *= 0.9), 
causing the ball to move faster (time.sleep(0.09) in the next iteration, 
then time.sleep(0.081) after the next bounce, and so on).
"""