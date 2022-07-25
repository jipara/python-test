from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.label1 = Label(text="Score: 0",
                            font=("Arial", 25, "bold"),
                            bg=THEME_COLOR,
                            fg="white"
                            )
        self.label1.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="some question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # self.canvas.config(text=)

        self.photo = PhotoImage(file="images/true.png")
        self.button_v = Button(self.window, image=self.photo, highlightthickness=0, command=self.true_pressed)
        self.button_v.grid(column=0, row=2)

        self.photo_x = PhotoImage(file="images/false.png")
        self.button_x = Button(self.window, image=self.photo_x, highlightthickness=0, command=self.false_pressed)
        self.button_x.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.label1.config(text=f"Score: {self.quiz.score}"):
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.button_x.config(state="disabled")
            self.button_v.config(state="disabled")


    def true_pressed(self):
        return self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        return self.give_feedback(self.quiz.check_answer("False"))
        # is_right = self.quiz.check_answer("False")
        # self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.give_feedback(1000, self.get_next_question)


    # def check_if_answer_is_correct(self):
    #     bool_answer = self.quiz.check_answer()
    #     print(bool_answer)
