def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    import decimal
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

# Citation: http://clintbellanger.net/articles/isometric_math/
def mapToIso(row, col, cols, halfWidth, halfHeight, screen):
    iso_x = (row-col) * halfWidth
    iso_y = (row+col) * halfHeight
    # adjust the coordinates to be on the center
    newIso_x = iso_x + screen.get_rect().centerx - halfWidth
    newIso_y = iso_y + screen.get_rect().centery - cols*halfHeight
    return (newIso_x, newIso_y)
    
# Citation: http://clintbellanger.net/articles/isometric_math/
def isoToMap(iso_x, iso_y, cols, halfWidth, halfHeight, screen):
    iso_x = iso_x - screen.get_rect().centerx + halfWidth - halfWidth
    iso_y = iso_y - screen.get_rect().centery + halfHeight*cols - halfHeight
    row = 1/2*(iso_x/halfWidth+iso_y/halfHeight)
    col = 1/2*(iso_y/halfHeight - iso_x/halfWidth)
    return (round(row), round(col))