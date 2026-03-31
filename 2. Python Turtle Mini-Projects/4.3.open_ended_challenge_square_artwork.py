from turtle import *

def draw_square(size, line_color):
    color(line_color)
    begin_fill()
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    end_fill()

draw_square(100, 'red')

penup()
goto(150, 0)
pendown()
draw_square(80, 'blue')

penup()
goto(300, 0)
pendown()
draw_square(60, 'green')

done()