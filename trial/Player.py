import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/circle.png').convert()
        self.rect = self.image.get_rect()

    def move(self, screenCenterX, screenCenterY, x, y):
        pass

    




