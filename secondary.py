import pygame as pg
from pygame import gfxdraw
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from midPointCircle import midPointFilledCircle, midPointCircle
import math

from midpoint import drawLineMidPoint


class Cardioid:
    def __init__(self, app):
        self.app = app
        self.radius = 400
        self.num_lines = 100
        self.translate = 0, 0
        self.counter, self.inc = 0, 0.01

    def get_color(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) if 0 < self.counter < 1 else (
            max(min(self.counter, 1), 0), -self.inc)

        return pg.Color('red').lerp('green', self.counter)

    def draw(self):
        time = pg.time.get_ticks()
        self.radius = 350 + 50 * abs(math.sin(time * 0.004) - 0.5)
        factor = 2 + 0.0001 * time

        midPointCircle(0, 0, self.radius)

        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            x_1 = int(self.radius * math.cos(theta))
            y_1 = int(self.radius * math.sin(theta))

            x_2 = int(self.radius * math.cos(factor * theta))
            y_2 = int(self.radius * math.sin(factor * theta))

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
