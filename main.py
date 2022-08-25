import turtle as t
import random


is_game_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
colors = ["red", "blue", "green", "yellow", "pink", "purple", "orange"]
y_positions = [-100, -70, -40, -10, 20, 50, 80]
all_turtles = []
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win? Enter a name: ").lower()

for index in range(0, 7):
    tim = t.Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[index])
    all_turtles.append(tim)


if user_bet:
    is_game_on = True


while is_game_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won! The {winning_color} turtle is a winner!")
            else:
                print(f"you lost! {winning_color} turtle is a winner!")

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
