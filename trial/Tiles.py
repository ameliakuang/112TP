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
        # self.rect.x = 10
        # self.rect.y = 400-85
        

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class DireTile(Tile):
    def __init__(self, dire):
        self.image = pygame.image.load('images/tiles/dire'+str(dire)+".png").convert_alpha()
        self.rect = self.image.get_rect()
        # self.rect.x = 10+80*dire
        # self.rect.y = 400-85

class PortalTile(Tile):
    def __init__(self):
        self.image = pygame.image.load('images/tiles/portal.png').convert_alpha()
        self.rect = self.image.get_rect()
        # self.rect = 10+80*5
        # self.rect.y = 400-85

class TargetTile(Tile):
    def __init__(self):
        self.image = pygame.image.load('images/tiles/target.png').convert_alpha()
        self.rect = self.image.get_rect()


