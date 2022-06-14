from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "right"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.board = 1
        self.color("Black")
        self.penup()
        self.goto(x=-170, y=270)
        self.write(f"Level: {self.board}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def level(self):
        self.board += 1
        self.clear()
        self.write(f"Level: {self.board}", align="center", font=('Arial', 24, 'normal'))
