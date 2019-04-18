import pygame
from Player import Player
from Tiles import *
import utility


class Board(object):
    def __init__(self, n, player):
        self.rows = self.cols = n
        self.board = Board.generateBoard(n)
        self.controlBar = Board.generateControlBar(self.board)
        self.player = player

        self.tileWidth = 72
        self.tileHeight = 72
        self.halfTileWidth = self.tileWidth//2
        self.halfTileHeight = self.tileHeight//2
        
        # Group for the generated tiles
        self.options = pygame.sprite.Group()



    # first randomly generate tiles, 
    # and then use backtracking to generate the board
    '''
    -1: is for player, and a normal tile should be placed in the board
    0: normal tiles
    1,2,3,4: direction tiles
    5: portal tiles
    6: jump tiles
    7: cube 
    8：target tiles
    '''
    @staticmethod
    def generateBoard(n):
        board = [ [ None ] * n for row in range(n)]
        board[0][0] = -1
        #solution = solve(board)
        #if solution != None:
            #pass
        return [[0,0,-1,0,0],
                [2,3,0,0,0],
                [2,3,0,0,0],
                [4,5,1,0,0],
                [0,0,0,0,0]]



    @staticmethod
    def generateControlBar(board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                if num != -1 or num != 0:
                    pass





    def draw(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                num = self.board[row][col]
                # the player position and normal grids
                if(num == -1) or (num == 0):
                    tile = Tile()
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.halfTileWidth, self.halfTileHeight)
                    centered_x = screen.get_rect().centerx + iso_x
                    centered_y = screen.get_rect().centery//2 + iso_y
                    screen.blit(tileImage, (centered_x, centered_y))
                elif(num in range(1,4)):
                    tile = DireTile(num)
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.halfTileWidth, self.halfTileHeight)
                    centered_x = screen.get_rect().centerx + iso_x
                    centered_y = screen.get_rect().centery//2 + iso_y
                    screen.blit(tileImage, (centered_x, centered_y))
                elif(num == 5):
                    tile = PortalTile()
                    tileImage = tile.image
                    tileRect = tile.rect
                    iso_x, iso_y = utility.mapToIso(row, col, self.halfTileWidth, self.halfTileHeight)
                    centered_x = screen.get_rect().centerx + iso_x
                    centered_y = screen.get_rect().centery//2 + iso_y
                    
                    #pygame.draw.rect(screen, (0,0,0), (centered_x, centered_y, tileRect[2], tileRect[3]))
                    screen.blit(tileImage, (centered_x, centered_y))
                else:
                    continue

        iso_x, iso_y = utility.mapToIso(2, 4, self.halfTileWidth, self.halfTileHeight)
        centered_x = screen.get_rect().centerx + iso_x
        centered_y = screen.get_rect().centery//2 + iso_y
        playerGroup = pygame.sprite.GroupSingle(self.player)
        # centered_y-10 to makes the player looks like higher than the board
        self.player.rect.x, self.player.rect.y = centered_x, centered_y-10
        self.player.image.set_colorkey((255,255,255))
        #pygame.draw.rect(screen, (0,0,0), (centered_x, centered_y, 70, 44))
        screen.blit(self.player.image, (self.player.rect.x,self.player.rect.y))
        
        





