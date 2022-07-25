from turtle import Turtle

ALIGN = "center"
GAMEOVER_FONT = ("arial", 20, "normal")
SCORE_FONT = ("courier", 20, "normal")
SCORE_X = 0
SCORE_Y = 270


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def write_score(self, score):
        self.goto(SCORE_X, SCORE_Y)
        self.clear()
        self.write(f"SCORE: {score}", align=ALIGN, font=SCORE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=GAMEOVER_FONT)
