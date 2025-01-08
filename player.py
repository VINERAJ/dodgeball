from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed("slowest")
        self.goto(0, -250)
        self.move_dist = 10

    def move_left(self):
        self.goto(self.xcor()-self.move_dist, -250)

    def move_right(self):
        self.goto(self.xcor()+self.move_dist, -250)

    def check_edges(self):
        if self.xcor()>350:
            self.goto(350, -250)
        elif self.xcor()<-350:
            self.goto(-350, -250)