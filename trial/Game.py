import pygame
from pygamegame import *
from Board import *
from Player import *
from Tiles import *
from Control import *
import utility

class Game(PygameGame):
    def init(self):
        self.mode = "help"
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
        elif (self.mode == "levelSelection"):
            self.levelSelectionKeyPressed(keyCode, modifier)

    def mousePressed(self, x, y):
        if (self.mode == "splashScreen"): 
            self.splashScreenMousePressed(x, y)
        elif (self.mode == "playGame"):   
            self.playGameMousePressed(x, y)
        elif (self.mode == "help"):       
            self.helpMousePressed(x, y)
        elif (self.mode == "levelSelection"):
            self.levelSelectionMousePressed(x,y)

    def timerFired(self, dt):
        if (self.mode == "splashScreen"): 
            self.splashScreenTimerFired(dt)
        elif (self.mode == "playGame"):   
            self.playGameTimerFired(dt)
        elif (self.mode == "help"):       
            self.helpTimerFired(dt)
        elif (self.mode == "levelSelection"):
            self.levelSelectionTimerFired(dt)


    def redrawAll(self, screen):
        if (self.mode == "splashScreen"): 
            self.splashScreenRedrawAll(screen)
        elif (self.mode == "playGame"):   
            self.playGameRedrawAll(screen)
        elif (self.mode == "help"):       
            self.helpRedrawAll(screen)
        elif (self.mode == "levelSelection"):
            self.levelSelectionRedrawAll(screen)

    ########################
    # splashScreen mode
    ########################
    def splashScreenKeyPressed(self, keyCode, modifier):
        self.mode = "playGame"
    def splashScreenMousePressed(self, x, y):
        pos = (x, y)
        if(self.levelRect.collidepoint(pos)):
            self.mode = "levelSelection"
    def splashScreenTimerFired(self, dt):
        pass
    def splashScreenRedrawAll(self, screen):
        # Draw the title and the level selection
        font1 = pygame.font.SysFont("copperplatettc", 120)

        self.titleSurface = font1.render("Pendo", True, (255, 255, 255))
        self.titleRect = self.titleSurface.get_rect()
        self.titleRect.center = (self.width//2, self.height//2-70)
        screen.blit(self.titleSurface, self.titleRect)

        font2 = pygame.font.SysFont("americantypewriterttc", 50)

        self.levelSurface = font2.render("Level Selection", True, (255, 255, 255), (205,140,149))
        self.levelRect = self.levelSurface.get_rect()
        self.levelRect.center = (self.width//2, self.height//2+50)
        screen.blit(self.levelSurface, self.levelRect)

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
            self.mode = "levelSelection"

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
        font3 = pygame.font.Font("freesansbold.ttf", 20)

        textSurface0 = font3.render("Instruction:))))", True, (255, 255, 255))
        screen.blit(textSurface0, ((self.width/2-300, self.height/2-220)))

        textSurface1 = font3.render("~Use your mouse to drag a tile to any empty spot~", True, (255, 255, 255))
        screen.blit(textSurface1, (self.width/2-300, self.height/2-170))

        textSurface2 = font3.render("~Build up the path to the target blue spot~", True, (255, 255, 255))
        screen.blit(textSurface2, (self.width/2-300, self.height/2-120))

        textSurface3 = font3.render("~Click on the right arrow for the ball to roll~", True, (255, 255, 255))
        screen.blit(textSurface3, (self.width/2-300, self.height/2-70))

        textSurface4 = font3.render("~Click on the menu button to go back to Level Selection Page~", True, (255, 255, 255))
        screen.blit(textSurface4, (self.width/2-300, self.height/2-20)) 

        textSurface5 = font3.render("~Click on the restart button to restart the game~", True, (255, 255, 255))
        screen.blit(textSurface5, (self.width/2-300, self.height/2+30))      

        textSurface6 = font3.render("~E~N~J~O~Y~", True, (255, 255, 255))
        screen.blit(textSurface6, (self.width/2-60, self.height/2+80))                


    ########################
    # levelSelection mode
    ########################
    def levelSelectionKeyPressed(self, keyCode, modifier):
        pass
    def levelSelectionMousePressed(self, x, y):
        self.mode = "help"
    def levelSelectionTimerFired(self, dt):
        pass
    def levelSelectionRedrawAll(self, screen):
        font2 = pygame.font.SysFont("americantypewriterttc", 50)

        self.levelSelectionSurface = font2.render("Level Selection", True, (255, 255, 255),(205,140,149))
        self.levelSelectionRect = self.levelSelectionSurface.get_rect()
        self.levelSelectionRect.center = (self.width//2, 40)
        screen.blit(self.levelSelectionSurface, self.levelSelectionRect)



    

game = Game()
game.run()