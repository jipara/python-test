import turtle
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

game_is_on = True
data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    state = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another states name?").title()
    if state == "Exit":
        # missing_states = []
        # for state1 in list_of_states:
        #     if state1 not in guessed_states:
        #         missing_states.append(state1)
        # print(missing_states)
        break
    if state in list_of_states:
        guessed_states.append(state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_coordinate = data[data.state == state]
        t.goto(int(data_coordinate.x), int(data_coordinate.y))
        t.write(data_coordinate.state.item())

difference = list(set(list_of_states) - set(guessed_states))
states_to_learn = pandas.DataFrame(difference)
states_to_learn.to_csv("states_to_learn.csv")

turtle.mainloop()


