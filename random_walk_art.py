import time
import turtle
import random

walker_turtle = turtle.Turtle()
screen = walker_turtle.getscreen()
screen.screensize(1000, 1000)
walk_angles = [0, 90, 180, 270, 360]
# color_list = ['blue', 'red', 'green', 'purple', 'yellow']
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


walker_turtle.pensize(10)
walker_turtle.speed('fastest')
for _ in range(10000):
    angle = random.choice(walk_angles)
    walker_turtle.right(angle)
    color_tuple = random_color()
    walker_turtle.pencolor(color_tuple)
    walker_turtle.forward(10)

time.sleep(5)
screen.exitonclick()
