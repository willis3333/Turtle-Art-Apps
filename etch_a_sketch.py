import turtle

turtle_drawer = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    turtle_drawer.forward(10)


def move_backward():
    turtle_drawer.backward(10)


def turn_left():
    turtle_drawer.left(5)


def turn_right():
    turtle_drawer.right(5)

def clear_screen():
    turtle_drawer.clear()


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=clear_screen, key='c')

screen.exitonclick()

