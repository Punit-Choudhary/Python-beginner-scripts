import pygame
import numpy as np
from math import sin, cos, radians

pygame.init()

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]  # Updated to a 3D perspective projection matrix
])

cube_points = [
    np.matrix([-1, -1, 1]),
    np.matrix([1, -1, 1]),
    np.matrix([1, 1, 1]),
    np.matrix([-1, 1, 1]),
    np.matrix([-1, -1, -1]),
    np.matrix([1, -1, -1]),
    np.matrix([1, 1, -1]),
    np.matrix([-1, 1, -1])
]

def connect_points(screen, i, j, pts):
    ori = (0, 0, 0)
    pygame.draw.line(screen, ori, (pts[i][0], pts[i][1]), (pts[j][0], pts[j][1]))

class Cube:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.ax, self.ay, self.az = 0, 0, 0
        self.points = []

        for point in cube_points:
            rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
            rotated2d = np.dot(rotation_y, rotated2d)
            rotated2d = np.dot(rotation_x, rotated2d)
            projected2d = np.dot(projection_matrix, rotated2d)
            x = int(projected2d[0][0] * self.size) + self.pos[0]
            y = int(projected2d[1][0] * self.size) + self.pos[1]
            self.points.append([x, y])

    def rotate(self, rx, ry, rz):
        self.ax += rx * 0.01
        rotation_x = np.matrix([
            [1, 0, 0],
            [0, cos(self.ax), -sin(self.ax)],
            [0, sin(self.ax), cos(self.ax)],
        ])
        self.ay += ry * 0.01
        rotation_y = np.matrix([
            [cos(self.ay), 0, sin(self.ay)],
            [0, 1, 0],
            [-sin(self.ay), 0, cos(self.ay)],
        ])
        self.az += rz * 0.01
        rotation_z = np.matrix([
            [cos(self.az), -sin(self.az), 0],
            [sin(self.az), cos(self.az), 0],
            [0, 0, 1],
        ])

        for i, point in enumerate(cube_points):
            rotated = np.dot(rotation_x, point.reshape((3, 1)))
            rotated = np.dot(rotation_y, rotated)
            rotated = np.dot(rotation_z, rotated)
            projected2d = np.dot(projection_matrix, rotated)
            x = int(projected2d[0][0] * self.size) + self.pos[0]
            y = int(projected2d[1][0] * self.size) + self.pos[1]
            self.points[i] = [x, y]

    def move(self, x, y):
        self.pos = (self.pos[0] + x, self.pos[1] + y)
        for i, point in enumerate(self.points):
            self.points[i] = [point[0] + x, point[1] + y]

    def render(self, screen):
        for p in range(4):
            connect_points(screen, p, (p+1) % 4, self.points)
            connect_points(screen, p+4, ((p+1) % 4) + 4, self.points)
            connect_points(screen, p, (p+4), self.points)
        for point in self.points:
            pygame.draw.circle(screen, (70, 50, 240), point, 3)

# Initialize Pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Cube")

# Create a cube instance
cube = Cube(pos=(width//2, height//2), size=50)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rotate the cube
    cube.rotate(1, 1, 1)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Render and update display
    cube.render(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
