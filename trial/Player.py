import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/circle.png').convert()
        self.rect = self.image.get_rect()

    def move(self, screenCenterX, screenCenterY, x, y):
        iso_x = (x - y) 
        iso_y = (x + y)/2
        centered_x = screenCenterX + iso_x
        centered_y = screenCenterY/2 + iso_y
        self.rect.centerx = centered_x
        self.rect.centery = centered_y




