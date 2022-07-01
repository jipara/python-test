from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)


# my_label = Label(text=0, font=("Arial", 12, "bold"))
# my_label.grid(column=1, row=3)


def button_clicked():
    new_text = entry.get()
    km1 = round(int(new_text) * 0.621371)
    label4.config(text=km1)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=4)

entry = Entry(width=10)
#Add some text to begin with
#entry.insert(END, string=0)
#Gets text in entry
print(entry.get())
entry.config(text=0)
entry.grid(column=1, row=0)
entry.get()



label1 = Label(text="is equal to", font=("Arial", 12, "bold"))
label1.grid(column=0, row=2)

label2 = Label(text="Miles", font=("Arial", 12, "bold"))
label2.grid(column=2, row=0)

label3 = Label(text="Km", font=("Arial", 12, "bold"))
label3.grid(column=2, row=2)

label4 = Label(text=0, font=("Arial", 12, "bold"))
label4.grid(column=1, row=2)

window.mainloop()
