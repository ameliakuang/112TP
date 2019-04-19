import pygame
from pygamegame import *
from Board import *
from Player import *
from Tiles import *
from Control import *
import utility

class Game(PygameGame):
    def init(self):
        # Background color
        self.bgColor = (247, 202, 201)

        # Player
        self.player = Player()
        self.playerGroup = pygame.sprite.GroupSingle(self.player)
        # Board
        ## self.boardObject is an object of the class Board
        ## self.board is the 2d list representation of the board object
        self.boardObject = Board(5, self.player)
        self.board = self.boardObject.board

        # Control
        self.begin = Begin(self.width, self.height)
        self.beginMoving = False

        self.reset = Reset(self.width, self.height)
        self.resetState = False

        self.menu = Menu(self.width, self.height)

        self.controlBar = controlBar(self.width, self.height)

    # move the tiles onto the board
    def keyPressed(self, keyCode, modifier):
        pass

    # click on the game icon and the ball can move
    def mousePressed(self, x, y):
        pos = (x, y)
        if(self.beginRect.collidepoint(pos)):
            self.player.beginMoving = True
        elif(self.resetRect.collidepoint(pos)):
            self.resetState = True
        elif(self.menuRect.collidepoint(pos)):
            pass

    # move the ball
    def timerFired(self, dt):
        if self.player.beginMoving:
            self.playerGroup.update(self.board)

    def redrawAll(self, screen):
        self.boardObject.draw(screen)
        self.controlBar.draw(screen, self.width, self.height)
        self.beginRect = screen.blit(self.begin.image, (self.begin.rect.x, self.begin.rect.y))
        self.resetRect = screen.blit(self.reset.image, (self.reset.rect.x, self.reset.rect.y))
        self.menuRect = screen.blit(self.menu.image, (self.menu.rect.x, self.menu.rect.y))

game = Game()
game.run()