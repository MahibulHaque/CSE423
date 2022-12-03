from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_points(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glColor3f(255, 140, 0)
    glVertex2f(x, y)
    glEnd()


def Circlepoints(x, y, x0, y0):
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
    Circlepoints(x, y, x0, y0)  # Circlepoints(x+x0,y+y0)

    while (x < y):

        if d < 0:
            d = d + 2 * x + 3
            x = x + 1
        else:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        Circlepoints(x, y, x0, y0)


def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    eightWayCircle(400, 400, 300)
    glutSwapBuffers()


def eightWayCircle(x, y, radius):
    midPointCircle(x, y, radius)  # big one
    x_s = x + (radius / 2)
    y_s = y
    radius_s = radius / 2
    midPointCircle(x_s, y_s, radius_s)  # right
    midPointCircle(250, 400, radius_s)  #left
    midPointCircle(400, 250, radius_s) #bottom
    midPointCircle(400, 550, radius_s) #top

    midPointCircle(250 + 43, 550 - 43, radius_s) #topleft
    midPointCircle(550 - 43, 250 + 43, radius_s) #bottomright
    midPointCircle(250 + 43, 250 + 43, radius_s) #bottom left
    midPointCircle(550 - 43, 550 - 43, radius_s) #topright



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(650, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab-3-20101503")
glutDisplayFunc(screen)

glutMainLoop()