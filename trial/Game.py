import pygame
from pygamegame import *
from Board import *
from Player import *
from Tiles import *
from Control import *
from Scene import *
import utility
import copy

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
        self.board = copy.deepcopy(self.boardObject.board)

        # Control
        self.begin = Begin(self.width, self.height)
        self.beginMoving = False

        self.reset = Reset(self.width, self.height)
        self.resetState = False

        self.menu = Menu(self.width, self.height)

        self.controlBar = controlBar(self.width, self.height)


        self.dragFlag = False
        self.objectDragged = None

    def keyPressed(self, keyCode, modifier):
        if (self.mode == "splashScreen"): 
            self.splashScreenKeyPressed(keyCode, modifier)
        elif (self.mode == "playGame"):   
            self.playGameKeyPressed(keyCode, modifier)
        elif (self.mode == "help"):       
            self.helpKeyPressed(keyCode, modifier)
        elif (self.mode == "levelSelection"):
            self.levelSelectionKeyPressed(keyCode, modifier)
        elif (self.mode == "levelCreation"):
            self.levelCreationKeyPressed(keyCode, modifier)

    def mousePressed(self, x, y):
        if (self.mode == "splashScreen"): 
            self.splashScreenMousePressed(x, y)
        elif (self.mode == "playGame"):   
            self.playGameMousePressed(x, y)
        elif (self.mode == "help"):       
            self.helpMousePressed(x, y)
        elif (self.mode == "levelSelection"):
            self.levelSelectionMousePressed(x,y)
        elif (self.mode == "levelCreation"):
            self.levelCreationMousePressed(keyCode, modifier)

    def mouseDrag(self, x, y):
        if self.mode == "playGame":
            self.playGameMouseDrag(x, y)

    def mouseRelease(self, x, y):
        if self.mode == "playGame":
            self.playGameMouseRelease(x, y)

    def timerFired(self, dt):
        if (self.mode == "splashScreen"): 
            self.splashScreenTimerFired(dt)
        elif (self.mode == "playGame"):   
            self.playGameTimerFired(dt)
        elif (self.mode == "help"):       
            self.helpTimerFired(dt)
        elif (self.mode == "levelSelection"):
            self.levelSelectionTimerFired(dt)
        elif (self.mode == "levelCreation"):
            self.levelCreationTimerFired(keyCode, modifier)


    def redrawAll(self, screen):
        if (self.mode == "splashScreen"): 
            self.splashScreenRedrawAll(screen)
        elif (self.mode == "playGame"):   
            self.playGameRedrawAll(screen)
        elif (self.mode == "help"):       
            self.helpRedrawAll(screen)
        elif (self.mode == "levelSelection"):
            self.levelSelectionRedrawAll(screen)
        elif (self.mode == "levelCreation"):
            self.levelCreationRedrawAll(keyCode, modifier)

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

    def playGameMouseDrag(self, x, y):
        pos = (x,y)

        if self.controlBar.tileRectList[0].collidepoint(pos) or self.dragFlag:
            print("here")
            tile = Tile()
            self.dragFlag = True
            tile.rect.center = (pos[0]-70/2, pos[1]-44/2)
            self.objectDragged = (tile, tile.rect.center)

    def playGameMouseRelease(self, x, y, screen):
        if self.dragFlag:
            self.dragFlag = False
            # draw the tile on the board
            row, col = utility.isoToMap(x, y, len(self.board), 35, 22, screen)
            if(row >= 0) and (row < len(self.board)) and (col >= 0) and (col < len(self.board)):
                # check legality of putting a tile there
                if(not self.board[row][col] in range(-1, 9)):
                    self.board[row][col] = self.objectDragged[0].type



    def playGameTimerFired(self, dt):
        if self.player.beginMoving:
            if(not self.player.illegalMove):
                self.playerGroup.update(self.board)
                if(self.player.win):
                    print("You win!")
            else:
                self.player.row, self.player.col = (0,0)
                print("You lose!")
        if self.resetState:
            self.board = copy.deepcopy(self.boardObject.board)
            self.player.__init__()
            self.resetState = False

    def playGameRedrawAll(self, screen):
        # Draw the board
        self.boardObject.draw(screen)


        # Draw the control
        self.controlBar.draw(screen, self.width, self.height)
        self.beginRect = screen.blit(self.begin.image, (self.begin.rect.x, self.begin.rect.y))
        self.resetRect = screen.blit(self.reset.image, (self.reset.rect.x, self.reset.rect.y))
        self.menuRect = screen.blit(self.menu.image, (self.menu.rect.x, self.menu.rect.y))

        if self.dragFlag and self.objectDragged != None:
            screen.blit(self.objectDragged[0].image, self.objectDragged[1])

    ########################
    # splashScreen mode
    ########################
    def splashScreenKeyPressed(self, keyCode, modifier):
        pass
    def splashScreenMousePressed(self, x, y):
        pos = (x, y)
        if(self.levelRect.collidepoint(pos)):
            self.mode = "levelSelection"
        elif(self.levelCreationRect.collidepoint(pos)):
            self.mode = "levelCreation"
        elif(self.helpRect.collidepoint(pos)):
            self.mode = "help"


    def splashScreenTimerFired(self, dt):
        pass
    def splashScreenRedrawAll(self, screen):
        # Draw the title and the level selection
        font1 = pygame.font.Font("freesansbold.ttf", 120)

        titleSurface = font1.render("Pendo", True, (255, 255, 255))
        titleRect = titleSurface.get_rect()
        titleRect.center = (self.width//2, self.height//2-70)
        screen.blit(titleSurface, titleRect)

        font2 = pygame.font.Font("freesansbold.ttf", 50)

        self.levelSurface = font2.render("Level Selection", True, (255, 255, 255), (205,140,149))
        self.levelRect = self.levelSurface.get_rect()
        self.levelRect.center = (self.width//2, self.height//2+50)
        screen.blit(self.levelSurface, self.levelRect)

        self.levelCreationSurface = font2.render("Level Creation", True, (255, 255, 255), (205,140,149))
        self.levelCreationRect = self.levelCreationSurface.get_rect()
        self.levelCreationRect.center = (self.width//2, self.height//2+150)
        screen.blit(self.levelCreationSurface, self.levelCreationRect)

        self.helpSurface = font2.render("Help", True, (255, 255, 255), (205,140,149))
        self.helpRect = self.helpSurface.get_rect()
        self.helpRect.center = (self.width//2, self.height//2+250)
        screen.blit(self.helpSurface, self.helpRect)        

    ########################
    # help mode
    ########################
    def helpKeyPressed(self, keyCode, modifier):
        pass
    def helpMousePressed(self, x, y):
        self.mode = "playGame"
    def helpTimerFired(self, dt):
        pass
    def helpRedrawAll(self, screen):
        font3 = pygame.font.Font("freesansbold.ttf", 20)

        textSurface0 = font3.render("Instruction:))))", True, (255, 255, 255))
        screen.blit(textSurface0, ((self.width/2-300, self.height/2-220)))

        textSurface1 = font3.render("~Use your mouse to drag a tile to any empty spot~", True, (255, 255, 255))
        screen.blit(textSurface1, (self.width/2-300, self.height/2-170))

        textSurface2 = font3.render("~Build up a path to the target blue spot~", True, (255, 255, 255))
        screen.blit(textSurface2, (self.width/2-300, self.height/2-120))

        textSurface3 = font3.render("~Click on the right arrow for the ball to roll~", True, (255, 255, 255))
        screen.blit(textSurface3, (self.width/2-300, self.height/2-70))

        textSurface4 = font3.render("~Click on the menu button to go back to Level Selection Page~", True, (255, 255, 255))
        screen.blit(textSurface4, (self.width/2-300, self.height/2-20)) 

        textSurface5 = font3.render("~Click on the restart button to restart the game~", True, (255, 255, 255))
        screen.blit(textSurface5, (self.width/2-300, self.height/2+30))  

        textSurface6 = font3.render("~Click anywhere to start~", True, (255, 255, 255))
        screen.blit(textSurface6, (self.width/2-300, self.height/2+80))      

        textSurface7 = font3.render("~E~N~J~O~Y~", True, (255, 255, 255))
        screen.blit(textSurface7, (self.width/2-60, self.height/2+130))  



    ########################
    # levelSelection mode
    ########################
    def levelSelectionKeyPressed(self, keyCode, modifier):
        pass
    def levelSelectionMousePressed(self, x, y):
        pos = (x, y)
        if(self.textRect1.collidepoint(pos)):
            self.mode = "level1"
        elif(self.textRect2.collidepoint(pos)):
            self.mode = "level2"
        elif(self.textRect3.collidepoint(pos)):
            self.mode = "level3"
    def levelSelectionTimerFired(self, dt):
        pass
    def levelSelectionRedrawAll(self, screen):
        font2 = pygame.font.Font("freesansbold.ttf", 50)

        levelSelectionSurface = font2.render("Level Selection", True, (255, 255, 255), (205,140,149))
        self.levelSelectionRect = levelSelectionSurface.get_rect()
        self.levelSelectionRect.center = (self.width//2, 40)
        screen.blit(levelSelectionSurface, self.levelSelectionRect)

        level1Text = font2.render("Level 1", True, (255, 255, 255), (205,140,149))
        self.textRect1 = level1Text.get_rect()
        self.textRect1.center = (self.width//2, 150)
        screen.blit(level1Text, self.textRect1)

        level2Text = font2.render("Level 2", True, (255, 255, 255), (205,140,149))
        self.textRect2 = level2Text.get_rect()
        self.textRect2.center = (self.width//2, screen.get_rect().centery)
        screen.blit(level2Text, self.textRect2)

        level3Text = font2.render("Level 3", True, (255, 255, 255), (205,140,149))
        self.textRect3 = level3Text.get_rect()
        self.textRect3.center = (self.width//2, self.height - 150)
        screen.blit(level3Text, self.textRect3)



    ########################
    # levelCreation mode
    ########################
    def levelCreationKeyPressed(self, keyCode, modifier):
        pass
    def levelCreationMousePressed(self, x, y):
        self.mode = "help"
    def levelCreationTimerFired(self, dt):
        pass
    def levelCreationRedrawAll(self, screen):
        pass


    

game = Game()
game.run()