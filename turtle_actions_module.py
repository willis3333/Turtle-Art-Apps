import turtle
import random
import colorgram


def extracted_colors_random():
    colors = colorgram.extract('/Users/willis/downloads/hirst.jpeg', 6)
    color = random.choice(colors).rgb
    return color

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


class TurtleDrawer:

    def __init__(self, turtle_input, dot_size_list):
        self.turtle_var = turtle_input
        self.dot_sizes = dot_size_list

    def go_to_end(self):
        for _ in range(0, 10):
            color = extracted_colors_random()
            self.turtle_var.dot(self.dot_sizes[random.randint(0, len(self.dot_sizes)-1)], color)
            self.turtle_var.forward(50)
        self.turtle_var.dot(self.dot_sizes[random.randint(0, len(self.dot_sizes)-1)], color)

    def left_side_uturn(self):
        self.turtle_var.left(90)
        self.turtle_var.forward(50)
        self.turtle_var.left(90)

    def right_side_uturn(self):
        self.turtle_var.right(90)
        self.turtle_var.forward(50)
        self.turtle_var.right(90)
