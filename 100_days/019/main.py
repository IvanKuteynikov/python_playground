import turtle as t
import random

nit = t.Turtle()
t.colormode(255)
nit.shape("turtle")
#nit.speed("fastest")

def move_left():
    nit.left(10)
    nit.forward(10)

def move_right():
    nit.right(10)
    nit.forward(10)

def move_forward():
    nit.forward(10)

def move_backward():
    nit.backward(10)

def clear():
    nit.home()
    nit.clear()

screen = t.Screen()

screen.listen()
screen.onkey(fun=move_forward, key='W')
screen.onkey(fun=move_backward, key='S')
screen.onkey(fun=move_left, key='A')
screen.onkey(fun=move_right, key='D')
screen.onkey(fun=clear, key='C')
screen.exitonclick()