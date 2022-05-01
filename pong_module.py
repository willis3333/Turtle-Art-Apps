import turtle
import snake_module


class Screen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.screensize(1000, 1000)
        self.screen.tracer(0)
        self.screen.title('PONG 1.0')


class MiddleWall:
    def __init__(self):
        self.wall_writer = turtle.Turtle()
        # self.wall_writer.color('white')
        # self.speed('fastest')
        self.wall_writer.penup()
        self.wall_writer.goto(0, -290)
        self.wall_writer.setheading(90)

    def create_wall(self):
        for _ in range(0, 10):
            self.wall_writer.pendown()
            self.wall_writer.forward(30)
            self.wall_writer.penup()
            self.wall_writer.forward(30)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        # self = turtle.Turtle()
        self.shape('circle')
        # self.color('white')
        self.shapesize(200, 200)
        # self.ball.penup()
        self.goto(0, 0)


class PlayerOnePaddle:
    def __init__(self):
        self.paddle = turtle.Turtle(shape='square')
        # self.paddle.color('white')

    def start_paddle_one(self):
        self.paddle.goto(-100, 0)
        self.paddle.write(arg='Player One', align='center', font=('Arial', 15, 'normal'))

#
# class CPUorPlayerTwoPaddle(turtle.Turtle):
#     def __init__(self):
#         super().__init__()
#
#
# class ScoreBoard(turtle.Turtle):
#     def __init__(self):
#         super().__init__()