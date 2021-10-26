import turtle
import time
from random import randint

turtle.hideturtle()
turtle.tracer(0, 0)
refresh_speed = 0.01
points = []
turtle.pensize(3)


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point:
    def __init__(self, mass, velocity: Vec, position):
        global points
        self.mass = mass
        self.velocity = velocity
        self.position = position
        points.append(self)

    def draw(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.forward(1)


def move(m):
    new_position = (m.position[0] + (m.velocity.x*refresh_speed*10), m.position[1] + (m.velocity.y*refresh_speed*10))
    m.position = new_position
    m.draw()


def interact():
    pass


def update():
    for m in points:
        move(m)


m1 = Point(2, Vec(18, 0), (-4, 48))
m2 = Point(2, Vec(5, 3), (-52, -31))
for i in range(6):
    m0 = Point(2, Vec(randint(-20, 20), randint(-20, 20)), (randint(-100, 100), randint(-100, 100)))


# simulation_loop
while True:
    turtle.clear()
    update()
    turtle.Screen().update()
    time.sleep(refresh_speed)

turtle.mainloop()
