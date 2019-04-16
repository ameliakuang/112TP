import pygame

class Tiles(pygame.sprite.Sprite):
    def __init__(self, row, col):
        self.location = (row, col)


