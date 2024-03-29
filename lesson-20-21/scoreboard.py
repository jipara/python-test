from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def score_1(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))


