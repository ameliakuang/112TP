import pygame
from pygamegame import *
from Board import *
from Player import *
from Tiles import *
import utility

class Game(PygameGame):
    def init(self):
        self.bgColor = (247, 202, 201)

        self.player = Player()
        self.playerGroup = pygame.sprite.GroupSingle(self.player)
        
        self.board = Board(5, self.player)


    # move the tiles onto the board
    def keyPressed(self, x, y):
        pass

    # click on the game icon
    def mousePressed(self, x, y):
        pass
        

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        self.board.draw(screen)

        


game = Game()
game.run()