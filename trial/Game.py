# beyond
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
        self.boardObject = Board(n, self.level)

        self.board = copy.deepcopy(self.boardObject.board)
        
        self.scene = None

        # Control
        self.begin = Begin(self.width, self.height)
        self.beginMoving = False

        self.reset = Reset(self.width, self.height)
        self.resetState = False

        self.menu = Menu(self.width, self.height)
        self.exit = Exit(self.width, self.height)

        self.save = Save(self.width, self.height)

        self.controlBar = controlBar(self.width, self.height)

        self.dragFlag = [False]*10
        self.objectDragged = None

        self.fonts = dict()
        self.fonts["splashScreenTitle"] = pygame.font.SysFont("copperplatettc", 150)
        self.fonts["splashScreenBoxes"] = pygame.font.SysFont("copperplatettc", 50)
        self.fonts["instruction"] = pygame.font.SysFont("avenirnextttc", 27)

        #get the texts
        self.beginTexting = False
        self.idBeginTexting = False
        self.idTextBox = TextBox(self.fonts["instruction"], True)
        self.boardBeginTexting = False
        self.boardTextBox = TextBox(self.fonts["instruction"], False)
        self.transmittedInfo = ""




    def keyPressed(self, keyCode, uni, modifier):
        if (self.mode == "splashScreen"): 
            self.splashScreenKeyPressed(keyCode, uni, modifier)
        elif (self.mode == "playGame"):   
            self.playGameKeyPressed(keyCode, uni, modifier)
        elif (self.mode == "help"):       
            self.helpKeyPressed(keyCode, uni, modifier)
        elif (self.mode == "levelSelection"):
            self.levelSelectionKeyPressed(keyCode, uni, modifier)
        elif (self.mode == "levelCreation"):
            self.levelCreationKeyPressed(keyCode, uni, modifier)

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
        elif self.mode == "levelCreation":
            self.levelCreationMouseDrag(x, y)


    def mouseReleased(self, x, y, screen):
        if self.mode == "playGame":
            self.playGameMouseReleased(x, y, screen)
        elif self.mode == "levelCreation":
            self.levelCreationMouseReleased(x, y, screen)

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
    def playGameKeyPressed(self, keyCode, uni, modifier):
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
                    if(isinstance(self.objectDragged[0], Player)) and self.board[row][col] != -1:
                        self.player.row = row
                        self.player.col = col
                    # check legality of putting a tile there
                    elif(self.board[row][col] == 9) or self.board[row][col] == 10:
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
        self.player.draw(screen, self.board, self.boardObject.cols, self.boardObject.halfTileWidth, self.boardObject.halfTileHeight)

        # Draw the control
        self.controlBar.draw(screen, self.width, self.height)
        pygame.draw.rect(screen, (255, 255, 255), (10+80*7, self.height-90, 300, 200))
        self.beginRect = screen.blit(self.begin.image, (self.begin.rect.x, self.begin.rect.y))
        self.resetRect = screen.blit(self.reset.image, (self.reset.rect.x, self.reset.rect.y))
        self.menuRect = screen.blit(self.menu.image, (self.menu.rect.x, self.menu.rect.y))

        for dragFlag in self.dragFlag:
            if dragFlag:
                screen.blit(self.objectDragged[0].image, self.objectDragged[1])

        #Scene
        if(self.scene != None):
            self.scene.draw(screen)
            if(self.scene.state == True):
                font = self.fonts["instruction"]
                textSurface = font.render("Select a new level by clicking on the menu button", True, (135, 71, 93))
                textRect = textSurface.get_rect()
                textRect.centerx = screen.get_rect().centerx
                textRect.centery = screen.get_rect().centery+90
                screen.blit(textSurface, textRect)
            else:
                font = self.fonts["instruction"]

                textSurface = font.render("Press any key to try again", True, (139, 71, 93))
                textRect = textSurface.get_rect()
                textRect.centerx = screen.get_rect().centerx
                textRect.centery = screen.get_rect().centery+60
                screen.blit(textSurface, textRect)


    ########################
    # splashScreen mode
    ########################
    def splashScreenKeyPressed(self, keyCode, uni, modifier):
        pass
    def splashScreenMousePressed(self, x, y):
        pos = (x, y)
        if(self.levelRect.collidepoint(pos)):
            self.mode = "levelSelection"
        elif(self.levelCreationRect.collidepoint(pos)):
            self.init(4)
            self.mode = "levelCreation"
            self.player.row, self.player.col = -10, -10
        elif(self.helpRect.collidepoint(pos)):
            self.mode = "help"


    def splashScreenTimerFired(self, dt):
        pass

    def splashScreenRedrawAll(self, screen):
        # Draw the title and the level selection
        font1 = self.fonts["splashScreenTitle"]

        titleSurface = font1.render("Pendo", True, (255, 255, 255))
        titleRect = titleSurface.get_rect()
        titleRect.center = (self.width//2, self.height//2-100)
        screen.blit(titleSurface, titleRect)

        font2 = self.fonts["splashScreenBoxes"]

        self.levelSurface = font2.render("Level Selection", True, (255, 255, 255), (205,140,149))
        self.levelRect = self.levelSurface.get_rect()
        self.levelRect.center = (self.width//2, self.height//2+30)
        screen.blit(self.levelSurface, self.levelRect)

        self.levelCreationSurface = font2.render("Level Creation", True, (255, 255, 255), (205,140,149))
        self.levelCreationRect = self.levelCreationSurface.get_rect()
        self.levelCreationRect.center = (self.width//2, self.height//2+130)
        screen.blit(self.levelCreationSurface, self.levelCreationRect)

        self.helpSurface = font2.render("Instruction", True, (255, 255, 255), (205,140,149))
        self.helpRect = self.helpSurface.get_rect()
        self.helpRect.center = (self.width//2, self.height//2+230)
        screen.blit(self.helpSurface, self.helpRect)        

    ########################
    # help mode
    ########################
    def helpKeyPressed(self, keyCode, uni, modifier):
        self.mode = "levelSelection"
    def helpMousePressed(self, x, y):
        self.mode = "splashScreen"
    def helpTimerFired(self, dt):
        pass
    def helpRedrawAll(self, screen):
        font3 = self.fonts["instruction"]

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
    def levelSelectionKeyPressed(self, keyCode, uni, modifier):
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
        elif(self.exitRect.collidepoint(pos)):
            self.mode = "splashScreen"
    def levelSelectionTimerFired(self, dt):
        pass
    def levelSelectionRedrawAll(self, screen):
        font2 = self.fonts["splashScreenBoxes"]

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

        self.exitRect = screen.blit(self.exit.image, (self.exit.rect.x, self.exit.rect.y))



    ########################
    # levelCreation mode
    ########################
    def levelCreationKeyPressed(self, keyCode, uni, modifier):
        if self.scene != None and self.scene.state == False:
            self.player.__init__()
            self.player.row, self.player.col = -10, -10
            self.scene.state = None
            self.scene = None # clear the winning/losing scene

        if self.idBeginTexting:
            if keyCode == pygame.K_RETURN:
                self.idBeginTexting = False
            self.idTextBox.update(keyCode, uni, modifier)

        if self.boardBeginTexting:
            if keyCode == pygame.K_RETURN:
                self.boardBeginTexting = False
                self.transmittedInfo += self.boardTextBox.text
                self.storeInfo(self.transmittedInfo)
                #print("self.transmittedInfo: ", self.transmittedInfo)
                self.idTextBox = None
                self.boardTextBox = None
            if self.boardTextBox != None:
                self.boardTextBox.update(keyCode, uni, modifier)

    def storeInfo(self, info):
        #print(self.board, "self.transmittedInfo: ", info)
        data = dict()
        data["board"] = self.board
        indexB = info.index("Board's")
        indexI = info.index("ID")
        data["User"] = info[9:indexB-1]
        data["boardName"] = info[indexB+14:]
        #print(data)

    def levelCreationMousePressed(self, x, y):
        pos = (x,y)
        self.playGameMousePressed(x, y)
        if(self.menuRect.collidepoint(pos)):
            self.mode = "splashScreen"
        elif(self.saveRect.collidepoint(pos)):
            self.beginTexting = True
            self.idBeginTexting = True
            self.idTextBox = TextBox(self.fonts["instruction"], True)
            self.boardTextBox = TextBox(self.fonts["instruction"], False)
            self.transmittedInfo = ""
        elif self.boardTextBox != None and (self.boardTextBox.textRect.collidepoint(pos)):
            self.transmittedInfo += self.idTextBox.text + " "
            self.idBeginTexting = False
            self.boardBeginTexting = True



    def levelCreationMouseDrag(self, x, y):
        pos = (x, y)
        self.playGameMouseDrag(x, y)

        if self.controlBar.tileRectList != None:
            if self.controlBar.tileRectList[7].collidepoint(pos) or self.dragFlag[7]:
                tile = Cube()
                self.dragFlag[7] = True
                pos = (pos[0] - 70 / 2, pos[1] - 44 / 2)
                self.objectDragged = (tile, pos)

            elif self.controlBar.tileRectList[8].collidepoint(pos) or self.dragFlag[8]:
                tile = TargetTile()
                self.dragFlag[8] = True
                pos = (pos[0] - 70/2, pos[1]-44/2)
                self.objectDragged = (tile, pos)

            elif self.controlBar.tileRectList[9].collidepoint(pos) or self.dragFlag[9]:
                player = Player()
                self.dragFlag[9] = True
                pos = (pos[0] - 70/2, pos[1] - 44/2)
                self.objectDragged = (player, pos)

    def levelCreationMouseReleased(self, x, y, screen):
        self.playGameMouseReleased(x, y, screen)

    def levelCreationTimerFired(self, dt):
        if self.player.beginMoving:
            if(not self.player.illegalMove):
                self.playerGroup.update(self.board)
                if(self.player.win):
                    self.scene = CustomScene(True)
            else:
                self.scene = CustomScene(False)
                self.player.row, self.player.col = -10,-10
        if self.resetState:
            self.board = copy.deepcopy(self.boardObject.board)
            self.player.__init__()
            self.player.row, self.player.col = -10, -10
            self.scene = None # clear the winning/losing scene
            self.resetState = False

    def levelCreationRedrawAll(self, screen):
        font2 = self.fonts["splashScreenBoxes"]

        levelCreationSurf = font2.render("Level Creation", True, (255, 255, 255), (205,140,149))
        self.levelCreationRect = levelCreationSurf.get_rect()
        self.levelCreationRect.center = (self.width//2, 40)
        screen.blit(levelCreationSurf, self.levelCreationRect)

        # draw the board
        self.boardObject.draw(screen, self.board)
        # control
        self.controlBar.draw(screen, self.width, self.height)
        self.beginRect = screen.blit(self.begin.image, (self.begin.rect.x, self.begin.rect.y))
        self.resetRect = screen.blit(self.reset.image, (self.reset.rect.x, self.reset.rect.y))
        self.menuRect = screen.blit(self.menu.image, (self.menu.rect.x, self.menu.rect.y))
        self.saveRect = screen.blit(self.save.image, (self.save.rect.x, self.save.rect.y))

        for dragFlag in self.dragFlag:
            if dragFlag:
                screen.blit(self.objectDragged[0].image, self.objectDragged[1])

        # player
        self.player.draw(screen, self.board, self.boardObject.cols, self.boardObject.halfTileWidth, self.boardObject.halfTileHeight)

        #Scene
        if(self.scene != None):
            self.scene.draw(screen)
            if(self.scene.state == True):
                font = self.fonts["instruction"]

                textSurface = font.render("Remember to save your work or go back to the menu:)", True, (135, 71, 93))
                textRect = textSurface.get_rect()
                textRect.centerx = screen.get_rect().centerx
                textRect.centery = screen.get_rect().centery+80
                screen.blit(textSurface, textRect)
            else:
                font = self.fonts["instruction"]

                textSurface = font.render("Press any key to try again", True, (139, 71, 93))
                textRect = textSurface.get_rect()
                textRect.centerx = screen.get_rect().centerx
                textRect.centery = screen.get_rect().centery+60
                screen.blit(textSurface, textRect)

        if self.beginTexting and self.boardTextBox != None:
            font = self.fonts["instruction"]
            textSurface = font.render("~Please enter your User ID and the name of the board:)~", True, (139, 71, 93))
            textRect = textSurface.get_rect()
            textRect.centerx = screen.get_rect().centerx
            textRect.centery = screen.get_rect().centery-105
            screen.blit(textSurface, textRect)

            textSurface = font.render("~Click on the corresponding text boxes and type~", True, (139, 71, 93))
            textRect = textSurface.get_rect()
            textRect.centerx = screen.get_rect().centerx
            textRect.centery = screen.get_rect().centery - 70
            screen.blit(textSurface, textRect)

            textSurface = font.render("~Hit return to save the information when you are done~", True, (139, 71, 93))
            textRect = textSurface.get_rect()
            textRect.centerx = screen.get_rect().centerx
            textRect.centery = screen.get_rect().centery-35
            screen.blit(textSurface, textRect)


            self.idTextBox.textRect.x = screen.get_rect().centerx-100
            self.idTextBox.textRect.y = screen.get_rect().centery
            self.idTextBox.render(screen, self.idTextBox.textRect.x, self.idTextBox.textRect.y)
            if self.idBeginTexting:
                self.idTextBox.render(screen, self.idTextBox.textRect.x, self.idTextBox.textRect.y)

            self.boardTextBox.textRect.x = screen.get_rect().centerx-100
            self.boardTextBox.textRect.y = self.idTextBox.textRect.y + 35
            self.boardTextBox.render(screen, self.boardTextBox.textRect.x, self.boardTextBox.textRect.y)
            if self.boardBeginTexting:
                self.boardTextBox.render(screen,self.boardTextBox.textRect.x, self.boardTextBox.textRect.y)





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
            

        # Lose
        else:
            image = pygame.image.load('images/game-over.png').convert()
            rect = image.get_rect()
            image.set_colorkey((0,0,0))
            rect.centerx = screen.get_rect().centerx
            rect.centery = screen.get_rect().centery-100


        screen.blit(image, rect)
    

game = Game()
game.run()