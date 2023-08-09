from turtle import Screen
from paddle import Paddle
from ball import Ball
import  time
from scoreboard import ScoreBoard


scoreboard = ScoreBoard()
screen = Screen()
screen.setup(width=1200,height=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle((-587,0))
r_paddle = Paddle((580,0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')


is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with y co-ordinate wall
    if ball.ycor() > 380 or ball.ycor() < -390:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -560 or ball.distance(r_paddle) < 50 and ball.xcor() > 550:
        ball.bounce_x()
        l_paddle.paddle_speed(ball.move_speed)
        r_paddle.paddle_speed(ball.move_speed)

    # detect collision with x co-ordinates
    if ball.xcor() < -590:
        ball.reset_position()
        scoreboard.r_point()


    if  ball.xcor() > 580:
        ball.reset_position()
        scoreboard.l_point()







screen.exitonclick()