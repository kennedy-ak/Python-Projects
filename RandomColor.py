import turtle
from turtle import *
from random import *

turtle.colormode(255)
def color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r ,g ,b )
    return color

ken = Turtle()
for i in range(75):
    ken.speed("fastest")
    ken.color(color())
    ken.circle(100)
    ken.right(5)






screen = Screen()
screen.exitonclick()
