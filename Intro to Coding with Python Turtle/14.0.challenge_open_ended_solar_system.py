from turtle import *

bgcolor("black")
speed(0)

# Sun
color("dark orange")
begin_fill()
circle(60)
end_fill()

penup()
forward(100)
pendown()

# Mercury
color("gray")
begin_fill()
circle(20)
end_fill()

penup()
forward(80)
pendown()

# Venus
color("dark goldenrod")
begin_fill()
circle(40)
end_fill()

penup()
forward(90)
pendown()

# Earth
color("forest green")
begin_fill()
circle(30)
end_fill()

# TODO: Add more planets here! And since i want to keep the sizes the same I will calculate what the distance should be abd how bigh the planets should be too. I will use the distance from the sun to the planets and the size of the planets to calculate how big they should be and how far they should be from each other.

hideturtle()

done()
