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
        board = [
            [0, 0, 1, 2, 3],
            [4, -1, 0, 0, 0],
            [0, 0, 5, 6, 0],
            [0, 0, 5, 7, 0],
            [0, 0, 0, 0, 0],
            ]    
        return board
    @staticmethod
    def generateControlBar(board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                if num != -1 or num != 0:
                    pass





    def draw(self, screen):
        for level in range(2):
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    num = self.board[row][col]
                    # the player position and normal grids
                    if(num == -1) or (num == 0):
                        tile = Tile()
                        tileImage = tile.image
                        iso_x, iso_y = utility.mapToIso(row, col, self.halfTileWidth, self.halfTileHeight)
                        centered_x = screen.get_rect().centerx + iso_x
                        centered_y = screen.get_rect().centery//2 + iso_y-level*10
                        screen.blit(tileImage, (centered_x, centered_y))
                    elif(num in range(1,4)):
                        tile = DireTile(num)
                        tileImage = tile.image
                        iso_x, iso_y = utility.mapToIso(row, col, self.halfTileWidth, self.halfTileHeight)
                        centered_x = screen.get_rect().centerx + iso_x
                        centered_y = screen.get_rect().centery//2 + iso_y-level*10
                        screen.blit(tileImage, (centered_x, centered_y))
                    elif(num == 5):
                        tile = PortalTile()
                        tileImage = tile.image
                        iso_x, iso_y = utility.mapToIso(row, col, self.halfTileWidth, self.halfTileHeight)
                        centered_x = screen.get_rect().centerx + iso_x
                        centered_y = screen.get_rect().centery//2 + iso_y-level*10
                        screen.blit(tileImage, (centered_x, centered_y))
                    else:
                        continue

        iso_x, iso_y = utility.mapToIso(3, 1, self.halfTileWidth, self.halfTileHeight)
        centered_x = screen.get_rect().centerx + iso_x
        centered_y = screen.get_rect().centery//2 + iso_y
        playerGroup = pygame.sprite.GroupSingle(self.player)
        self.player.rect.centerx, self.player.rect.centery = centered_x, centered_y-20
        playerGroup.draw(screen)
        
        





