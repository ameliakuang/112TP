import pygame
from pygamegame import *
from Board import *
from Player import *
from Tiles import *
import utility

class Game(PygameGame):
    def init(self):
        self.bgColor = (220, 129, 0)

        self.player = Player()
        self.playerGroup = pygame.sprite.GroupSingle(self.player)
        
        self.board = Board(5, self.player)

    def mousePressed(self, x, y):
        pass
        #if(click on a tile):
            ##elf.




        self.player.move(self, x, y)
        #print(screenCenterX, self.player.rect.centerx)
        self.player.move(screenCenterX, screenCenterY, x, y)
        self.board = Board(5, self.player)
        #print(self.player.rect.centerx)

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        self.board.draw(screen)
        utility.helloWorld()


game = Game()
game.run()