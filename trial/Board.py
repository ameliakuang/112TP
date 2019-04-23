import pygame
from Player import Player
from Tiles import *
import utility
import random


class Board(object):
    def __init__(self, n, player, level):
        self.rows = self.cols = n
        self.board = self.generateBoard(5, 1)
        self.player = player

        self.tileWidth = 70
        self.tileHeight = 44
        self.halfTileWidth = self.tileWidth//2
        self.halfTileHeight = self.tileHeight//2
        




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
    9: empty spot
    '''
    def generateBoard(self, n, level):
        if level == 0:
            return [[-1, 0, 0,0,2],
                    [0, 0, 0,0,0],
                    [0, 0, 0,0,0],
                    [6, 7, 0,0,0],
                    [9, 0, 0,0,1]]
        elif level == 1:
            board = [[0] * n for row in range(n)]
            board[0][0] = -1
            board[n-1][n-1] = 8
            # generate two possibilities
            temp = random.randint(1, 3)
            # two spots for portal tiles
            if(temp == 1):
                row_on_0th_col = random.randint(1, n-2)
                row_on_last_col = random.randint(1, n-2)
                board[row_on_0th_col][0] = 9
                board[row_on_last_col][n-1] = 9
            elif(temp == 2):   
                board[n-1][0] = 9
            else:
                row_on_0th_col = random.randint(1, n-2)
                board[row_on_0th_col][0] = 9
                board[row_on_0th_col][n-1] = 9
            return board

    def draw(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                num = self.board[row][col]
                # the player position
                if(num == -1):
                    tile = DireTile(3)
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
                # normal tile
                if (num == 0):
                    tile = Tile()
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
                # direction tiles
                elif(num in range(1,5)):
                    tile = DireTile(num)
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
                # portal tiles
                elif(num == 5):
                    tile = PortalTile()
                    tileImage = tile.image
                    tileRect = tile.rect
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
                elif(num == 6):
                    tile = JumpTile()
                    tileImage = tile.image
                    tileRect = tile.rect
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))                    
                # cube
                elif(num == 7):
                    tile = Cube()
                    tileImage = tile.image
                    tileRect = tile.rect
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    iso_y -= self.halfTileHeight+5
                    screen.blit(tileImage, (iso_x, iso_y))
                # target tiles
                elif(num == 8):
                    tile = TargetTile()
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
                # empty spots
                else:
                    continue
        # for the player
        iso_x, iso_y = utility.mapToIso(self.player.row, self.player.col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
        playerGroup = pygame.sprite.GroupSingle(self.player)
        # centered_y-10 to makes the player looks like higher than the board
        self.player.rect.x, self.player.rect.y = iso_x, iso_y-15
        self.player.image.set_colorkey((255,255,255))
        screen.blit(self.player.image, (self.player.rect.x,self.player.rect.y))
        
        


