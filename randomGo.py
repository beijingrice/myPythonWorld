import turtle
import random
t = turtle.Pen()
while True:
    t.pensize(3)
    t.speed(10000)
    if random.randint(0, 1) == 0:
        t.right(random.randint(0, 180))
    if random.randint(0, 1) == 1:
        t.left(random.randint(0, 180))
    t.forward(random.randint(0, 10))
