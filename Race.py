from turtle import Turtle,Screen
from random import randint

turtle_colors =["red","orange","yellow","green","blue","purple",]
y_cordinate=[-70,-40,-10,20,50,80,]


screen = Screen()
screen.setup(width=600,height=400)
users_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color?: ")
is_game_on = False
all_turtles=[]
for index in range(6):
    ken_the_turtle = Turtle()
    ken_the_turtle.shape("turtle")
    ken_the_turtle.penup()
    ken_the_turtle.color(turtle_colors[index])
    ken_the_turtle.goto(x=-280,y=y_cordinate[index])
    all_turtles.append(ken_the_turtle)

if users_bet:
    is_game_on =True


while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor()> 280:
            is_game_on=False
            winning_color =turtle.pencolor()
            if winning_color == users_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You loose! The {winning_color} turtle won the race ")
        random_distances = randint(0,10)
        turtle.forward(random_distances)



screen.exitonclick()