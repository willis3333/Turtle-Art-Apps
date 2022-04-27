import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.title('Ninja Turtle Race')

donatello = turtle.Turtle(shape='turtle')
rafael = turtle.Turtle(shape='turtle')
michelangelo = turtle.Turtle(shape='turtle')
leonardo = turtle.Turtle(shape='turtle')

turtle_list = [donatello, rafael, michelangelo, leonardo]
turtle_colors = ['purple', 'red', 'orange', 'blue']
x = 0
for ninjaturtle in turtle_list:
    ninjaturtle.fillcolor(turtle_colors[x])
    x += 1

y = 150
for ninjaturtle in turtle_list:
    ninjaturtle.penup()
    ninjaturtle.goto(x=-230, y=y)
    y -= 100

user_bet = screen.textinput('Choose your turtle!', 'Which ninja turtle do you think will win?\n'
                                                   '0-Donatello(purple)\n1-Rafael(red)\n2-Michelangelo(orange)\n3-Leonardo(blue)')
print(user_bet)

if user_bet:
    race_on = True

while race_on:
    for turtle_index in range(0, len(turtle_list)):
        ninjaturtle = turtle_list[turtle_index]
        ninjaturtle.forward(random.randint(0, 10))
        if ninjaturtle.position()[0] >= 230:
            print(f'{turtle_index}')
            race_on = False
            ninjaturtle.home()
            ninjaturtle.shapesize(5, 5, 5)
            if user_bet == turtle_index:
                screen.title('You win!')
            else:
                screen.title('Maybe next time!')

screen.exitonclick()
