import turtle
import turtle_actions_module

turtle_drawer = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
turtle_drawer.speed('fastest')

gap = 1
for _ in range(0, int(360/gap)):
    turtle_drawer.setheading(turtle_drawer.heading() + gap)
    color = turtle_actions_module.random_color()
    turtle_drawer.pencolor(color)
    turtle_drawer.circle(100)

screen.exitonclck()


