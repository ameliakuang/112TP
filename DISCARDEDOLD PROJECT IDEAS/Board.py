# Board.py
## Creates a 2D list that represents the board, 0 for none,
## 1 for normalTile

import pygame
from pygamegame import *

class Board(PygameGame):
    def __init__(self):
        self.board = Game.generateBoard(5)
        self.

    @staticmethod
    def generateBoard(num):
        board = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            ]      
        return board  

    def redrawAll(self, screen):



    

