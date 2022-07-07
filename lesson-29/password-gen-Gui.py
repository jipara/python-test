from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    p_l = [choice(letters) for _ in range(nr_letters)]
    p_s = [choice(symbols) for _ in range(nr_symbols)]
    p_n = [choice(symbols) for _ in range(nr_numbers)]

    password_list = p_l + p_s + p_n
    shuffle(password_list)

    password = "".join(password_list)
    entry3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def safe():
    website_input = entry1.get()
    email_input = entry2.get()
    password_input = entry3.get()
    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title="Empty fields", message="you forgot to fill all fields, please field them all")
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"These are the details entered: \nEmail: {email_input} \nPassword: {password_input} \nis it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website_input} | {email_input} | {password_input} \n")
                entry1.delete(0, 'end')
                entry3.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Mamager")
window.config(pady=50, padx=50)

image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

label1 = Label(text="Website", font=("Arial", 12, "bold"))
label1.grid(column=0, row=1)


label2 = Label(text="Email/Username", font=("Arial", 12, "bold"))
label2.grid(column=0, row=2)


label3 = Label(text="Password", font=("Arial", 12, "bold"))
label3.grid(column=0, row=3)

entry1 = Entry(width=35)
entry1.grid(column=1, row=1, columnspan=2)
entry1.focus()

entry2 = Entry(width=35)
entry2.grid(column=1, row=2, columnspan=2)
entry2.insert(0, "jipara@email.com")

entry3 = Entry(width=21)
entry3.grid(column=1, row=3, columnspan=1)


button1 = Button(text="Generate Password", command=password_gen)
button1.grid(column=2, row=3)

button2 = Button(text="Add", width=36, command=safe)
button2.grid(column=1, row=4, columnspan=2)

window.mainloop()
