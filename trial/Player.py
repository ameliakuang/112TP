import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/circle.png').convert()
        self.rect = self.image.get_rect()
        self.beginMoving = False
        self.row = 0
        self.col = 0
        self.drow = 0
        self.dcol = 0
    '''
    -1: is for player, and a normal tile should be placed in the board
    0: normal tiles
    1,2,3,4: direction tiles
    5: portal tiles
    6: jump tiles
    7: cube 
    8：target tiles
    '''

    def moveLegal(self, board):
        rows = len(board)
        cols = len(board[0])


    def update(self, board):
        print("here")
        illegal = False

        row, col = self.row, self.col
        num = board[row][col]
        if(num == -1):
            self.drow = 1
        # check for direction tiles
        elif(num == 1):
            self.drow = 1
        elif(num == 2):
            self.drow = -1
        elif(num == 3):
            pass

        self.row += self.drow
        self.col += self.dcol


    




