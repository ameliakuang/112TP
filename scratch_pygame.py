import pygame
from pygame.locals import *
 
pygame.init()
 
DISPLAYSURF = pygame.display.set_mode((640, 480), DOUBLEBUF)    #set the display mode, window title and FPS clock
pygame.display.set_caption('Map Rendering Demo')
FPSCLOCK = pygame.time.Clock()
 
map_data = [
[0, 0, 0, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1]
]               #the data for the map expressed as [row[tile]].
 
wall = pygame.image.load('wall.png').convert_alpha()  #load images
grass = pygame.image.load('grass.png').convert_alpha()
 
TILEWIDTH = 64  #holds the tile width and height
TILEHEIGHT = 64
TILEHEIGHT_HALF = TILEHEIGHT /2
TILEWIDTH_HALF = TILEWIDTH /2
 
for row_nb in range(len(map_data)):    #for every row of the map...
    row = map_data[row_nb]
    for col_nb in range(len(row)):
        tile = row[col_nb]
        if tile == 1:
            tileImage = wall
        else:
            tileImage = grass
        cart_x = row_nb * TILEWIDTH_HALF
        cart_y = col_nb * TILEHEIGHT_HALF  
        iso_x = (cart_x - cart_y) 
        iso_y = (cart_x + cart_y)/2
        centered_x = DISPLAYSURF.get_rect().centerx + iso_x
        centered_y = DISPLAYSURF.get_rect().centery/2 + iso_y
        DISPLAYSURF.blit(tileImage, (centered_x, centered_y)) #display the actual tile
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
 
    pygame.display.flip()
    FPSCLOCK.tick(30)