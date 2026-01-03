from turtle import Screen
import time

import snake
from scoreboard import Scoreboard
from food import Food
from snake import Snake

#setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=my_snake.up, key="Up")
screen.onkey(fun=my_snake.down, key="Down")
screen.onkey(fun=my_snake.left, key="Left")
screen.onkey(fun=my_snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # detect collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 \
        or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    for segment in my_snake.segments[1:]:
         if my_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()










screen.exitonclick()