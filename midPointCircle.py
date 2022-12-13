from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_points(x, y):
    glPointSize(1)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(x / (1600 / 2), y / (900 / 2), .4)
    glVertex2f(x / (1600 / 2), y / (900 / 2))  # jekhane show korbe pixel
    glEnd()


# Starting from here

def zoneCircleConvert(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)


def midPointCircle(x0, y0, radius):
    d = 1 - radius
    x = 0
    y = radius
    zoneCircleConvert(x, y, x0, y0)
    while x < y:
        if d >= 0:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        else:
            d = d + 2 * x + 3
            x = x + 1
        zoneCircleConvert(x, y, x0, y0)


def midPointFilledCircle(x0, y0, radius):
    while radius != 0:
        midPointCircle(x0, y0, radius)
        radius -= 1



