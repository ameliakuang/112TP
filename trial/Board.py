import pygame
from Player import Player
from Tiles import *
import utility


class Board(object):
    def __init__(self, n, player):
        self.rows = self.cols = n
        self.board = Board.generateBoard(n)
        self.playerTile = player.image
        
        self.tileWidth = 72
        self.tileHeight = 72
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
    '''
    @staticmethod
    def generateBoard(n):
        board = [
            [-1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            ]       
        return board



    def draw(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                num = self.board[row][col]
                # the player position
                if(num == -1):
                    num = 0 # just place a normal tile there
                    tile = Tile()
                    tileImage = tile.image
                    iso_x, iso_y = utility.mapToIso(row, col, self.halfTileWidth, self.halfTileHeight)
                    centered_x = screen.get_rect().centerx + iso_x
                    centered_y = screen.get_rect().centery//2 + iso_y
                    screen.blit(tileImage, (centered_x, centered_y))
                elif(num == 10):
                    continue
                elif(num == 12):
                    continue
                else:
                    continue
                # CITATION: the conversion from cartesian coordinates to isometric coordinates
                # is from https://opengameart.org/content/cannonball
                '''
                # cart_x, cart_y: square map's row and col 
                cart_x = row * self.halfTileWidth
                cart_y = col * self.halfTileHeight
                # iso_x, iso_y: isometric map's x and y coordinates
                iso_x = (cart_x - cart_y) 
                iso_y = (cart_x + cart_y)/2
                
                # The above calculation is equivalent to:
                # iso_x = (row-col)*self.halfTileWidth
                # iso_y = ((row+col)*self.halfTileHeight)//2

                centered_x = screen.get_rect().centerx + iso_x
                centered_y = screen.get_rect().centery//2 + iso_y
                #pygame.draw.rect(screen, (0, 100, 0), (centered_x, centered_y, self.tileWidth, self.tileHeight))
                screen.blit(tile, (centered_x, centered_y))
                '''
        
        screen.blit(self.playerTile, (300, 100))



