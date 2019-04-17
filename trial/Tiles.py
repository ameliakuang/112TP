import pygame
import utility
'''
-1: is for player, and a normal tile should be placed
0: normal tiles
1,2,3,4: direction tiles
5: portal tiles
6: jump tiles
7: cube 
'''

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/tiles/normal.png').convert_alpha()
        self.rect = self.image.get_rect()


class DireTile(Tile):
	def __init__(self, dire):
		self.image = pygame.image.load('images/tiles/dire'+str(dire)+".png").convert_alpha()
		self.rect = self.image.get_rect()

class PortalTile(Tile):
	def __init__(self, dire):
		self.image = pygame.image.load('images/tiles/portal.png').convert_alpha()
		self.rect = self.image.get_rect()


