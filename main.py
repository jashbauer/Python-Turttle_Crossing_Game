from turtle import Screen
from cars import Cars
from street import Street
from play_turtle import Player
from writer import Writer
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.colormode(255)
screen.tracer(0)

street = Street()
cars = Cars()
player = Player()
writer = Writer()


game_on = True
while game_on:
    time.sleep(player.refresh_speed)
    screen.update()

    writer.write_score(score=player.score)
    cars.move_cars()

    screen.listen()
    screen.onkey(fun=player.move_up, key="Up")

    for car in cars.my_cars:
        if player.car_collision(car):
            game_on = False
            writer.game_over()
            break

    player.player_reset()


screen.exitonclick()
