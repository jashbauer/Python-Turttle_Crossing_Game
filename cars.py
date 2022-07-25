from turtle import Turtle
from random import randint


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.my_cars = []
        self.create_car()

    def create_car(self):
        offset = 0
        for i in range(12):
            random_x = randint(-300, 300)
            y = -180 + offset
            random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            car = Turtle(shape="square")
            car.pu()
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.goto(random_x, y)
            car.color(random_color)
            car.setheading(180)
            self.my_cars.append(car)
            offset += 30

    def move_cars(self):
        for car in self.my_cars:
            car.forward(randint(0, 30))
            if car.xcor() < -350:
                x = 350
                y = randint(-180, 200)
                car.goto(x=x, y=y)


