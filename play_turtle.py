from turtle import Turtle

INITIAL_X = 0
INITIAL_Y = -240


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.goto(x=INITIAL_X, y=INITIAL_Y)
        self.refresh_speed = 0.1
        self.score = 0

    def move_up(self):
        self.forward(20)

    def car_collision(self, car):
        return self.distance(car) <= 20

    def player_reset(self):
        if self.ycor() >= 240:
            self.goto(INITIAL_X, INITIAL_Y)
            self.refresh_speed /= 1.10
            self.score += 1
