from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_POSITION = 280
Y_POSITION = [260, 240, 220, 200, 180, 160, 140, 120, 100, 80, 60, 40, 20, 0, -260, -240, -220, -200, -180, -160, -140,
              -120, -100, -80, -60, -40, -20]
LEFT = 180


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(LEFT)
        self.y_move = 3
        self.move_speed = 0.1
        self.goto(X_POSITION, random.choice(Y_POSITION))
        #self.move()

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_increment(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())
