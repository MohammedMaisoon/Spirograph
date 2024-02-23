import random
import turtle
from turtle import *
Snake=Turtle()
turtle.colormode(255)
def random_colours():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour=(r,g,b)
    return random_colour
Snake.speed(100)
Snake.pensize(2)
colour=random_colours()
def spirograph(size):
    for _ in range(int(360 / size)):
        Snake.color(random_colours())
        Snake.circle(100)
        Snake.setheading(Snake.heading()+size)
spirograph(5)
screen=Screen()
screen.exitonclick()
