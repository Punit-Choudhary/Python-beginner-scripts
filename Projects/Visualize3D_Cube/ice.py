import pygame
import numpy as np
from math import sin, cos


projection_matrix = np.matrix([
  [1, 0, 0],
  [0, 1, 0]
])


cube_points = [
  np.matrix([-1, -1, 1]),
  np.matrix([1, -1, 1]),
  np.matrix([1,  1, 1]),
  np.matrix([-1, 1, 1]),
  np.matrix([-1, -1, -1]),
  np.matrix([1, -1, -1]),
  np.matrix([1, 1, -1]),
  np.matrix([-1, 1, -1])
]


def connect_points(screen, i, j, points):
  pygame.draw.line(screen, (0,0,0), (points[i][0], points[i][1]), (points[j][0], points[j][1]))


class Cube:
  def __init__(self, pos, size):
    self.pos = pos
    
    self.size = size
    
    self.ax, self.ay, self.az = 0, 0, 0
    
    self.points = []
    
    rotation_x = np.matrix([
      [1, 0, 0],
      [0, cos(self.ax), -sin(self.ax)],
      [0, sin(self.ax), cos(self.ax)],
    ])
    
    rotation_y = np.matrix([
      [cos(self.ay), 0, sin(self.ay)],
      [0, 1, 0],
      [-sin(self.ay), 0, cos(self.ay)],
    ])
    
    rotation_z = np.matrix([
      [cos(self.az), -sin(self.az), 0],
      [sin(self.az), cos(self.az), 0],
      [0, 0, 1],
    ])
    
    for point in cube_points:
      rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
      rotated2d = np.dot(rotation_y, rotated2d)
      rotated2d = np.dot(rotation_x, rotated2d)
      
      projected2d = np.dot(projection_matrix, rotated2d)
      
      x = int(projected2d[0][0] * self.size) + self.pos[0]
      y = int(projected2d[1][0] * self.size) + self.pos[1]
      
      self.points.append([x, y])
  
  def rotate(self, rx, ry, rz):
    rotation_x, rotation_y, rotation_z = None, None, None
    
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
      rotated = point.reshape((3,1))
      
      rotated = np.dot(rotation_x, rotated)
      
      rotated = np.dot(rotation_y, rotated)
      
      rotated = np.dot(rotation_z, rotated)
      
      projected2d = np.dot(projection_matrix, rotated)
      
      x = int(projected2d[0][0] * self.size) + self.pos[0]
      y = int(projected2d[1][0] * self.size) + self.pos[1]
      
      self.points[i] = [x, y]
  
  def move(self, x, y):
    self.pos = (self.pos[0]+x, self.pos[1]+y)
    
    for i, point in enumerate(self.points):
      self.points[i] = [point[0]+x,point[1]+y]
  
  def render(self, screen): # improve this
    for p in range(4):
      connect_points(screen, p, (p+1) % 4, self.points)
      connect_points(screen, p+4, ((p+1) % 4) + 4, self.points)
      connect_points(screen, p, (p+4), self.points)
    
    for point in self.points:
      pygame.draw.circle(screen, (70,50,240), point, 3)
