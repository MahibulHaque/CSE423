from OpenGL.GL import *
from OpenGL.GLUT import *

time = .0

def create_shader(shader_type, source):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    return shader
def timer(value):
    global time
    if time>100.0:
        time = .0
    else:
        time +=.1
    glutPostRedisplay()
    glutTimerFunc(10, timer, 0)
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glUniform1f(timeLocation, time)