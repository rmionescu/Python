import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

PLAYER_WIDTH, PLAYER_HEIGHT = 20, 26
CAR_WIDTH, CAR_HEIGHT = 40, 20


def exit_game():
    global game_is_on
    game_is_on = False


# This works only if the turtle is a square of 20x20 but the turtle is more like 20x26
def check_rect_collision(a, b):
    if abs(int(a.xcor()) - int(b.xcor())) < int(PLAYER_WIDTH/2 + CAR_WIDTH/2) and \
            abs(int(a.ycor()) - int(b.ycor())) < int(PLAYER_HEIGHT/2 + CAR_HEIGHT/2):
        return True


def determinant(vec1, vec2):
    # print(f"{vec1}, {vec2}")
    # print(f"Determinant is {vec1[0] * vec2[1] - vec1[1] * vec2[0]}")
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


def vector_subtraction(v1, v2):
    x_result = (v1[0] + (-1 * v2[0]), v1[1] + (-1 * v2[1]))
    return x_result


# one edge is a-b, the other is c-d
# Return true in case of intersection
def edge_intersection(a, b, c, d):
    # print(f"Calculating det for {a, b} and {c, d}")
    det = determinant(vector_subtraction(b, a), vector_subtraction(c, d))
    t = determinant(vector_subtraction(c, a), vector_subtraction(c, d)) / det
    u = determinant(vector_subtraction(b, a), vector_subtraction(c, a)) / det
    if (t < 0) or (u < 0) or (t > 1) or (u > 1):
        return False
    else:
        return True


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing v1")
screen.bgcolor("grey")
screen.tracer(0)
screen.listen()


# Create the player
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Check for keystrokes
screen.onkey(exit_game, "Escape")
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    # print(f"Generated a new car at {car_manager.all_cars[-1].position()}.")
    car_manager.move_car()

    # Detect collision with a car
    for car in car_manager.all_cars:
        # if (abs(car.xcor() - player.xcor()) <= 25) and (abs(car.ycor() - player.ycor()) <= 19):
        if check_rect_collision(car, player):
            print(f"Collision with car detected at player position: {player.position()} and car {car.position()}")
            # Check for precision collision
            upper_pl_vector_a = (player.xcor()-3, player.ycor()+17)
            upper_pl_vector_b = (player.xcor()+3, player.ycor()+17)
            lower_pl_vector_a = (player.xcor()-9, player.ycor()-9)
            lower_pl_vector_b = (player.xcor()+9, player.ycor()-9)
            front_car_vector_c = (car.xcor()-20, car.ycor()-10)
            front_car_vector_d = (car.xcor()-20, car.ycor()+10)
            lower_car_vector_d = (car.xcor()+20, car.ycor()-10)
            if edge_intersection(upper_pl_vector_a, upper_pl_vector_b, front_car_vector_c, front_car_vector_d) or \
                    edge_intersection(lower_pl_vector_a, lower_pl_vector_b, front_car_vector_c, front_car_vector_d) or \
                    edge_intersection(upper_pl_vector_a, upper_pl_vector_b, front_car_vector_d, lower_car_vector_d):
                print(f"\tPrecision collision with car detected at player position: {int(player.xcor()), player.ycor()}"
                      f" and car {car.xcor(), car.ycor()}")
                scoreboard.game_over()
                game_is_on = False

    # Check if player crossed the road
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.increase_score()
        # Increase the speed for all the cars
        car_manager.increase_speed()

screen.exitonclick()
