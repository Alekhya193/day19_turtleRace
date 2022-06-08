from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def moveForward():
    tim.forward(15)

def movebackwards():
    tim.backward(15)

def turnleft():
    tim.left(10)

def turnrightt():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(fun=moveForward,key="6")
screen.onkey(fun=movebackwards,key="4")
screen.onkey(turnleft,"7")
screen.onkey(turnrightt,"9")
screen.onkey(clear,"c")

screen.exitonclick()