from turtle import Turtle

LANE_WIDTH = 2
STRIP_WIDTH = 5


class Street(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.upper_lane()
        self.lower_lane()
        self.middle_strip()

    def upper_lane(self):
        self.pensize(width=LANE_WIDTH)
        self.pu()
        self.goto(x=-300, y=210)
        self.pd()
        self.forward(600)

    def lower_lane(self):
        self.pensize(width=LANE_WIDTH)
        self.pu()
        self.goto(x=-300, y=-210)
        self.pd()
        self.forward(600)

    def middle_strip(self):
        self.pensize(width=STRIP_WIDTH)
        self.pu()
        self.goto(x=-300, y=0)
        self.pencolor("orange")
        self.pensize(width=5)
        while self.xcor() != 300:
            self.pd()
            self.forward(20)
            self.pu()
            self.forward(20)
