import turtle
import random


class Snake:
    def __init__(self):
        # self.snake.speed('fastest')
        self.segments = []
        self.positions = []
        self.x = 0
        self.y = 0
        self.snake_length = 3

    def snake_create(self):
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
        snake_segment = turtle.Turtle(shape='square')
        snake_segment.penup()
        self.segments.append(snake_segment)
        print(len(self.segments))

    def move(self):
        # TODO: debug snake movement
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].position())
            # print(i, self.segments[i].position())
            print(self.segments[0].heading())
        self.segments[0].forward(20)

    def go_north(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def go_south(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def go_east(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def go_west(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)


class SnakeFood:
    def __init__(self):
        self.food = turtle.Turtle(shape='circle')
        self.food.shapesize(1, 1)
        self.food.penup()

    def place_food(self):
        self.food.setposition(random.randint(-200, 200), random.randint(-200, 200))
