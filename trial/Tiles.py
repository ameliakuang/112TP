# This file contains the Tile class.
import pygame
import utility
'''
-1: is for player, and a normal tile should be placed
0: normal tiles
1,2,3,4: direction tiles
5: portal tiles
6: jump tiles
7: cube 
8: target
9: empty
'''

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #super(Tile, self).__init__()
        self.image = pygame.image.load('images/tiles/normal.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.type = 0

class DireTile(Tile):
    def __init__(self, dire):
        super(DireTile, self).__init__()
        self.dire = dire
        self.image = pygame.image.load('images/tiles/dire'+str(self.dire)+".png").convert_alpha()
        self.rect = self.image.get_rect()
        self.type = dire

class PortalTile(Tile):
    def __init__(self):
        super(PortalTile, self).__init__()
        self.image = pygame.image.load('images/tiles/portal.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.type = 5


class JumpTile(Tile):
    def __init__(self):
        super(JumpTile, self).__init__()
        self.image = pygame.image.load('images/tiles/jump.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.type = 6

class Cube(Tile):
    def __init__(self):
        super(Cube, self).__init__()
        self.image = pygame.image.load('images/tiles/cube.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.type = 7

class TargetTile(Tile):
    def __init__(self):
        super(TargetTile, self).__init__()
        self.image = pygame.image.load('images/tiles/target.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.type = 8

class EmptyTile(Tile):
    def __init__(self):
        super(EmptyTile, self).__init__()
        self.image = pygame.image.load('images/tiles/empty.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.type = 10



