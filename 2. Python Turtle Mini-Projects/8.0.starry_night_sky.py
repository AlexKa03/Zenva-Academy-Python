from turtle import *
from random import *

bgcolor("black")
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

for i in range(100):
    xpos = randrange(-width // 2, width // 2)
    ypos = randrange(-height // 2, height // 2)
    draw_star(xpos, ypos)

print("done")

done()
