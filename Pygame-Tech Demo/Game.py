import pygame
from Cube import Cube
from pygamegame import *

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

class Game(PygameGame):
    def init(self):
        self.cube = Cube(self.width/2, self.height/2)

    def mousePressed(self, x, y):
        cx, cy, r = self.cube.circle
        if distance(cx, cy, x, y) <= self.cube.length:
            self.cube.mouseUpdate()

    def keyPressed(self, keyCode, modifier):
        self.cube.keyUpdate(self.isKeyPressed)

    def redrawAll(self, screen):
        for i in range(len(self.cube.diamondList)): 
            diamond = self.cube.diamondList[i]
            color = [[0, 153, 255], [0, 51, 255], [0, 102, 255]]
            pygame.draw.polygon(screen, color[i], diamond)

game = Game()
game.run()