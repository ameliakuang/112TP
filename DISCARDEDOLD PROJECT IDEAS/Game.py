import pygame
import os, random, math
from pygamegame import *
from Tile import *

class Game(PygameGame):
    def init(self):
        self.bgColor = (0,0,0)
        self.rows = 2
        self.cols = 2
        self.tiles = pygame.sprite.Group()
        for row in range(self.rows):
            for col in range(self.cols):
                planeCenterX = self.width//2
                planeCenterY = self.height//2
                centerx, centery = getPosition(self, planeCenterX, planeCenterY, row, col)
                tile = normalTile(centerx, centery)
                self.tiles.add(tile)

    def getPosition(self, planeCenterX, planeCenterY, row, col):
        centerx, centery = None, None
        tileDiagonal = ((self.width/2)-10)/row
        if(row+col % 2 == 0):
            centerx = planeCenterX
            centery = planeCenterY+(tileDiagonal)*(0.5+row)
        else:
            centerx = 




    def redrawAll(self, screen):
        self.tiles.draw(screen)
        pygame.draw.rect(screen, (122,0,0), (300, 200, 30, 20))

game = Game()
game.run()
