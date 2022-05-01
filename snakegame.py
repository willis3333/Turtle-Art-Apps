import turtle
import time
import snake_module

# set up initial variables for snake, food, and screen
snake = snake_module.Snake()
screen = snake_module.ScreenInit()
snake.snake_create()
snake_food = snake_module.SnakeFood()
snake_food.place_food()
scoreboard = snake_module.ScoreBoard()
scoreboard.show_score()

# Begin game
game_on = True
while game_on:
    # set screen to listen to keyboard input for snake movement
    screen.listen()
    screen.onkey(fun=snake.go_north, key='w')
    screen.onkey(fun=snake.go_south, key='s')
    screen.onkey(fun=snake.go_west, key='a')
    screen.onkey(fun=snake.go_east, key='d')
    # snake movement
    screen.update()
    time.sleep(.1)
    snake.move()
    # set snake food to relocate upon collision with snake
    if int(snake.segments[0].distance(snake_food.food)) < 20:
        scoreboard.update_score()
        snake_food.place_food()
        snake.add_segment()
        time.sleep(.1)
    # set game to pause and scoreboard to write game over snake collision with screen borders
    if int(snake.segments[0].position()[0]) not in range(-295, 295) or int(snake.segments[0].position()[1]) not in range(-295, 295):
        game_on = False
        scoreboard.game_over()
        # restart = screen.textinput('Game OVER', 'continue? (y or n)')
        # if restart == 'y':
        #     # resetting snake, food, and screen if user chooses to continue
        #     # TODO: debug snake movement on restart of game
        #     screen.clear()
        #     snake.__init__()
        #     snake.snake_create()
        #     snake_food.__init__()
        #     snake_food.place_food()
        #     scoreboard.__init__()
        #     scoreboard.show_score()
        #     game_on = True
        # else:
        #     exit()
    # set game to pause and scoreboard to write game over snake collision with its tail
    for segment in snake.segments[1:]:
        if segment.distance(snake.segments[0]) < 5:
            game_on = False
            scoreboard.game_over()
screen.exitonclick()

