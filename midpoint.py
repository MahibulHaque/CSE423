from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def findzone(x1, y1, x2, y2):
    zone = -10
    dx = x2 - x1
    dy = y2 - y1
    if (abs(dx) >= abs(dy)):
        if (dx > 0 and dy >= 0):
            zone = 0
        elif (dx < 0 and dy >= 0):
            zone = 3
        elif (dx < 0 and dy <= 0):
            zone = 4
        elif (dx > 0 and dy <= 0):
            zone = 7

    else:
        if (dx >= 0 and dy > 0):
            zone = 1
        elif (dx <= 0 and dy < 0):
            zone = 5
        elif (dx <= 0 and dy > 0):
            zone = 2
        elif (dx >= 0 and dy < 0):
            zone = 6

    return zone


def convertZoneToZero(x11, y11, x22, y22, zone):
    if (zone == 0):
        x1 = x11
        y1 = y11
        x2 = x22
        y2 = y22
    elif (zone == 1):
        x1 = y11
        y1 = x11
        x2 = y22
        y2 = x22
    elif (zone == 2):
        x1 = y11
        y1 = -x11
        x2 = y22
        y2 = -x22
    elif (zone == 3):
        x1 = -x11
        y1 = y11
        x2 = -x22
        y2 = y22
    elif (zone == 4):
        x1 = -x11
        y1 = -y11
        x2 = -x22
        y2 = -y22
    elif (zone == 5):
        x1 = -y11
        y1 = -x11
        x2 = -y22
        y2 = -x22
    elif (zone == 6):
        x1 = -y11
        y1 = x11
        x2 = -y22
        y2 = x22
    elif (zone == 7):
        x1 = x11
        y1 = -y11
        x2 = x22
        y2 = -y22
    if zone == -10:
        return x11, y11, x22, y22
    else:
        return x1, y1, x2, y2


def convertZoneToRandom(x11, y11, zone):
    if (zone == 0):
        x1 = x11
        y1 = y11
    elif (zone == 1):
        x1 = y11
        y1 = x11

    elif (zone == 2):
        x1 = -y11
        y1 = x11

    elif (zone == 3):
        x1 = -x11
        y1 = y11

    elif (zone == 4):
        x1 = -x11
        y1 = -y11

    elif (zone == 5):
        x1 = -y11
        y1 = -x11

    elif (zone == 6):
        x1 = y11
        y1 = -x11

    elif (zone == 7):
        x1 = x11
        y1 = -y11

    if zone == -10:
        return x11, y11
    else:
        return x1, y1


def drawLineMidPoint(x1, y1, x2, y2, colors):
    zo = findzone(x1, y1, x2, y2)
    if (zo != 0):
        x1, y1, x2, y2 = convertZoneToZero(x1, y1, x2, y2, zo)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    x = x1
    y = y1
    while (x <= x2):
        x_1, y_1 = convertZoneToRandom(x, y, zo)
        draw_points(x_1, y_1, colors)
        if (d > 0):
            d = d + incNE
            x = x + 1
            y = y + 1
        else:
            d = d + incE
            x = x + 1


def draw_points(x, y, color):
    glPointSize(1)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(color[0] / 255, color[1] / 255, color[3]/255)
    glVertex2f(x / (1600 / 2), y / (900 / 2))  # jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
