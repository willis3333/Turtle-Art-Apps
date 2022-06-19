import turtle
import time
import snake_module

# set up initial variables for snake, food, and screen
snake = snake_module.Snake()
screen_init = snake_module.Screen()
screen = screen_init.screen
snake.snake_create()
snake_food = snake_module.SnakeFood()
snake_food.place_food()
user = screen.textinput('Please enter your name', 'Your name:').upper()

# create high scores dictionary from txt file
with open('snake_high_scores.txt') as f:
    high_score_list = f.readlines()
    f.close()
high_score_dict = {}
high_scores_string = ''
# high_score_list = high_score_list[0:10]
for i in range(1, len(high_score_list), 2):
    high_score_dict[high_score_list[i-1].replace('\n','')] = int(high_score_list[i])
sorted_high_score_dict = dict(sorted(high_score_dict.items(), key=lambda item: item[1], reverse=True))
score_key_list = list(sorted_high_score_dict.items())[0:5]
highest_score_key = int(score_key_list[0][1])
lowest_score_key = int(score_key_list[-1][1])
for pair in score_key_list:
    high_scores_string += f'{pair[0]} : {pair[1]}\n'

# scoreboard intro/ initiation
scoreboard = snake_module.ScoreBoard(user=user, highest_score=highest_score_key)
scoreboard.intro(high_scores_string)
scoreboard.show_score()


def game_over():
    """
    function to display game over and reset snake, food and screen upon collision with tail or wall.
    Also adds score to txt file if it is in the top 5
    """
    scoreboard.game_over()
    if scoreboard.score > lowest_score_key:
        score_key_list[-1] = (user, scoreboard.score)
        with open('snake_high_scores.txt', 'w') as file:
            for score_pair in score_key_list:
                file.write(f'{score_pair[0]}\n{score_pair[1]}\n')
        restart = screen.textinput('Game OVER', 'HIGH SCORE ! play again? (y or n)')
    else:
        restart = screen.textinput('Game OVER', 'play again? (y or n)')
    if restart == 'y':
        # resetting snake, food, and screen if user chooses to continue
        scoreboard.reset()
        snake_food.place_food()
        snake.reset()
    else:
        exit()


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
        game_over()
    # set game to pause and scoreboard to write game over snake collision with its tail
    for segment in snake.segments[1:]:
        if segment.distance(snake.segments[0]) < 5:
            game_over()

screen.exitonclick()

