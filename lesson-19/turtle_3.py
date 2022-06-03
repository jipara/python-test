import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the raise?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-170, -100, -30, 40, 110, 180]
all_turtles = []


for turtle1 in range(0, 6):
    name = Turtle()
    name.shape("turtle")
    name.penup()
    name.color(colors[turtle1])
    name.goto(x=-230, y=y_position[turtle1])
    all_turtles.append(name)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won! The {winning_color}")
            else:
                print(f"you lost! The {winning_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        # else:
        #     is_race_on == False

screen.exitonclick()

