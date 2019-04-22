import pygame
from Player import Player
from Tiles import *
import utility


class Board(object):
    def __init__(self, n, player):
        self.rows = self.cols = n
        self.board = Board.generateBoard(n)
        #self.controlBar = Board.generateControlBar(self.board)
        self.player = player

        self.tileWidth = 70
        self.tileHeight = 44
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
        return [[-1, 0, 0,0,0],
                [0, 0, 0,0,0],
                [8, 0, 0,0,0],
                [0, 8, 5,0,0],
                [5, 0, 0,0,0]]

    def draw(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                num = self.board[row][col]
                # the player position and normal grids
                if(num == -1) or (num == 0):
                    tile = Tile()
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
                elif(num in range(1,5)):
                    tile = DireTile(num)
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
                elif(num == 5):
                    tile = PortalTile()
                    tileImage = tile.image
                    tileRect = tile.rect
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
                elif(num == 8):
                    tile = TargetTile()
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
                else:
                    continue
        # for the player
        iso_x, iso_y = utility.mapToIso(self.player.row, self.player.col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
        playerGroup = pygame.sprite.GroupSingle(self.player)
        # centered_y-10 to makes the player looks like higher than the board
        self.player.rect.x, self.player.rect.y = iso_x, iso_y-10
        self.player.image.set_colorkey((255,255,255))
        screen.blit(self.player.image, (self.player.rect.x,self.player.rect.y))
        
        





