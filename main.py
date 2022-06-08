#Turtle race game
import turtle
from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
user_input=screen.textinput(title="Bet",prompt="make a Bet and Enter name of the turtle that you think will win: ")
# print(user_input)
colors=["violet","blue","green","yellow","orange","red"]
y_position=[-70,-40,-10,20,50,80]
all_turtles=[]

for i in range(0,6):
 new_turtle=Turtle(shape="turtle")
 new_turtle.color(colors[i])
 new_turtle.penup()
 new_turtle.goto(x=-230, y=y_position[i])
 all_turtles.append(new_turtle)

race_on=False
if user_input:
    race_on=True

while race_on:
    for new_turtle in all_turtles:

        if new_turtle.xcor()>230:
            race_on=False
            if new_turtle.pencolor()==user_input:
                print(f"you wom!!!. {new_turtle.pencolor()} is the winner")
            else:
                print(f"You lost!!!. {new_turtle.pencolor()} is the winner ")
        new_turtle.forward(random.randint(0,10))



screen.exitonclick()