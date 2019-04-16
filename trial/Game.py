import pygame
from pygamegame import *
from Board import *
from Player import *

class Game(PygameGame):
    def init(self):
        self.bgColor = (220, 129, 0)
        self.player = Player()
        self.board = Board(5, self.player)

    def mousePressed(self, x, y):
        screenCenterX = self.width//2
        screenCenterY = self.height//2
        #print(screenCenterX, self.player.rect.centerx)
        self.player.move(screenCenterX, screenCenterY, x, y)
        self.board = Board(5, self.player)
        #print(self.player.rect.centerx)

    def timerFired(self, dt):
        pass


    def redrawAll(self, screen):
        self.board.draw(screen)

game = Game()
game.run()