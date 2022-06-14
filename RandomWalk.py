import turtle
from turtle import Turtle,Screen
from random import choice,randint


#colors=["cornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","dark slate gray",]
turtle.colormode(255)
def color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r ,g ,b )
    return color

ken = Turtle()
directions = [0,90,180,270]
for i in range(200):
    ken.pensize(10)
    ken.speed("fastest")
    ken.color(color())
    #ken.color(choice(colors))
    ken.forward(30)
    ken.setheading(choice(directions))




screen = Screen()
screen.exitonclick()