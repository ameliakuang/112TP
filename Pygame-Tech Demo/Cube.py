import pygame
import math, random
from pygamegame import *


class Cube(PygameGame):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.length = cy *2 // 5
        self.angle = math.pi*(2/3)
        self.diamondList = Cube.getDiamonds(self)
        self.circle = (cx, cy, cy *2 // 5)


    @staticmethod
    def getDiamonds(self):
        diamondList = [[[0, 0]] * 4 for i in range(3)]
        downCoordinates = []
        cx, cy = self.cx, self.cy
        for i in range(3):
            diamondList[i][2] = [cx, cy]

        for i in range(3):
            topx1 = cx + self.length * math.cos(i*self.angle+math.pi/2)
            topy1 = cy - self.length * math.sin(i*self.angle+math.pi/2)
            diamondList[i][0] = [topx1, topy1]
        for i in range(3):
            downx1 = cx + self.length * math.cos(i*self.angle-math.pi/2)
            downy1 = cy - self.length * math.sin(i*self.angle-math.pi/2)
            downCoordinates.append([downx1, downy1])
        diamondList[0][1] = downCoordinates[1]
        diamondList[0][3] = downCoordinates[2]
        diamondList[2][1] = downCoordinates[0]
        diamondList[2][3] = downCoordinates[1]
        diamondList[1][1] = downCoordinates[2]
        diamondList[1][3] = downCoordinates[0]      
        return diamondList

    def mouseUpdate(self):
        dire = random.choice([[5, 0], [0, 5], [-5, 0], [0, -5]])
        self.cx += dire[0]
        self.cy += dire[1]
        self.diamondList = Cube.getDiamonds(self)

    def keyUpdate(self, keysDown):
        if keysDown(pygame.K_UP):
            self.length = min(150, self.length+10)
            self.diamondList = Cube.getDiamonds(self)
        elif keysDown(pygame.K_DOWN):
            self.length = max(self.length - 10, 10)
            self.diamondList = Cube.getDiamonds(self)

