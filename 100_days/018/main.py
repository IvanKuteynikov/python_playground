import turtle as t
import random

nit = t.Turtle()
t.colormode(255)
nit.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


nit.pensize(7)


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
        nit.pencolor(color[color_code])
        nit.forward(100)
        nit.right(angle)


movement = [move_left, move_right, move_forward, move_backward]

x = 1000
while x > 0:
    chosen_move = random.choice(movement)
    chosen_move(15)
    x -= 1
print("end")

# for shape_sides in range(3, 11):
#    draw_a_figure(shape_sides)
#    color_code += 1


screen = t.Screen()
screen.exitonclick()
