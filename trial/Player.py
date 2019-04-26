import pygame
import utility

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('images/circle.png').convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.beginMoving = False
        self.illegalMove = False
        self.win = False
        # Player's current position
        self.row = 0
        self.col = 0
        self.drow = 0
        self.dcol = 0
        self.currDire = "down"

        self.currPortal = (None, None)
    '''
    -1: is for player, and a normal tile should be placed in the board
    0: normal tiles
    1,2,3,4: direction tiles
    5: portal tiles
    6: jump tiles
    7: cube 
    8：target tiles
    '''
    # either the player has moved out of the board
    # or the player reaches somewhere empty
    # or the player is on the cube but the previous tile is not a jump tile
    def moveIllegal(self, board):
        rows = len(board)
        cols = len(board[0])
        if(self.row < 0) or (self.col < 0) or (self.row >= rows) or (self.col >= cols):
            return True
        if not ( board[self.row][self.col] in range(-1, 9)):
            return True
        if board[self.row][self.col] == 7 and not board[self.row-self.drow][self.col-self.dcol] == 6:
            return True 
        return False

    def update(self, board):
        self.illegalMove = self.moveIllegal(board)
        if(not self.illegalMove):
            num = board[self.row][self.col]
            if(num == -1):
                self.drow = 1
                self.dcol = 0
            # check for direction tiles
            ## up
            elif(num == 1):
                self.currDire = "up"
                self.drow, self.dcol = -1,0
            ## right
            elif(num == 2):
                self.currDire = "right"
                self.drow, self.dcol = 0, -1
            ## down
            elif(num == 3):
                self.currDire = "down"
                self.drow, self.dcol = 1, 0
            ## left
            elif (num == 4):
                self.currDire = "left"
                self.drow, self.dcol = 0, 1
            # check for portal tiles
            elif (num == 5):
                self.drow, self.dcol = self.teleport(self.row, self.col, board)
            elif (num == 6):
                if self.currDire == "up":
                    self.drow = -1
                    self.dcol = 0
                elif self.currDire == "right":
                    self.drow, self.dcol = 0, -1
                elif self.currDire == "down":
                    self.drow, self.dcol = 1, 0
                elif self.currDire == "left":
                    self.drow, self.dcol = 0,1
            elif (num == 7):
                if self.currDire == "left":
                    self.drow = 0
                    self.dcol = 1
                elif self.currDire == "right":
                    self.drow, self.dcol = 0, -1
                elif self.currDire == "up":
                    self.drow, self.dcol = -1, 0
                elif self.currDire == "down":
                    self.drow, self.dcol = 1, 0
            elif(num == 8):
                self.win = True
                self.drow, self.dcol = 0,0

            self.row += self.drow
            self.col += self.dcol
            self.board = board


    def teleport(self, row, col, board):
        rows = cols = len(board)
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == 5) and (r != row or c != col) and (self.currPortal != (r, c)):
                    self.currPortal = (row,col)
                    return (r-row, c-col)
        if(self.currDire == "up"):
            return (-1, 0)
        elif(self.currDire == "right"):
            return (0, -1)
        elif(self.currDire == "down"):
            return (1, 0)
        elif(self.currDire == "left"):
            return (0, 1)

    def draw(self, screen, board, cols, halfWidth, halfHeight):
        if self.row < cols and 0 <= self.row and self.col < cols and 0 <= self.col and board[self.row][self.col] == 7:
            iso_x, iso_y = utility.mapToIso(self.row, self.col, cols, halfWidth, halfHeight, screen)
            playerGroup = pygame.sprite.GroupSingle(self)
            # iso_y-15 to makes the player looks like higher than the board
            self.rect.x, self.rect.y = iso_x, iso_y-50
            #self.image.set_colorkey((255,255,255))
            screen.blit(self.image, (self.rect.x,self.rect.y))
        else:
            iso_x, iso_y = utility.mapToIso(self.row, self.col, cols, halfWidth, halfHeight, screen)
            playerGroup = pygame.sprite.GroupSingle(self)
            # iso_y-15 to makes the player looks like higher than the board
            self.rect.x, self.rect.y = iso_x, iso_y-15
            #self.image.set_colorkey((255,255,255))
            screen.blit(self.image, (self.rect.x,self.rect.y))



            


    




