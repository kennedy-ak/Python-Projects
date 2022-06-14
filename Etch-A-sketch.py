from turtle import Turtle,Screen

ken_the_turtle = Turtle()
screen = Screen()

def move_forward():
    ken_the_turtle.forward(10)

def move_backwards():
    ken_the_turtle.backward(10)
def counter_clockwise():
    ken_the_turtle.left(45)
def clockwise():
    ken_the_turtle.right(45)

def clear():
    ken_the_turtle.reset()


screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backwards,key="s")
screen.onkey(fun=counter_clockwise,key="a")
screen.onkey(fun=clockwise,key="d")
screen.onkey(fun=clear,key="c")

screen.exitonclick()