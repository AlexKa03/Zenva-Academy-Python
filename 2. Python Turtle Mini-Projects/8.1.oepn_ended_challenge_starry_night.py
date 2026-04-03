from turtle import *
from random import *

bgcolor("midnight blue")
hideturtle()

speed(0)

width = window_width()
height = window_height()

def draw_star(xpos, ypos):
    size = randrange(4, 10)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")

def draw_moon(xpos, ypos):
    size = randrange(150, 265)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")

for i in range(1000):
    xpos = randrange(-width // 2, width // 2)
    ypos = randrange(-height // 2, height // 2)
    draw_star(xpos, ypos)

xpos = randrange(-width // 2, width // 2)
ypos = randrange(-height // 2, height // 2)
draw_moon(xpos, ypos)

print("done")

done()
