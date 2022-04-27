import turtle
import turtle_actions_module

turtle_object = turtle.Turtle()
screen = turtle_object.getscreen()
turtle.colormode(255)

turtle_object.pen(pendown=False)
screen.screensize(1000, 1000)
screen.bgcolor('yellow')
turtle_object.speed('fastest')
screen.delay(10)
turtle_object.setposition(-250, -250)
dot_sizes = [5, 10, 15, 20, 25, 30]
turtle_drawer = turtle_actions_module.TurtleDrawer(turtle_object, dot_sizes)
turtle_drawer.go_to_end()
x = 0
while x < 5:
    turtle_drawer.left_side_uturn()
    turtle_drawer.go_to_end()
    turtle_drawer.right_side_uturn()
    turtle_drawer.go_to_end()
    x += 1

# time.sleep(3)
#
# exit()

