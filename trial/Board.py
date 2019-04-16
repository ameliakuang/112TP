import pygame
from Player import Player
from Tiles import *


class Board(object):
    def __init__(self, n, player):
        self.rows = self.cols = n
        self.board = Board.generateBoard(n)
        self.tile0 = pygame.image.load('images/tiles/normal.png').convert_alpha()
        self.tile1 = pygame.image.load('images/tiles/target.png').convert_alpha()
        self.playerTile = player.image
        
        self.tileWidth = 64
        self.tileHeight = 64
        self.halfTileWidth = self.tileWidth//2
        self.halfTileHeight = self.tileHeight//2


    # first randomly generate tiles, 
    # and then use backtracking to generate the board
    @staticmethod
    def generateBoard(n):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 10, 0],
            [0, 0, 0, 12, 0],
            ]       
        return board



    def draw(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                num = self.board[row][col]
                if(num == 0):
                    tile = self.tile0
                elif(num == 10):
                    continue
                elif(num == 12):
                    tile = self.playerTile
                else:
                    tile = self.tile1
                # CITATION: the conversion from cartesian coordinates to isometric coordinates
                # is from https://opengameart.org/content/cannonball
                '''
                # cart_x, cart_y: square map's row and col coordinates
                cart_x = row * self.halfTileWidth
                cart_y = col * self.halfTileHeight
                # iso_x, iso_y: isometric map's row and col coordinates
                iso_x = (cart_x - cart_y) 
                iso_y = (cart_x + cart_y)/2
                '''
                # The above calculation is equivalent to:
                iso_x = (row-col)*self.halfTileWidth
                iso_y = ((row+col)*self.halfTileHeight)//2

                centered_x = screen.get_rect().centerx + iso_x
                centered_y = screen.get_rect().centery//2 + iso_y
                #pygame.draw.rect(screen, (0, 100, 0), (centered_x, centered_y, self.tileWidth, self.tileHeight))
                screen.blit(tile, (centered_x, centered_y))











