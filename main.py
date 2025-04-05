import time
import turtle
from turtle import Turtle,Screen
from createpaddle import Create_Paddle
from ball import Ball
from score import Score

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle=Create_Paddle((-380,0))
l_paddle=Create_Paddle((380,0))
ball=Ball()
score=Score()

screen.listen()
screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key="Down",fun=r_paddle.down)
screen.onkey(key="Left",fun=l_paddle.right_up)
screen.onkey(key="Right",fun=l_paddle.right_down)
is_on = True
while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()


    if ball.distance(l_paddle) < 35 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(r_paddle) < 35 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor()>380 :

        ball.new_ball()
        score.r_point()

    if ball.xcor() < -380:
        ball.new_ball()
        score.l_point()









screen.exitonclick()