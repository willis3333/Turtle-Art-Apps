import turtle
import time

turtle_drawer = turtle.Turtle()

screen = turtle.getscreen()

screen.screensize(1000, 1000)


sides = [3, 4, 5, 6, 7, 8]
color_list = ['blue', 'red', 'green', 'purple', 'yellow', 'orange']
for side in sides:
    turtle.pencolor(color_list[side-3])
    turtle.forward(100)
    angle = 360 / side
    for _ in range(side-1):
        turtle.right(angle)
        turtle.forward(100)
    turtle.right(angle)

screen.exitonclick()
# exit()
