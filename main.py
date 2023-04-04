import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")

# Draw the finish line
line = turtle.Turtle()
line.penup()
line.goto(200, 0)
line.pendown()
line.goto(200, 200)
line.goto(200, -200)

# Create the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for i in range(6):
    turtle = turtle.Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-200, 30*i)
    turtles.append(turtle)

# Get user input for betting
bet = screen.textinput("Place your bet", "Which turtle will win the race? Enter a color:")

# Move the turtles randomly and check for winner
winner = None
while not winner:
    for turtle in turtles:
        turtle.forward(random.randint(1, 5))
        if turtle.xcor() >= 200:
            winner = turtle
            break

# Display the winner and payout
if winner.color()[0] == bet.lower():
    screen.textinput("Winner!", "Congratulations! Your turtle won! You win 100 points.")
else:
    screen.textinput("Loser!", "Sorry, your turtle lost. Better luck next time.")

# Exit on click
screen.exitonclick()
