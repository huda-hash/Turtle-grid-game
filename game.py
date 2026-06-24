import turtle
import random
screen = turtle.Screen()
screen.title("Grid Game")
screen.setup(600, 600)
screen.bgcolor("lightblue")

# Create a turtle to write everything on the play screen
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto (0,0)
writer.color ("purple")

# Create score-board on the top of the game window
move_writer = turtle.Turtle()
move_writer.hideturtle()
move_writer.penup()
move_writer.color("purple")
move_writer.goto(0, 250)

move_writer.write("Moves Left: 10", align="center", font=("Arial", 18, "bold"))

# Create a turtle to draw the grid
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(5)
pen.pencolor("white")

# Function to draw the grid
start = -200
cell = 80

moves = 0
game_over = False

# To randomise the finding position's co-ordinates
positions = [-160, -80, 0, 80, 160]
x_pos = random.choice(positions)
y_pos = random.choice(positions)

target = turtle.Turtle()
target.hideturtle()
target.shape("square")
target.color("red")
target.penup()
target.goto(x_pos, y_pos)
target.shapesize(3)

#grid drawing
for i in range (6):
    pen.penup()
    pen.goto(start, start + i * cell)
    pen.pendown()
    pen.goto(start+5*cell, start + i * cell)
for j in range (6):
    pen.penup()
    pen.goto(start + j * cell, start)
    pen.pendown()
    pen.goto(start + j * cell, start + 5*cell)

#creating the movable player in form of a square
player = turtle.Turtle()
player.shape("square")
player.color("gray", "pink")
player.penup()
player.shapesize(3)
player.goto(-160, -160)

# WASD creation
def update_moves():
    move_writer.clear()
    move_writer.write(
        f"Moves Left: {10 - moves}",
        align="center",
        font=("Arial", 18, "bold")
    )

def move_up():
    global moves, game_over

    if game_over:
        return
    
    y = player.ycor()

    if moves < 10 and y < 160:
        player.sety(y + 80)
        moves += 1
        update_moves()

    if player.xcor() == x_pos and player.ycor() == y_pos:
        writer.write("YOU WIN 🎉", align="center", font=("Arial", 24, "bold"))
        game_over= True

    if moves >=10:
        writer.write("Out of moves", align="center", font=("Arial", 24, "bold"))
        game_over= True

screen.listen()
screen.onkey(move_up, "w")

def move_down():
    global moves,game_over

    if game_over:
        return
    
    y = player.ycor()
    if moves < 10 and y > -160:
        player.sety(y - 80)
        moves += 1
        update_moves()

    if player.xcor() == x_pos and player.ycor() == y_pos:
        writer.write("YOU WIN 🎉", align="center", font=("Arial", 24, "bold"))
        game_over= True

    if moves >=10:
        writer.write("Out of moves", align="center", font=("Arial", 24, "bold"))
        game_over= True

screen.listen()
screen.onkey(move_down, "s")

def move_left():
    global moves, game_over

    if game_over:
        return
    x = player.xcor()
    if moves < 10 and x > -160:
        player.setx(x - 80)
        moves += 1
        update_moves()

    if player.xcor() == x_pos and player.ycor() == y_pos:
        writer.write("YOU WIN 🎉", align="center", font=("Arial", 24, "bold"))
        game_over= True

    if moves >=10:
        writer.write("Out of moves", align="center", font=("Arial", 24, "bold"))
        game_over= True

screen.listen()
screen.onkey(move_left, "a")

def move_right():
    global moves, game_over

    if game_over:
        return
    
    x = player.xcor()
    if moves < 10 and x < 160:
        player.setx(x + 80)
        moves += 1
        update_moves()

    if player.xcor() == x_pos and player.ycor() == y_pos:
        writer.write("YOU WIN 🎉", align="center", font=("Arial", 24, "bold"))
        game_over= True

    if moves >=10:
        writer.write("Out of moves", align="center", font=("Arial", 24, "bold"))
        game_over= True

screen.listen()
screen.onkey(move_right, "d")
turtle.done()
