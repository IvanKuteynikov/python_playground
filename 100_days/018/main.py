import turtle as t
import random
from extract_colors import color_list

nit = t.Turtle()
t.colormode(255)
nit.shape("turtle")
#nit.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


nit.pensize(1)


# color = ['#8aeba9', '#82c09f',  '#7a9494', '#8b8895',  '#9b7b96',  '#bc7d8a', '#de8891',  '#ff9397',  '#ff9a80',  '#ffa780']
# color_code = 0

def move_left(steps):
    nit.pencolor(random_color())
    nit.left(90)
    nit.forward(steps)


def move_right(steps):
    nit.pencolor(random_color())
    nit.right(90)
    nit.forward(steps)


def move_forward(steps):
    nit.pencolor(random_color())
    nit.forward(steps)


def move_backward(steps):
    nit.pencolor(random_color())
    nit.backward(steps)


def draw_a_figure(sides):
    angle = 360 / sides
    for _ in range(sides):
        nit.pencolor(random_color())
        nit.forward(100)
        nit.right(angle)

def draw_a_painting(radius, space, wide, height, start_x, start_y):
    nit.teleport(start_x, start_y)
    dot_spacing = wide + radius + space
    nit.penup()
    for i in range(height):
        current_y = start_y + i * dot_spacing
        nit.teleport(start_x, current_y)
        for x in range(wide):
            nit.pencolor(random.choice(color_list))
            nit.dot(radius)
            nit.forward(dot_spacing)

movement = [move_left, move_right, move_forward, move_backward]

def draw_spirograph(angle):
    for _ in range(int(360 / angle)):
        nit.pencolor(random_color())
        nit.setheading(nit.heading() + angle)
        nit.circle(100)

def random_walk(steps):
    chosen_move = random.choice(movement)
    chosen_move(steps)

def draw_shapes(start_num_of_angles, finish_num_of_angles):
    for shape_sides in range(start_num_of_angles, finish_num_of_angles):
        nit.pencolor(random_color())
        draw_a_figure(shape_sides)

#draw_spirograph(5)

draw_a_painting(30, 40, 10, 10, -350, -350)



screen = t.Screen()
screen.exitonclick()
