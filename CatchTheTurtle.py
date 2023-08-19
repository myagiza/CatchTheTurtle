import random
import turtle
import time

# SCREEN
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
score = 0
game_over = False

# TURTLE
jack = turtle.Turtle()

# SCORE
def setup_score_Turtle():
    jack.penup()
    top_height = screen.window_height() / 2
    y = top_height * 1 * 0.9
    jack.setpos(0, y)
    jack.write("SCORE : 0", align="center", font=("Arial", 30, "bold"))
    jack.hideturtle()

setup_score_Turtle()

# Turtle Shape
gaming_turtle = turtle.Turtle()
gaming_turtle.penup()
gaming_turtle.shape("turtle")
gaming_turtle.shapesize(2.2)

# Handle click event
def handle_click(x, y):
    global score
    score += 1
    jack.clear()
    jack.write(arg=f"SCORE : {score}", align="center", font=("Arial", 30, "bold"))
    if score >= 10:
        gaming_over()

gaming_turtle.onclick(handle_click)

# Generate random position
def random_position():
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)
    return x, y

# Move gaming turtle to a random position
def gaming_turtle_position():
    while not game_over:
        gaming_turtle.penup()
        gaming_turtle.hideturtle()
        gaming_turtle.setpos(*random_position())
        gaming_turtle.showturtle()
        gaming_turtle.pendown()
        time.sleep(0.8)

gaming_over_turtle = turtle.Turtle()
gaming_over_turtle.penup()
gaming_over_turtle.hideturtle()

# Display game over message
def gaming_over():
    global game_over
    gaming_over_turtle.write(f"GAME OVER", align="center", font=("Arial", 50, "bold"))
    time.sleep(5)
    screen.bye()

# Start the game by positioning the gaming turtle
gaming_turtle_position()

# Start the turtle graphics event loop
turtle.mainloop()
