from turtle import Turtle, Screen
from ball import Ball
import random

class Enemies(Turtle):
    def __init__(self):
        super().__init__()
        self.enemy_list = []
        self.ball_list = []
        self.xpos = -350
        self.fired_ball = 0
        for x in range(0,7):
            x_point = self.xpos+x*140
            new_enemy = Turtle("square")
            new_enemy.color("red")
            new_enemy.penup()
            new_enemy.speed("slowest")
            self.enemy_list.append(new_enemy)
            new_enemy.goto(x_point, 250)
            new_ball = Ball()
            new_ball.goto(x_point, 250)
            new_ball.hideturtle()
            self.ball_list.append(new_ball)


    def fire(self):
        for enemy in self.enemy_list:
            fire_chance = random.randint(0, 5)
            print(fire_chance)
            if fire_chance==1:
                self.ball_list[self.enemy_list.index(enemy)].showturtle()
                self.fired_ball = self.enemy_list.index(enemy)
                self.ball_list[self.enemy_list.index(enemy)].is_fired=True
                return True

    def ball_move(self):
        print("working")
        self.ball_list[self.fired_ball].move()