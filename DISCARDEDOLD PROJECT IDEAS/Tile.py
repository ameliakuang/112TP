# Tile.py
## A generic Tile class

import pygame
import os
from pygamegame import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.centerx, self.centery = centerx, centery

    def move(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (300, 300))

class NormalTile(Tile):
    def __init__(self, centerx, centery):
        super().__init__(centerx, centery)
        image = pygame.image.load("images/normalTile.png").convert_alpha()
        self.image = pygame.transform.scale(image, (50, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

class UnstableTile(Tile):
    def __init__(self, centerx, centery):
        super().__init__(centerx, centery)
        image = pygame.image.load("images/blockTile.png").convert_alpha()
        self.image = pygame.transform.scale(image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery



class Obstruction(Tile):
    def __init__(self, centerx, centery):
        super().__init__(centerx, centery)
        image = pygame.image.load("images/blockTile.png").convert_alpha()
        self.image = pygame.transform.scale(image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    # An ObstructionTile cannot be moved.
    def move(self):
        return

