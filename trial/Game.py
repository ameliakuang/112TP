import pygame
from pygamegame import *
from Board import *
from Player import *
from Tiles import *
from Control import *
import utility

class Game(PygameGame):
    def init(self):
        self.bgColor = (247, 202, 201)

        self.player = Player()
        self.playerGroup = pygame.sprite.GroupSingle(self.player)
        
        self.board = Board(5, self.player)

        # Control
        self.begin = Begin(self.width, self.height)
        self.beginMoving = False

        #self.controlBar = controlBar(self.width, self.height)


    # move the tiles onto the board
    def keyPressed(self, keyCode, modifier):
        pass

    # click on the game icon
    def mousePressed(self, x, y):
        pass

    def timerFired(self, dt):
        if self.beginMoving:
            self.playerGroup.move(self.board)

    def redrawAll(self, screen):
        self.board.draw(screen)
        #self.controlBar.draw(screen)
        #self.begin.draw(screen)

        


game = Game()
game.run()