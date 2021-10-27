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


def vec_sum(vec1, vec2):
    return Vec(vec1.x+vec2.x, vec1.y+vec2.y)


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


def split(m):
    m1, m2 = Point(2, vec_sum(m.velocity, Vec(2, 0)), m.position), Point(2, vec_sum(m.velocity, Vec(0, 2)), m.position)


def interact():
    pass


def update(split_flag):
    for m in points:
        move(m)
        if split_flag:
            pass


for i in range(50):
    m0 = Point(2, Vec(randint(-20, 20), randint(-20, 20)), (randint(-100, 100), randint(-100, 100)))


j = 0

# simulation_loop
while 1:
    turtle.clear()
    split_flag = j % 15 == 0
    # split(points[0])
    update(split_flag)
    turtle.Screen().update()
    time.sleep(refresh_speed)
    j += 1

turtle.mainloop()
