from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\classes"))
import game # need for game.Cell class and game.MAP_SIZE

# Parameters of grid and window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = float(max(SCREEN_WIDTH // game.MAP_SIZE, SCREEN_HEIGHT // game.MAP_SIZE))

# # generate test map
# new_map1 = [[game.Cell.Empty for _ in range(game.MAP_SIZE)] for _ in range(game.MAP_SIZE)]

# # spawn wall on edges
# for i in range(game.MAP_SIZE):
#     for j in range(game.MAP_SIZE):
#         if i == 0 or i == 29 or j == 0 or j == 29:
#             new_map1[i][j] = game.Cell.Wall

# # spawn snake and food
# new_map1[15][15] = game.Cell.Snake
# new_map1[15][16] = game.Cell.Snake
# new_map1[20][20] = game.Cell.Food

# # Create copy of map for test animation
# new_map2 = []
# for i in range(game.MAP_SIZE):
#     new_map2.append(new_map1[i].copy())

# # Make little changes in map
# new_map2[15][15] = game.Cell.Empty
# new_map2[15][16] = game.Cell.Empty
# new_map2[15][24] = game.Cell.Snake
# new_map2[15][25] = game.Cell.Snake


# Class for Graphic
class GUI:

    # Init map
    def __init__(self, new_map):
        self.new_map = new_map


        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) # type: ignore
        glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        glutInitWindowPosition(100, 100)
        glutCreateWindow("Snake")
        
        glPointSize(GRID_SIZE)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glClearColor(0.93, 0.99, 0.43, 1.0)
        gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
        glutSwapBuffers()

    # Func that define scene to draw
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # type: ignore
        glBegin(GL_POINTS)
        print(self.new_map)
        for i in range(game.MAP_SIZE * 2):
            for j in range(game.MAP_SIZE * 2):
                match self.new_map[i // 2][j // 2]:  # Multiplication by 2 and division need for more tight location
                    # grids
                    case game.Cell.Empty:
                        continue
                    case game.Cell.Food:
                        glColor3f(1.0, 0.22, 0.0)
                    case game.Cell.Snake: 
                        glColor3f(0.2, 0.5, 0.4)
                    case game.Cell.Wall:
                        glColor3f(0.24, 0.15, 0.0)
                glVertex2f((i + 1) * GRID_SIZE // 2, (j + 1) * GRID_SIZE // 2)
        glEnd()

        glFlush()

    # Method that draw scene
    def draw(self):
        # Init GLUT
        # Init window
        #glutMainLoop()
        self.display()


# new = GUI(new_map1)
# new.draw()
# glutMainLoop()  # That need for keeping window open and this is problem for animation
