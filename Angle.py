# EDIT ANGLE BEFORE YOU BEGIN! RECCOMENDED ANGLES: 60, 90, 120, 127, 179
import turtle
angle = 90
f = 1
bar = turtle.Turtle()
bar.speed(0)
while True:
    bar.forward(f)
    bar.right(angle)
    f += 1
