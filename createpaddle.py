from turtle import Turtle
AXIS = [(-350, 0), (350, 0)]
class Create_Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.3, stretch_wid=2.0)
        self.goto(position)



    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
    def right_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
    def right_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)