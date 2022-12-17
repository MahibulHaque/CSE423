import random

import pygame as pg
from pygame import gfxdraw
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from midPointCircle import midPointFilledCircle, midPointCircle
import math
import numpy as np
from scipy.io.wavfile import read
from midpoint import drawLineMidPoint
from rectangle import drawRectangle
from transformation import rotate3D, scale

samplerate, data = read("music.wav")

print(f"number of channels = {data.shape[0]}")
number_of_channels = 2
length = data.shape[0] / samplerate
print(samplerate)


class Cardioid:
    def __init__(self, app):
        self.app = app
        self.radius = int(input("Enter the initial radius: "))
        self.num_lines = int(input("Enter the number of lines you want inside the circle: "))
        self.translate = 0, 0
        self.counter, self.inc = 0, 0.01
        self.sec = 0

    def get_color(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) if 0 < self.counter < 1 else (
            max(min(self.counter, 1), 0), -self.inc)

        return pg.Color('red').lerp('green', self.counter)

    def draw(self):
        time = pg.time.get_ticks()

        self.sec += 1

        self.radius = 150 + 50 * abs(math.sin(time * 0.004) - 0.5)
        factor = 2 + 0.0001 * time
        factor2 = 1.5 * abs(math.sin(time * 0.004) - 0.5)

        midPointCircle(0, 150, self.radius)
        v1 = np.array([[-800],
                       [-430],
                       [1]])
        v2 = np.array([[-750],
                       [-430],
                       [1]])
        v3 = np.array([[-750],
                       [-450],
                       [1]])
        v4 = np.array([[-800],
                       [-450],
                       [1]])
        v11 = scale(1, factor2, v1)
        v22 = scale(1, factor2, v2)
        x_val = 0
        for i in range(32):
            translate_y = random.randint(-100, 0)
            drawRectangle(int(v1[0][0]) + x_val, int(v11[1][0])+translate_y, int(v2[0][0]) + x_val, int(v22[1][0])+translate_y,
                          int(v3[0][0]) + x_val, int(v3[1][0]),
                          int(v4[0][0]) + x_val, int(v4[1][0]), self.get_color())
            x_val += 50

        # drawRectangle(int(v1[0][0]), int(v11[1][0]), int(v2[0][0]), int(v22[1][0]), int(v3[0][0]), int(v3[1][0]),
        #               int(v4[0][0]), int(v4[1][0]),
        #               self.get_color())
        # drawRectangle(int(v1[0][0] + 50), int(v11[1][0]) - 140, int(v2[0][0] + 50), int(v22[1][0]) - 140,
        #               int(v3[0][0] + 50),
        #               int(v3[1][0]),
        #               int(v4[0][0] + 50), int(v4[1][0]),
        #               self.get_color())
        # drawRectangle(int(v1[0][0] + 100), int(v11[1][0]) - 70, int(v2[0][0] + 100), int(v22[1][0]) - 70,
        #               int(v3[0][0] + 100),
        #               int(v3[1][0]),
        #               int(v4[0][0] + 100), int(v4[1][0]),
        #               self.get_color())
        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            x_1 = int(self.radius * math.cos(theta))
            y_1 = int(self.radius * math.sin(theta))+150

            x_2 = int(self.radius * math.cos(factor * theta))
            y_2 = int(self.radius * math.sin(factor * theta))+150

            drawLineMidPoint(x_1, y_1, x_2, y_2, self.get_color())


class App:
    def __init__(self):
        glutInitWindowPosition(0, 0)
        self.screen = pg.display.set_mode((1600, 900), DOUBLEBUF | OPENGL)
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)

    def draw(self):
        self.screen.fill('black')
        self.cardioid.draw()
        pg.display.flip()

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


if __name__ == '__main__':
    app = App()
    app.run()
