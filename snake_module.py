import time
import turtle
import random


"""
Snake Module is created to create object oriented code for the snakegame.
"""


class Screen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.screensize(1000, 1000)
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        self.screen.title('Snake Game')


class Snake:
    """
    The Snake class is the default snake object in the game, and can be used to alter the snake's features.
    It also includes the functions required to create, move, turn, and add length to the snake.
    """
    def __init__(self):
        # self.snake.speed('fastest')
        self.segments = []
        self.positions = []
        self.x = 0
        self.y = 0
        self.snake_length = 3

    def snake_create(self):
        """
        Creates three square turtle objects and appends them to segments list and moves them to
        starting position locations to form a snake
        """
        for _ in range(0, self.snake_length):
            coordinates = (self.x, self.y)
            self.positions.append(coordinates)
            self.x -= 20
        for position in self.positions:
            snake_segment = turtle.Turtle(shape='square')
            snake_segment.color('white')
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)
            print(snake_segment.xcor(), snake_segment.ycor())
            print(self.segments)

    def add_segment(self):
        """
        Appends one square turtle object to segments list to add additional length to snake
        """
        snake_segment = turtle.Turtle(shape='square')
        snake_segment.penup()
        snake_segment.color('white')
        snake_segment.goto(self.segments[2].position())
        self.segments.append(snake_segment)
        print(len(self.segments))

    def move(self):
        """
        Moves snake segments forward in animated motion with one segment following the next in position
        """
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].position())
            # print(i, self.segments[i].position())
        self.segments[0].forward(20)

    def go_north(self):
        """
        Sets heading of snakes head (1st segment) northbound or 90 degrees only if its not currently southbound
        """
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def go_south(self):
        """
        Sets heading of snakes head (1st segment) southbound or 270 degrees only if its not currently northbound
        """
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def go_east(self):
        """
        Sets heading of snakes head (1st segment) eastbound or 0 degrees only if its not currently westbound
        """
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def go_west(self):
        """
        Sets heading of snakes head (1st segment) westbound or 180 degrees only if its not currently eastbound
        """
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def reset(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.__init__()
        self.snake_create()


class SnakeFood:
    """
    The SnakeFood class is the default snake object in the game, and can be used to alter the snake's features.
    """
    def __init__(self):
        self.food = turtle.Turtle(shape='circle')
        self.food.color('green')
        self.food.shapesize(.5, .5)
        self.food.penup()

    def place_food(self):
        """
        places food in random position on the screen
        """
        self.food.setposition(random.randint(-200, 200), random.randint(-200, 200))


class ScoreBoard(turtle.Turtle):
    """
    Default object for game scoreboard with parent class Turtle.
    """

    def __init__(self, highest_score, user):
        super().__init__()
        self.score = 0
        self.hi_score = highest_score
        self.user = user
        self.color('white')
        self.hideturtle()
        self.penup()
        self.start_logo = '''

          _________ _______      _____   ____  __.___________  
         /   _____/ \      \    /  _  \ |    |/ _|\_   _____/  
         \_____  \  /   |   \  /  /_\  \|      <   |    __)_   
         /        \/    |    \/    |    \    |  \  |        \  
        /_______  /\____|__  /\____|__  /____|__ \/_______  /  
                \/         \/         \/        \/        \/   

                '''

    def show_score(self):
        '''
        Writes string to object scoreboard displaying current score stored as score variable
        '''
        self.goto(0, 250)
        self.write(arg=f'Score: {self.score} High Score: {self.hi_score}', align='center', font=('Arial', 15, 'normal'))

    def update_score(self):
        '''
        Adds 1 to score variable and clears then shows current score
        '''
        self.score += 1
        if self.score > self.hi_score:
            self.hi_score = self.score
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER. final score: {self.score}', align='center', font=('Arial', 15, 'normal'))

    def reset(self):
        self.clear()
        self.score = 0
        self.show_score()

    def intro(self, high_scores):
        self.goto(0, 0)
        self.write(arg=f'Hello, {self.user}. Welcome to \n{self.start_logo}\nHigh Scores: \n{high_scores}',
                   align='center', font=('Arial', 15, 'normal'))
        time.sleep(4)
        self.clear()


