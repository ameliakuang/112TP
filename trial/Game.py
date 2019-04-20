import pygame
from pygamegame import *
from Board import *
from Player import *
from Tiles import *
from Control import *
import utility

class Game(PygameGame):
    def init(self):
        self.mode = "splashScreen"
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

    def keyPressed(self, keyCode, modifier):
        if (self.mode == "splashScreen"): 
            self.splashScreenKeyPressed(keyCode, modifier)
        elif (self.mode == "playGame"):   
            self.playGameKeyPressed(keyCode, modifier)
        elif (self.mode == "help"):       
            self.helpKeyPressed(keyCode, modifier)

    def mousePressed(self, x, y):
        if (self.mode == "splashScreen"): 
            self.splashScreenMousePressed(x, y)
        elif (self.mode == "playGame"):   
            self.playGameMousePressed(x, y)
        elif (self.mode == "help"):       
            self.helpMousePressed(x, y)

    def timerFired(self, dt):
        if (self.mode == "splashScreen"): 
            self.splashScreenTimerFired(dt)
        elif (self.mode == "playGame"):   
            self.playGameTimerFired(dt)
        elif (self.mode == "help"):       
            self.helpTimerFired(dt)


    def redrawAll(self, screen):
        if (self.mode == "splashScreen"): 
            self.splashScreenRedrawAll(screen)
        elif (self.mode == "playGame"):   
            self.playGameRedrawAll(screen)
        elif (self.mode == "help"):       
            self.helpRedrawAll(screen)

    ########################
    # splashScreen mode
    ########################
    def splashScreenKeyPressed(self, keyCode, modifier):
        self.mode = "playGame"
    def splashScreenMousePressed(self, x, y):
        pass
    def splashScreenTimerFired(self, dt):
        pass
    def splashScreenRedrawAll(self, screen):
        pass

    ########################
    # playGame mode
    ########################
    def playGameKeyPressed(self, keyCode, modifier):
        pass
    def playGameMousePressed(self, x, y):
        pos = (x, y)
        if(self.beginRect.collidepoint(pos)):
            self.player.beginMoving = True
        elif(self.resetRect.collidepoint(pos)):
            self.resetState = True
        elif(self.menuRect.collidepoint(pos)):
            self.mode = "splashScreen"
    def playGameTimerFired(self, dt):
        if self.player.beginMoving:
            self.playerGroup.update(self.board)
    def playGameRedrawAll(self, screen):
        # Draw the board
        self.boardObject.draw(screen)
        # Draw the control
        self.controlBar.draw(screen, self.width, self.height)
        self.beginRect = screen.blit(self.begin.image, (self.begin.rect.x, self.begin.rect.y))
        self.resetRect = screen.blit(self.reset.image, (self.reset.rect.x, self.reset.rect.y))
        self.menuRect = screen.blit(self.menu.image, (self.menu.rect.x, self.menu.rect.y))


    ########################
    # help mode
    ########################
    def helpKeyPressed(self, keyCode, modifier):
        pass
    def helpMousePressed(self, x, y):
        pass
    def helpTimerFired(self, dt):
        pass
    def helpRedrawAll(self, screen):
        pass

game = Game()
game.run()