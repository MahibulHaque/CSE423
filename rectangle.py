import math
import numpy as np
from midpoint import drawLineMidPoint
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawRectangle(x1, y1, x2, y2, x3, y3, x4, y4,colors, filled=False ):
    y1=max(-430,y1)
    y2=max(-430,y2)
    y3=max(-450,y3)
    y4=max(-450,y4)

    drawLineMidPoint(x1, y1, x2, y2,colors)
    drawLineMidPoint(x2, y2, x3, y3,colors)
    drawLineMidPoint(x3, y3, x4, y4,colors)
    drawLineMidPoint(x4, y4, x1, y1,colors)
    if filled:
        x11 = x1
        x44 = x4
        y11 = y1
        y22 = y2
        while x11 != x2:
            drawLineMidPoint(x11, y1, x44, y4,colors)
            x11 += 1
            x44 += 1
        while y11 != y4:
            drawLineMidPoint(x1, y11, x2, y22,colors)
            y11 -= 1
            y22 -= 1



