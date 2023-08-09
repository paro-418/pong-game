from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-450, 320)
        self.write(f'score: {self.l_score}', align='center', font=('Courier', 40, 'normal'))
        self.goto(450, 320)
        self.write(f'score: {self.r_score}', align='center', font=('Courier', 40, 'normal'))
