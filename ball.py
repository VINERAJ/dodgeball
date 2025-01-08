from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_acceleration = 400
        self.y_velocity = 0
        self.x_velocity = 0
        self.y_move = 0
        self.x_move = 0
        self.points = 0
        self.is_fired = False

    def make_ball(self):
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed("slowest")
        self.xpos = random.randint(-350, 350)
        self.goto(self.xpos, 250)

    def move(self):
        if self.is_fired==True:
            self.y_velocity = self.y_velocity + 0.04*self.y_acceleration
            self.y_move = self.y_velocity*0.04 + 0.5*self.y_acceleration*0.0016
            self.x_move = self.x_velocity * 0.04
            self.goto(self.xcor()+self.x_move, self.ycor()-self.y_move)

    def at_bottom(self):
        if self.ycor()<-300:
            self.is_fired=False
            self.points+=10
            self.y_velocity=0+self.points
            self.xpos = random.randint(-350, 350)
            self.goto(self.xpos, 250)