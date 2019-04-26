import pygame
from Tiles import *
import utility
import random


class Board(object):
    def __init__(self, n, level):
        self.rows = self.cols = n
        self.board = self.generateBoard(n, level)
        self.level = level

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
    10: level creation tile
    '''
    def generateBoard(self, n, level):
        board = [[0] * n for row in range(n)]
        board[0][0] = -1
        if level == 0:
            return [[-1, 0, 0,0,0],
                    [6, 0, 0,0,0],
                    [6, 6, 7,0,0],
                    [7, 6, 7,0,0],
                    [4, 0, 6,7,0]]
        elif level == 1:
            board[n-1][n-1] = 8
            #  two possibilities
            temp = random.randint(1, 3)
            # two spots for portal tiles
            if(temp == 1):
                row_on_0th_col = random.randint(1, n-2)
                row_on_last_col = random.randint(1, n-2)
                board[row_on_0th_col][0] = 9
                board[row_on_last_col][n-1] = 9
            # one spot for direction tile on the corner
            elif(temp == 2):   
                board[n-1][0] = 9
            # two spots for two direction tiles
            else:
                row_on_0th_col = random.randint(1, n-2)
                board[row_on_0th_col][0] = 9
                board[row_on_0th_col][n-1] = 9
            return board
        elif level == 2:
            # ensure that a pair of direction tiles can be put
            row_on_0th_col = random.randint(1, n-1)
            row_on_last_col = row_on_0th_col
            board[row_on_0th_col][0] = 9
            board[row_on_last_col][n-1] = 9

            row_on_last_col_for_target = random.randint(0, n-2)
            board[row_on_last_col_for_target][n-1] = 8
            
            tempCol = random.randint(1, n-2)
            for row in range(1,n-1):
                board[row][tempCol] = 9
            return board
        elif level == 3:
            col = random.choice([n-2, n-3, n-1])

            if(col == n-3) or (col == n-2):
                row_on_that_col = random.randint(3, n-3)

                board[row_on_that_col][col] = 8
                board[row_on_that_col][col-1] = 9
                board[row_on_that_col][col-4] = 9
                board[row_on_that_col][col-3] = 7
                for row in range(1, n):
                    board[row][col-1] = 9
                board[row_on_that_col][0] = 9

            else:
                board[0][col] = 8
                row_for_cube = random.randint(3, n-3)
                col_for_cube = random.randint(3, n-3)
                board[row_for_cube][col_for_cube] = 7
                board[row_for_cube][col_for_cube-1] = 9
                board[row_for_cube][col] = 9
                board[row_for_cube][0] = 9
                if(n != 6):
                    for row in range(row_for_cube+1, n):
                        board[row][col_for_cube] = 9
                for row in range(0, n-3):
                    board[row][col-2] = 9
            
            return board
        # level creation
        elif level == 4:
            for row in range(n):
                for col in range(n):
                    board[row][col] = 10
            return board





    def draw(self, screen, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
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
                # jump
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
                    iso_y -= self.halfTileHeight+8
                    screen.blit(tileImage, (iso_x, iso_y))
                # target tiles
                elif(num == 8):
                    tile = TargetTile()
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
                # empty spots
                elif (num == 9):
                    continue
                else:
                    tile = EmptyTile()
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.cols, self.halfTileWidth, self.halfTileHeight, screen)
                    screen.blit(tileImage, (iso_x, iso_y))
        

        
        


