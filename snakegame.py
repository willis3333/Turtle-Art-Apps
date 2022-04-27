import turtle
import time
import snake_module

snake = snake_module.Snake()
screen = turtle.Screen()
screen.screensize(1000, 1000)
screen.tracer(0)
screen.title('Snake Game')
snake.snake_create()
snake_food = snake_module.SnakeFood()
snake_food.place_food()

game_on = True


while game_on:
    screen.listen()
    screen.onkey(fun=snake.go_north, key='w')
    screen.onkey(fun=snake.go_south, key='s')
    screen.onkey(fun=snake.go_west, key='a')
    screen.onkey(fun=snake.go_east, key='d')
    screen.update()
    time.sleep(.2)
    snake.move()

    if int(snake.segments[0].position()[1] - snake_food.food.position()[1]) in range(-10, 10) and int(snake.segments[0].position()[0] - snake_food.food.position()[0]) in range(-20, 20):
        snake_food.place_food()
        snake.add_segment()
        time.sleep(.3)
    #     snake_segment = turtle.Turtle(shape='square')
    #     snake_segment.penup()
    #     # vars()['snake_segment' + str(i)].fillcolor('green')
    #     snake_segment.goto(position)
    #     segments.append(snake_segment)
    #     # speed += 5
    #     print(len(segments))

    if snake.segments[0].position()[0] > 298 or snake.segments[0].position()[0] < -298 or snake.segments[0].position()[1] > 298 or snake.segments[0].position()[1] < -298:
        game_on = False
        restart = screen.textinput('Game OVER', 'continue? (y or n)')
        if restart == 'y':
            screen.clear()
            snake.__init__()
            snake.snake_create()
            snake_food.__init__()
            snake_food.place_food()
            # snake.home()
            # snake_food.setposition(random.randint(-200, 200), random.randint(-200, 200))
            # segments = [snake]
            # positions = []
            # x = 20
            # y = 0
            # snake_length = 3
            # for _ in range(0, snake_length):
            #     coordinates = (x, y)
            #     positions.append(coordinates)
            #     x += 20
            # i = 0
            # for position in positions:
            #     snake_segment = turtle.Turtle(shape='square')
            #     snake_segment.penup()
            #     # vars()['snake_segment' + str(i)].fillcolor('green')
            #     snake_segment.goto(position)
            #     segments.append(snake_segment)
            #     i += 1
            game_on = True
        else:
            exit()

screen.exitonclick()

