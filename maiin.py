from turtle import Screen, Turtle
from ball import Ball
from player import Player
from enemies import Enemies
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Dodgeball")
screen.tracer(0)

you = Player()
ball = Ball()
enemies = Enemies()
screen.listen()
screen.update()

game_is_on = True
while game_is_on:
    time.sleep(0.04)
    screen.onkey(you.move_left, "Left")
    screen.onkey(you.move_right, "Right")
    you.check_edges()
    if enemies.fire()==True:
        ball.is_fired=True
    enemies.ball_move()
    # ball.move()
    # ball.at_bottom()
    # if ball.distance(you)<20:
    #     game_is_on=False
    screen.update()


screen.exitonclick()