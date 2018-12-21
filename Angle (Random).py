import turtle, random
angle = random.randint(30,360)
f = 1
bar = turtle.Turtle()
bar.speed(0)
while True:
    bar.forward(f)
    bar.right(angle)
    f += 1
