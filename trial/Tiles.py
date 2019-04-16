import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init()
        image = pygame.image.load('images/normal.png').convert_alpha()


class DireTile(Tile):
	def __init__(self, dire):
		image = pygame.image.load('images/dire'+str(dire)+".png").convert_alpha()

class PortalTile(Tile):
	def __init__(self, dire):
		image = pygame.image.load('images/portal.png').convert_alpha()


