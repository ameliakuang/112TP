def mapToIso(row, col, halfWidth, halfHeight):
    iso_x = (row*halfWidth - col * halfHeight)
    iso_y = (row*halfWidth + col*halfHeight)/2
    return (iso_x, iso_y)
    

def isoToMap(iso_x, iso_y, halfWidth, halfHeight):
    row = x / halfWidth + y / halfHeight
    col = y / halfHeight*2 - x / halfWidth*2
    return (row, col)