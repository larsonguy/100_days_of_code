import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move_turtle, "Up")

win_count = 0
game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car and stop game
    for car in car_manager.all_cars:
        if car.distance(player) < 22:
            scoreboard.game_over()
            game_is_on = False
    if player.is_at_finish_line():
        player.turtle_reset()
        car_manager.level_up()
        print(car_manager.car_speed)
        scoreboard.score_point()


screen.exitonclick()
