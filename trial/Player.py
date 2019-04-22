import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('images/circle.png').convert()
        self.rect = self.image.get_rect()

        self.beginMoving = False
        self.illegalMove = False
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

    def moveIllegal(self, board):
        rows = len(board)
        cols = len(board[0])
        if(self.row < 0) or (self.col < 0) or (self.row >= rows) or (self.col >= cols):
            print("yes")
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
                self.drow = -1
                self.dcol = 0
            ## right
            elif(num == 2):
                self.currDire = "right"
                self.drow = 0
                self.dcol = -1
            ## down
            elif(num == 3):
                self.currDire = "down"
                self.drow = 1
                self.dcol = 0
            ## left
            elif (num == 4):
                self.currDire = "left"
                self.drow = 0
                self.dcol = 1
            # check for portal tiles
            elif (num == 5):
                self.drow, self.dcol = self.teleport(self.row, self.col, board)
            self.row += self.drow
            self.col += self.dcol

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



            


    




