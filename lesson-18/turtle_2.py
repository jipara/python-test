from turtle import Turtle, Screen
import random
timmy = Turtle()

color = ["red", "blue", "pink", "black", "green", "orange"]
directions = [0, 90, 180, 270]

for _ in range(50):
    timmy.forward(20)
    timmy.pensize(15)
    timmy.color(random.choice(color))
    timmy.setheading(random.choice(directions))
