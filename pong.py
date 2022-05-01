import pong_module
import turtle

# setup screen
screen_init = pong_module.Screen()
screen = screen_init.screen

# create middle wall
middle_wall = pong_module.MiddleWall()
middle_wall.create_wall()

# create two paddles
player_one_paddle = pong_module.PlayerOnePaddle()
player_one_paddle.start_paddle_one()
# prompt user for two players or one

# create paddle 1 keys. if 2p, paddletwo controlled by keyboard, else random movement

# restrict paddle movement within boundaries

# create ball and articulate movement
pong_ball = pong_module.Ball()
pong_ball.goto(0, 0)


# create function for ball collision with screen vertical screen boundaries or paddles

# create scoreboard and functionality

# update score when ball collides with lateral screen boundaries


screen.exitonclick()
