import random
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=700, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color :  ")
y_positions = [-70, -40, -10, 20, 50, 80]
colors = [ "red", "orange", "pink", "green", "blue", "purple"]
all_turtle = []


tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
tim.penup()
tom.penup()
tim.goto(x = 260, y = 200)
tom.goto(x = 260, y = 200)
tim.pendown()
tim.goto(x = 260, y = -200)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x= -300, y= y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 250:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner...")
            else:
                print(f"Booo, you lost! The {winning_color} turtle is the winner...")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()