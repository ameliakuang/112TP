import pygame
from pygamegame import *
from Board import *
from Player import *
from Tiles import *
from Control import *
import utility
import copy
import random

class Game(PygameGame):
    def init(self, level = 0):
        self.mode = "splashScreen"
        # Background color
        self.bgColor = (247, 202, 201)

        # Player
        self.player = Player()
        self.playerGroup = pygame.sprite.GroupSingle(self.player)
        # Board
        ## self.boardObject is an object of the class Board
        ## self.board is the 2d list representation of the board object
        self.level = level
        n = 0
        if self.level == 3:
            n = random.choice([6,8,10])
        else:
            n = 5
        self.boardObject = Board(n, self.player, self.level)
        #print("board level", self.level)
        self.board = copy.deepcopy(self.boardObject.board)
        #print(self.board)
        
        self.scene = None

        # Control
        self.begin = Begin(self.width, self.height)
        self.beginMoving = False

        self.reset = Reset(self.width, self.height)
        self.resetState = False

        self.menu = Menu(self.width, self.height)

        self.controlBar = controlBar(self.width, self.height)

        self.dragFlag = [False]*7
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
            self.levelCreationMousePressed(x,y)

    def mouseDrag(self, x, y):
        if self.mode == "playGame":
            self.playGameMouseDrag(x, y)

    def mouseReleased(self, x, y, screen):
        if self.mode == "playGame":
            self.playGameMouseReleased(x, y, screen)

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
            self.levelCreationTimerFired(dt)


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
            self.levelCreationRedrawAll(screen)

    ########################
    # playGame mode
    ########################
    def playGameKeyPressed(self, keyCode, modifier):
        if self.scene != None and self.scene.state == False:
            self.player.__init__()
            self.scene.state = None
            self.scene = None # clear the winning/losing scene
            


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

        if self.controlBar.tileRectList != None:
            if self.controlBar.tileRectList[0].collidepoint(pos) or self.dragFlag[0]:
                tile = Tile()
                self.dragFlag[0] = True
                pos = (pos[0] - 70 / 2, pos[1] - 44 / 2)
                self.objectDragged = (tile, pos)

            elif self.controlBar.tileRectList[1].collidepoint(pos) or self.dragFlag[1]:
                tile = DireTile(1)
                self.dragFlag[1] = True
                pos = (pos[0] - 70 / 2, pos[1] - 44 / 2)
                self.objectDragged = (tile, pos)

            elif self.controlBar.tileRectList[2].collidepoint(pos) or self.dragFlag[2]:
                tile = DireTile(2)
                self.dragFlag[2] = True
                pos = (pos[0] - 70 / 2, pos[1] - 44 / 2)
                self.objectDragged = (tile, pos)

            elif self.controlBar.tileRectList[3].collidepoint(pos) or self.dragFlag[3]:
                tile = DireTile(3)
                self.dragFlag[3] = True
                pos = (pos[0] - 70 / 2, pos[1] - 44 / 2)
                self.objectDragged = (tile, pos)

            elif self.controlBar.tileRectList[4].collidepoint(pos) or self.dragFlag[4]:
                tile = DireTile(4)
                self.dragFlag[4] = True
                pos = (pos[0] - 70 / 2, pos[1] - 44 / 2)
                self.objectDragged = (tile, pos)

            elif self.controlBar.tileRectList[5].collidepoint(pos) or self.dragFlag[5]:
                tile = PortalTile()
                self.dragFlag[5] = True
                pos = (pos[0] - 70 / 2, pos[1] - 44 / 2)
                self.objectDragged = (tile, pos)

            elif self.controlBar.tileRectList[6].collidepoint(pos) or self.dragFlag[6]:
                tile = JumpTile()
                self.dragFlag[6] = True
                pos = (pos[0] - 70 / 2, pos[1] - 44 / 2)
                self.objectDragged = (tile, pos)


    def playGameMouseReleased(self, x, y, screen):
        index = 0
        while(index < len(self.dragFlag)):
            dragFlag = self.dragFlag[index]
            if dragFlag:
                self.dragFlag[index] = False
                # draw the tile on the board
                row, col = utility.isoToMap(x, y, len(self.board), 35, 22, screen)
                if(row >= 0) and (row < len(self.board)) and (col >= 0) and (col < len(self.board)):
                    # check legality of putting a tile there
                    if(self.board[row][col] == 9):
                        self.board[row][col] = self.objectDragged[0].type
                    else:
                        self.objectDragged = None
            index += 1

    def playGameTimerFired(self, dt):
        if self.player.beginMoving:
            if(not self.player.illegalMove):
                self.playerGroup.update(self.board)
                if(self.player.win):
                    self.scene = CustomScene(True)
            else:
                self.player.row, self.player.col = (0,0)
                self.scene = CustomScene(False)

        if self.resetState:
            self.board = copy.deepcopy(self.boardObject.board)
            self.player.__init__()
            self.scene = None # clear the winning/losing scene
            self.resetState = False


    def playGameRedrawAll(self, screen):
        # Draw the board
        self.boardObject.draw(screen, self.board)

        # Draw the control
        self.controlBar.draw(screen, self.width, self.height)
        self.beginRect = screen.blit(self.begin.image, (self.begin.rect.x, self.begin.rect.y))
        self.resetRect = screen.blit(self.reset.image, (self.reset.rect.x, self.reset.rect.y))
        self.menuRect = screen.blit(self.menu.image, (self.menu.rect.x, self.menu.rect.y))

        for dragFlag in self.dragFlag:
            if dragFlag:
                screen.blit(self.objectDragged[0].image, self.objectDragged[1])

        #Scene
        if(self.scene != None):
            self.scene.draw(screen)


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
        self.mode = "levelSelection"
    def helpMousePressed(self, x, y):
        self.mode = "splashScreen"
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

        textSurface6 = font3.render("~Press any key to select a level~", True, (255, 255, 255))
        screen.blit(textSurface6, (self.width/2-300, self.height/2+80))  

        textSurface7 = font3.render("~Click anywhere to go back to the splash screen~", True, (255, 255, 255))
        screen.blit(textSurface7, (self.width/2-300, self.height/2+130))    

        textSurface8 = font3.render("~E~N~J~O~Y~", True, (255, 255, 255))
        screen.blit(textSurface8, (self.width/2-60, self.height/2+180))  



    ########################
    # levelSelection mode
    ########################
    def levelSelectionKeyPressed(self, keyCode, modifier):
        pass
    def levelSelectionMousePressed(self, x, y):
        pos = (x, y)
        if(self.textRect1.collidepoint(pos)):
            self.init(1)
            self.mode = "playGame"
            self.level = 1
        elif(self.textRect2.collidepoint(pos)):
            self.init(2)
            self.level = 2
            self.mode = "playGame"
        elif(self.textRect3.collidepoint(pos)):
            self.init(3)
            self.level = 3
            self.mode = "playGame"
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
        self.mode = "splashScreen"
    def levelCreationTimerFired(self, dt):
        pass
    def levelCreationRedrawAll(self, screen):
        font2 = pygame.font.Font("freesansbold.ttf", 50)

        levelCreationSurf = font2.render("Level Creation", True, (255, 255, 255), (205,140,149))
        self.levelCreationRect = levelCreationSurf.get_rect()
        self.levelCreationRect.center = (self.width//2, 40)
        screen.blit(levelCreationSurf, self.levelCreationRect)
# Citation:https://stackoverflow.com/questions/14700889/pygame-level-menu-states
# I changed the specific image loaded and add the interaction with the player
class CustomScene(object):
    def __init__(self, state):
        self.state = state

    def draw(self, screen):
        # Win
        if(self.state == True):
            image = pygame.image.load('images/You Win.png').convert()
            image.set_colorkey((0,0,0))
            rect = image.get_rect()
            rect.centerx = screen.get_rect().centerx
            rect.centery = screen.get_rect().centery-50
            font = pygame.font.Font("freesansbold.ttf", 20)

            textSurface = font.render("Select a new level by clicking the menu button", True, (255, 255, 0))
            textRect = textSurface.get_rect()
            textRect.centerx = screen.get_rect().centerx
            textRect.centery = screen.get_rect().centery+80
            screen.blit(textSurface, textRect)
        # Lose
        else:
            image = pygame.image.load('images/game-over.png').convert()
            rect = image.get_rect()
            image.set_colorkey((0,0,0))
            rect.centerx = screen.get_rect().centerx
            rect.centery = screen.get_rect().centery-100

            font = pygame.font.Font("freesansbold.ttf", 20)

            textSurface = font.render("Press any key to try again", True, (255, 255, 0))
            textRect = textSurface.get_rect()
            textRect.centerx = screen.get_rect().centerx
            textRect.centery = screen.get_rect().centery+50
            screen.blit(textSurface, textRect)
        screen.blit(image, rect)
    

game = Game()
game.run()