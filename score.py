from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.l_paddle=0
        self.r_paddle=0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_paddle,align="center",font=("Courier",50,"normal"))
        self.goto(100, 200)
        self.write(self.r_paddle, align="center", font=("Courier", 50, "normal"))
    def l_point(self):
        self.l_paddle+=1
        self.updatescore()
    def r_point(self):
        self.r_paddle+=1
        self.updatescore()

