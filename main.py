from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen_width = 500
screen_height = 400
screen.setup(500, 400)

user_bet = screen.textinput(title="Place you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow2", "green", "blue", "purple"]
y_positions = [-80, -40, -0, 40,  80, 120]
is_race_on = False
all_turtles = []

# racers
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
