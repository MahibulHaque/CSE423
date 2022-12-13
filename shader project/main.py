import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

verticies = (
    (100, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


# def Cube():
#     glBegin(GL_LINES)
#     for edge in edges:
#         for vertex in edge:
#             glVertex3fv(verticies[vertex])
#     glEnd()


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

    return x1, y1


def drawLineMidPoint(x1, y1, x2, y2):
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
        draw_points(x_1, y_1)
        if (d > 0):
            d = d + incNE
            x = x + 1
            y = y + 1
        else:
            d = d + incE
            x = x + 1


def draw_points(x, y):
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)
    glBegin(GL_LINES)
    # call the draw methods here
    # draw_points(300, 40)
    drawLineMidPoint(50, 300, 50, 400)  # vertical
    drawLineMidPoint(150, 200, 150, 300)  # vertical
    drawLineMidPoint(50, 200, 150, 200)  # horizontal
    drawLineMidPoint(50, 300, 150, 300)  # horizontal
    drawLineMidPoint(50, 400, 150, 400)  # horizontal
    drawLineMidPoint(200, 200, 200, 400)  # vertical

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 2 (ID:19301051)")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
