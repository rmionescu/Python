from turtle import Screen
from paddle import Paddle
from conf import WIDTH, HEIGHT, BALL_SPEED, BALL_SIZE, PADDLE_X_SIZE, PADDLE_Y_SIZE
from ball import Ball
from scoreboard import Scoreboard
import time
import math


def exit_game():
    global game_is_on
    game_is_on = False


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong v1")
screen.tracer(0)

# Create a paddle at 450 px distance of the side walls
p1_paddle = Paddle((int(WIDTH / 2) - 50, 0))
p2_paddle = Paddle((-int(WIDTH / 2) + 50, 0))
# print(f"Left Paddle created at {p2_paddle.position()} and Right paddle created at {(p1_paddle.position())}")

# Create the ball
ball = Ball()

# Create the scoreboard
scoreboard = Scoreboard()

# Check for keystrokes
screen.listen()
screen.onkeypress(p1_paddle.move_up, "Up")
screen.onkeypress(p1_paddle.move_down, "Down")
screen.onkeypress(p2_paddle.move_up, "w")
screen.onkeypress(p2_paddle.move_down, "s")
screen.onkeypress(exit_game, "Escape")

game_is_on = True
detect_paddle_collision = True
winner = ""
speed = BALL_SPEED
ball_size = BALL_SIZE * 20
paddle_x_size = PADDLE_X_SIZE * 20
paddle_y_size = PADDLE_Y_SIZE * 20

# Calculate the up/down wall threshold
h_wall_threshold = (HEIGHT / 2) - ball_size
paddle_threshold = int(WIDTH / 2) - 50 - (paddle_x_size - 5)
paddle_size_th = math.ceil(math.sqrt((paddle_x_size/2) ** 2 + (paddle_y_size/2) ** 2))
# print(f"paddle_threshold={paddle_threshold}; paddle_size_th={paddle_size_th}")

while game_is_on:
    time.sleep(speed)
    # Refresh the screen
    screen.update()
    # Move the ball
    ball.move()
    # print(f"Ball position: {ball.position()}")

    # Detect collision with wall
    if abs(ball.ycor()) >= h_wall_threshold:
        ball.bounce_y()

    # Detect collision with player1_paddle (335)
    if (detect_paddle_collision and (ball.xcor() >= paddle_threshold and p1_paddle.distance(ball) <= paddle_size_th)) or \
            (detect_paddle_collision and (ball.xcor() <= -paddle_threshold and p2_paddle.distance(ball) <= paddle_size_th)):
        ball.bounce_x()
        speed *= 0.9
        print(f"Paddle collision detected at {ball.position()}. Speed = {speed}. "
              f"P1 position {p1_paddle.position()}. P2 position {p2_paddle.position()}")

    # Detect if the ball pass a certain point after which the player loses
    if ball.xcor() >= paddle_threshold + 5 and p1_paddle.distance(ball) > paddle_size_th:
        detect_paddle_collision = False
        winner = "player1"
    elif ball.xcor() <= -paddle_threshold - 5 and p2_paddle.distance(ball) > paddle_size_th:
        detect_paddle_collision = False
        winner = "player2"

    # Detect left/right wall collision
    if abs(ball.xcor()) >= (WIDTH / 2) - (paddle_x_size / 2):
        scoreboard.update_score(winner)
        detect_paddle_collision = True
        ball.goto(0, 0)
        ball.bounce_x()
        speed = BALL_SPEED
        time.sleep(2)


screen.exitonclick()
