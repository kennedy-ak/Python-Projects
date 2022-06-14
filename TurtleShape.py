from turtle import Turtle,Screen
import random
colors=["cornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","dark slate gray",]
ken = Turtle()

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for i in range(num_of_sides):
        ken.forward(100)
        ken.right(angle)


for shape_side in range(3,10):
    ken.color(random.choice(colors))
    draw_shape(shape_side)








screen = Screen()

screen.exitonclick()