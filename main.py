import turtle
import time
from math import sqrt
from random import randint

turtle.hideturtle()
turtle.tracer(0, 0)
refresh_speed = 0.001
points = []
turtle.pensize(3)
G = 6.6742*10


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def vec_sum(vec1, vec2):
    """
    Sum of two vectors
    :param vec1: a Vec object (a vector)
    :param vec2: a Vec object (a vector)
    :return: the sum of vec1 and vec2
    """
    return Vec(vec1.x+vec2.x, vec1.y+vec2.y)


def vec_multiplication(vec1, k):
    """
    Multiplication of a vector by a real
    :param vec1: a Vec object (a vector)
    :param k: a real number
    :return: the multiplication of vec1 by k
    """
    return Vec(vec1.x*k, vec1.y*k)


class Point:
    def __init__(self, mass, velocity: Vec, position, name="m"):
        global points
        self.name = name
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
    """
    Calculate the position of the new position and draw m there
    :param m: a Point object
    """
    new_position = (m.position[0] + (m.velocity.x*refresh_speed), m.position[1] + (m.velocity.y*refresh_speed))
    m.position = new_position
    m.draw()


def split(m):
    m1, m2 = Point(2, vec_sum(m.velocity, Vec(2, 0)), m.position), Point(2, vec_sum(m.velocity, Vec(0, 2)), m.position)


def interact(m1, m2, info_flag):
    x1, y1 = m1.position
    x2, y2 = m2.position
    d = sqrt((abs(x1 - x2))**2 + (y1 - y2)**2)
    Fg = G*m1.mass*m2.mass/d**2
    if info_flag:
        print(Fg)
    calculate_new_velocity(m1, vec_multiplication(Vec(x2-x1, y2-y1), Fg), info_flag)
    calculate_new_velocity(m2, vec_multiplication(Vec(x1 - x2, y1 - y2), Fg), info_flag)


def calculate_new_velocity(m, force_sum, info_flag):
    """
    :param m: a Point object
    :param force_sum: the sum of all the forces that applied to m --> a vector
    """
    new_velocity = vec_sum(m.velocity, vec_multiplication(force_sum, refresh_speed/m.mass))
    if info_flag:
        print(m.name, new_velocity.x, new_velocity.y)
    m.velocity = new_velocity


def bounce(point, axis):
    """
    :param point:
    :param axis: True if y axis and False if x axis
    """

    if axis:
        point.velocity = Vec(point.velocity.x, -point.velocity.y)
    else:
        point.velocity = Vec(-point.velocity.x, point.velocity.y)
    # or: point.velocity = (axe*point.velocity.x, -1*axe*point.velocity.y) with axe = -1 or 1


def update(info_flag):
    """
    Updates the position and interaction of all the points
    """
    # interactions
    for i in range(len(points)):
        for j in points[i+1:]:
            interact(points[i], j, info_flag)
    for i in points:
        print(i.position[1])
        if 300 < i.position[1] < 301 or -300 < i.position[1] < -299:
            print("bounce")
            bounce(i, False)
        elif i.position[0] in (1000, -1000):
            bounce(i, True)
    for m in points:
        move(m)
        # Pour simuler une chute de balle avec parabole:
        # calculate_new_velocity(m, Vec(0, -800))


""" Two orbiting systems
m0 = Point(330000, Vec(0, 0), (0, 0))
# 10000 m/s --> sortir de l'attraction | 5000 --> orbite ronde
m1 = Point(1, Vec(5000, 0), (0, 180), "move point")
m2 = Point(500, Vec(5000, 0), (0, 200), "blabla")
"""
max_coords = 200
max_mass = 3000
min_mass = 100
max_speed = 3000
s = vec_sum(Vec(2, 5), Vec(0, -2*5))
print("somme", s.x, s.y)

for i in range(1):
    m1 = Point(randint(min_mass, max_mass), Vec(randint(-max_speed, max_speed), randint(-max_speed, max_speed)),
               (randint(-max_coords, max_coords), randint(-max_coords, max_coords)))

j = 0
# simulation_loop
while 1:
    turtle.clear()
    # info_flag = j % 100 == 0
    info_flag = False
    #split(points[0])
    update(info_flag)
    turtle.Screen().update()
    time.sleep(0.001)
    j += 1

turtle.mainloop()
