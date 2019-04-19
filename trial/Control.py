import pygame
from Tiles import *

class Control(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/tiles/normal.png').convert_alpha()
        self.rect = self.image.get_rect()

class Begin(Control):
    def __init__(self, screenWidth, screenHeight):
        self.image = pygame.image.load('images/icons/right.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = screenWidth-80
        self.rect.centery = screenHeight-90

    def draw(self, screen):
        screen.blit(self.image, (self.rect.centerx, self.rect.centery))

class controlBar(Control):
    def __init__(self, screenWidth, screenHeight):
        self.image = pygame.Surface((screenWidth-100, 250))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = screenHeight-90

        self.tileOptions = pygame.sprite.Group()
        self.tileOptions.add(Tile())
        for i in range(1, 5):
            direTile = DireTile(i)
            self.tileOptions.add(direTile)
        portalTile = PortalTile()
        self.tileOptions.add(portalTile)

    def draw(self, screen, screenWidth, screenHeight):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for tile in self.tileOptions:
            x, y = 10+80*tile.type, screenHeight-70
            screen.blit(tile.image, (x, y))
            







