#import colorgram as cg
import turtle
import random
#color_list = cg.extract('image.jpg', 20)
turtle.colormode(255)
ken = turtle.Turtle()

#for color in color_list:
  #  r = color.rgb.r
   # g = color.rgb.g
    #b = color.rgb.b
   # new_color =(r ,g ,b)
  #  rgb_colors.append(new_color)

    #rgb_colors.append(color.rgb)


colors=[ (235, 243, 251), (234, 225, 93), (233, 49, 133), (213, 158, 105), (115, 177, 214), (212, 133, 177), (196, 75, 23), (193, 163, 14), (36, 103, 168), (33, 192, 111), (11, 22, 65), (235, 225, 2), (183, 45, 124), (122, 189, 156), (189, 10, 68), (23, 28, 169), (237, 161, 203)]
ken.hideturtle()
ken.setheading(230)
ken.penup()
ken.forward(250)
ken.pendown()

ken.setheading(0)
number_of_dots = 100
for dot_counts in range(1,number_of_dots+1):
    ken.speed("fastest")
    ken.penup()
    ken.dot(20,random.choice(colors))
    ken.forward(50)
    ken.penup()
    if dot_counts % 10 ==0:
        ken.setheading(90)
        ken.forward(50)
        ken.setheading(180)
        ken.forward(500)
        ken.setheading(0)




screen = turtle.Screen()
screen.exitonclick()

