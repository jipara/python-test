import random
from tkinter import *

import pandas
from pandas import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
to_learn = {}
# ---------------------------- Flash card setup ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
#dictionary_words = DataFrame.to_dict(data)
    to_learn = data.to_dict(orient="records")



def random_word():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=image_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=image_back)


def is_known():
    to_learn.remove(current_card)
    random_word()
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = PhotoImage(file="./images/card_front.png")
image_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=image_front)

title_text = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=(FONT_NAME, 60, "bold"))

canvas.grid(column=1, row=0, columnspan=2)
#2
#
# canvas_back = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas_back.create_image(400, 253, image=image_back)
#
# title_back = canvas_back.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
# word_back = canvas_back.create_text(400, 263, text="Word", fill="black", font=(FONT_NAME, 60, "bold"))
# canvas_back.grid(column=1, row=0)

#2
image_x = PhotoImage(file="./images/wrong.png")
button_x = Button(image=image_x, highlightthickness=0, command=random_word)
button_x.grid(column=1, row=1)

#3
image_right = PhotoImage(file="./images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=is_known)
button_right.grid(column=2, row=1)

random_word()
window.mainloop()
