import turtle
import random

'''
Snake Module is created to create object oriented code for the snakegame.
'''

class Snake:
    '''
    The Snake class is the default snake object in the game, and can be used to alter the snake's features.
    It also includes the functions required to create, move, turn, and add length to the snake.
    '''
    def __init__(self):
        # self.snake.speed('fastest')
        self.segments = []
        self.positions = []
        self.x = 0
        self.y = 0
        self.snake_length = 3

    def snake_create(self):
        '''
        Creates three square turtle objects and appends them to segments list and moves them to
        starting position locations to form a snake
        '''
        for _ in range(0, self.snake_length):
            coordinates = (self.x, self.y)
            self.positions.append(coordinates)
            self.x -= 20
        for position in self.positions:
            snake_segment = turtle.Turtle(shape='square')
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)
            print(snake_segment.xcor(), snake_segment.ycor())
            print(self.segments)

    def add_segment(self):
        '''
        Appends one square turtle object to segments list to add additional length to snake
        '''
        snake_segment = turtle.Turtle(shape='square')
        snake_segment.penup()
        self.segments.append(snake_segment)
        print(len(self.segments))

    def move(self):
        '''
        Moves snake segments forward in animated motion with one segment following the next in position
        '''
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].position())
            # print(i, self.segments[i].position())
        self.segments[0].forward(20)

    def go_north(self):
        '''
        Sets heading of snakes head (1st segment) northbound or 90 degrees only if its not currently southbound
        '''
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def go_south(self):
        '''
        Sets heading of snakes head (1st segment) southbound or 270 degrees only if its not currently northbound
        '''
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def go_east(self):
        '''
        Sets heading of snakes head (1st segment) eastbound or 0 degrees only if its not currently westbound
        '''
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def go_west(self):
        '''
        Sets heading of snakes head (1st segment) westbound or 180 degrees only if its not currently eastbound
        '''
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)


class SnakeFood:
    '''
    The SnakeFood class is the default snake object in the game, and can be used to alter the snake's features.
    '''
    def __init__(self):
        self.food = turtle.Turtle(shape='circle')
        self.food.shapesize(1, 1)
        self.food.penup()

    def place_food(self):
        '''
        places food in random position on the screen
        '''
        self.food.setposition(random.randint(-200, 200), random.randint(-200, 200))


class ScoreBoard(turtle.Turtle):
    '''
    Default object for game scoreboard with parent class Turtle. 
    '''
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)

    def show_score(self):
        '''
        Writes string to object scoreboard displaying current score stored as score variable
        '''
        self.write(arg=f'Score: {self.score}', align='center', font=('Arial', 15, 'normal'))

    def update_score(self):
        '''
        Adds 1 to score variable and clears then shows current score
        '''
        self.score += 1
        self.clear()
        self.show_score()

