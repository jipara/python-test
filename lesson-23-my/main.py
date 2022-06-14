import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
turtle = Player()
screen.onkey(turtle.up, "Up")
board = Scoreboard()
objs = []

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    for i in range(1):
        time.sleep(2)
        objs.append(CarManager())
        for i in objs:
            t = i.move()
            if turtle.distance(i) < 15:
                game_is_on = False
                board.game_over()
            if turtle.ycor() > 270:
                board.level()
                time.sleep(2)
                i.move_increment()
