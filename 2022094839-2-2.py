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



def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # draw coordinate x axis and y axis printed
    glBegin(GL_LINES)
    glColor3ub(255,0,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0,255,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255,255,255)
    glVertex2fv( (T @ np.array([.0, .5, 1.]))[:-1] )
    glVertex2fv( (T @ np.array([.0, .0, 1.]))[:-1] )
    glVertex2fv( (T @ np.array([.5, .0, 1.]))[:-1] )
    glEnd()


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def main():
    if not glfw.init():
        return
    window = glfw.create_window(480,480, "2022094839-2-2",None,None)
    
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        # rotating core logic
        # this makes rotating moving animation

        t = glfw.get_time() # scala parameter
        s = np.sin(t) # s is an alias for sin theta
        c = np.cos(t) # c is an alias for cos theta

        T = np.array([[1.,0.,.4],[0.,1.,0.],[0.,0.,1.]])
        R = np.array([[c,-s,0.], [s,c,0.],  [0.,0.,1.]])

        # end of core logic.

        render(R @ T)
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()


# system info


# Ubuntu 20.04 and Python3 environment (OpenGL 3)

# PyOpenGL Platform configuration has been changed to 'glx'

# Latest version of OpenGL is recommended to run this program.

# This program was successfully tested with python3 from the shell environment.
