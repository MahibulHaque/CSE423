import math
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def rotate3D(degree, axis, vertex=[], compound=False):
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
    if compound:
        if axis == "x":
            return rx
        elif axis == "y":
            return ry
        else:
            return rz
    else:
        if axis == "x":
            return np.matmul(rx, vertex)
        elif axis == "y":
            return np.matmul(ry, vertex)
        else:
            return np.matmul(rz, vertex)


def scale(a, b, vertex=[], compound=False):
    s = np.array([[a, 0, 0],
                  [0, b, 0],
                  [0, 0, 1]])
    if compound:
        return s
    else:
        return np.matmul(s, vertex)


def shear(a, b, vertex=[], compound=False):
    sh = np.array([[1, a, 0],
                   [b, 1, 0],
                   [0, 0, 1]])
    if compound:
        return sh
    else:
        return np.matmul(sh, vertex)


def compoundTransformation(trans1, trans2, vertex, degree=90, axis="x", a1=1, b1=1, a2=1, b2=1):
    if trans1 == "rotate3D" and trans2 == "scale":
        ct = np.matmul(rotate3D(degree, axis, compound=True), scale(a1, b1, compound=True))
        return np.matmul(ct, vertex)
    elif trans1 == "rotate3D" and trans2 == "shear":
        ct = np.matmul(rotate3D(degree, axis, compound=True), shear(a1, b1, compound=True))
        return np.matmul(ct, vertex)
    elif trans1 == "scale" and trans2 == "shear":
        ct = np.matmul(scale(a1, b1, compound=True), shear(a2, b2, compound=True))
        return np.matmul(ct, vertex)
