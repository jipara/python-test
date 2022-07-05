
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer")
    label_check_box.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    breaks = [short_break_sec, short_break_sec, short_break_sec, long_break_sec]

    if reps % 8 == 0:
        count_down(long_break_sec)
        label1.config(text="Break", font=("Arial", 25, "bold"), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label1.config(text="Break", font=("Arial", 25, "bold"), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        label1.config(text="Work", font=("Arial", 25, "bold"), fg=GREEN, bg=YELLOW)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        label_check_box.config(text=marks)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label1 = Label(text="Timer", font=("Arial", 25, "bold"), fg=GREEN, bg=YELLOW)
label1.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

label_check_box = Label(font=("Arial", 12, "bold"), fg=GREEN, bg=YELLOW)
label_check_box.grid(column=1, row=3)


window.mainloop()
