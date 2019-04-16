import pygame
from Player import Player


class Board(object):
    def __init__(self, rows, player):
        self.rows = self.cols = rows
        self.board = Board.generateBoard(self.rows)
        self.tile0 = pygame.image.load('grass.png').convert_alpha()
        self.tile1 = pygame.image.load('wall.png').convert_alpha()
        self.playerTile = player.image
        self.tileWidth = 64
        self.tileHeight = 64

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
                cart_x = row * self.tileWidth//2
                cart_y = col * self. tileHeight//2
                iso_x = (cart_x - cart_y) 
                iso_y = (cart_x + cart_y)/2
                centered_x = screen.get_rect().centerx + iso_x
                centered_y = screen.get_rect().centery/2 + iso_y
                screen.blit(tile, (centered_x, centered_y))
