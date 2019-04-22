# Citation: http://clintbellanger.net/articles/isometric_math/
def mapToIso(row, col, cols, halfWidth, halfHeight, screen):
    iso_x = (row-col) * halfWidth
    iso_y = (row+col) * halfHeight
    # adjust the coordinates to be on the center
    newIso_x = iso_x + screen.get_rect().centerx - halfWidth
    newIso_y = iso_y + screen.get_rect().centery - cols*halfHeight
    return (newIso_x, newIso_y)
    
# not sure if works at all
def isoToMap(iso_x, iso_y, halfWidth, halfHeight):
    row = x / halfWidth + y / halfHeight
    col = y / halfHeight*2 - x / halfWidth*2
    return (row, col)