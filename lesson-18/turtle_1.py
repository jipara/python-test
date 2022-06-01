from turtle import Turtle, Screen

timmy = Turtle()


# timmy.shape("turtle")
# timmy.color("red", "red")
# for tutle in range(4):
#     timmy.forward(100)
#     timmy.right(90)

import heroes
print(heroes.gen())


# for i in range(5):
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(20)
#     timmy.pendown()
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(20)
#
# for _ in range(3, 11):
#     angle = 360/_
#     for i in range(3, 11):
#         timmy.forward(100)
#         timmy.right(angle)


# timmy.forward(80)
# timmy.left(120)
# timmy.forward(80)
# timmy.left(120)
# timmy.forward(80)
# timmy.left(120)

import random
color = ["red", "blue", "pink", "black", "green", "orange"]

def number(num_slides):
    angel = 360 / num_slides
    for _ in range(num_slides):
        timmy.forward(100)
        timmy.right(angel)
    timmy.pencolor(random.choice(color))


for shape_side_n in range(3, 11):
    number(shape_side_n)

screen = Screen()

screen.exitonclick()
