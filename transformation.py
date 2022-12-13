import math
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def rotate3D(degree, axis, vertex):
    a = math.cos(math.radians(degree))
    b = math.sin(math.radians(degree))

    rx = np.array([[1, 0, 0],
                   [0, a, -b],
                   [0, b, a]])
    ry = np.array([[a, 0, b],
                   [0, 1, 0],
                   [-b, 0, a]])
    rz = np.array([[a, -b, 0],
                   [b, a, 0],
                   [0, 0, 1]])
    if axis == "x":
        return np.matmul(rx, vertex)
    elif axis == "y":
        return np.matmul(ry, vertex)
    else:
        return np.matmul(rz, vertex)


def scale(factor1, factor2, vertex):
    s = np.array([[factor1, 0, 0],
                  [0, factor2, 0],
                  [0, 0, 1]])
    return np.matmul(s, vertex)


def shear(a, b, vertex):
    sh = np.array([[1, a, 0],
                   [b, 1, 0],
                   [0, 0, 1]])
    return np.matmul(sh, vertex)
