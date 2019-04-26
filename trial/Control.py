import pygame
from Player import *
from Tiles import *

class Control(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/tiles/normal.png').convert_alpha()
        self.rect = self.image.get_rect()

class Begin(Control):
    def __init__(self, screenWidth, screenHeight):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/icons/begin.png').convert_alpha()
        self.rect = self.image.get_rect()
        #print(self.rect.x, self.rect.y)
        self.rect.x, self.rect.y = screenWidth-120, screenHeight-120

class Reset(Control):
    def __init__(self, screenWidth, screenHeight):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/icons/return.png').convert_alpha()
        self.rect = self.image.get_rect()
        #print(self.rect.x, self.rect.y)
        self.rect.x, self.rect.y = screenWidth-90, -20

class Menu(Control):
    def __init__(self, screenWidth, screenHeight):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/icons/menuList.png').convert_alpha()
        self.rect = self.image.get_rect()
        #print(self.rect.x, self.rect.y)
        self.rect.x, self.rect.y = -7, -10


class controlBar(Control):
    def __init__(self, screenWidth, screenHeight):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((screenWidth-100, 200))
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
        jumpTile = JumpTile()
        cube = Cube()
        player = Player()
        targetTile = TargetTile()
        self.tileOptions.add(portalTile)
        self.tileOptions.add(jumpTile)
        self.tileOptions.add(cube)
        self.tileOptions.add(targetTile)
        self.tileOptions.add(player)

        self.tileRectList = []

    def draw(self, screen, screenWidth, screenHeight):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for tile in self.tileOptions:
            # for target tile
            if isinstance(tile, TargetTile):
                x, y = 10 + 80*8, screenHeight - 70
                self.tileRectList.append(screen.blit(tile.image, (x, y)))
            # for cube
            elif isinstance(tile, Cube):
                x, y = 10 + 80*tile.type, screenHeight-80
                self.tileRectList.append(screen.blit(tile.image, (x, y)))
            # for the other tiles
            elif not isinstance(tile, Player):
                x, y = 10+80*tile.type, screenHeight-70
                self.tileRectList.append(screen.blit(tile.image, (x, y)))
            # for the player
            else:
                x, y = 10+80*9, screenHeight-70
                tile.image.set_colorkey((255,255,255))
                self.tileRectList.append(screen.blit(tile.image, (x, y)))
            







