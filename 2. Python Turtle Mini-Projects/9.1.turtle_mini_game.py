from turtle import *

def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()

def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()

def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()

def check_goal():
    if xcor() > (width // 2) - 300:
        color("brown")
        pencolor("white")
        write("YOU WIN!", font=("Arial", 25, "normal"))

        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")

speed(0)
# The course just gave general numbers for the below gotos, but as in my case, if you have larger
# monitor the given cords wont workd, I will make it work on any screen size regardless of the
# resolution and size
width = window_width()
height = window_height()

move_distance = 50

bgcolor("#C2B280")

penup()
goto((width // 2) - 300, height // 2)
pendown()

color("blue")

begin_fill()
goto(width // 2, height // 2)
goto(width // 2, -height // 2)
goto((width // 2) - 300, -height // 2)
goto((width // 2) - 300, height // 2)
end_fill()

penup()
goto(-(width // 2) + 300, 0)
color("green")
shape("turtle")

onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
listen()

done()
