# Ubuntu 20.04 and Python3 environment (OpenGL 3)

# PyOpenGL Platform configuration has been changed to 'glx'

# Latest version of OpenGL is recommended to run this program.

import OpenGL
import os
os.environ["PYOPENGL_PLATFORM"] = "glx"
import numpy as np
import glfw
import OpenGL.GL
from OpenGL.GL import *

val = GL_TRIANGLE_FAN

def createPolyShape(n, radius):
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    for angle in angles:
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        glVertex3f(x, y, 0.0)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    radius = 0.5
    n = 12
    global val
    glBegin(val)
    createPolyShape(n, radius)
    glEnd()
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def key_callback(window, key, scancode, action, mods):
    global val
    primitive = {glfw.KEY_1: GL_POINTS,
            glfw.KEY_2: GL_LINES, 
            glfw.KEY_3: GL_LINE_STRIP, 
            glfw.KEY_4: GL_LINE_LOOP, 
            glfw.KEY_5: GL_TRIANGLES, 
            glfw.KEY_6: GL_TRIANGLE_STRIP, 
            glfw.KEY_7: GL_TRIANGLE_FAN, 
            glfw.KEY_8: GL_QUADS, 
            glfw.KEY_9: GL_QUAD_STRIP, 
            glfw.KEY_0: GL_POLYGON}

    if key >= glfw.KEY_0 and key <= glfw.KEY_9:
        if action == glfw.PRESS:
            val = primitive[key]
        elif action == glfw.RELEASE:
            print('key released')
        elif action == glfw.REPEAT:
            print('key repeated')




def main():
    if not glfw.init():
        return
    window = glfw.create_window(480,480, "2022094839-2-1",None,None)
    
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, key_callback)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        render()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()



# system info


# Ubuntu 20.04 and Python3 environment (OpenGL 3)

# PyOpenGL Platform configuration has been changed to 'glx'

# Latest version of OpenGL is recommended to run this program.

# This program was successfully tested with python3 from the shell environment

