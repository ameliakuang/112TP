import cv2
import numpy as np

def getPoints():
    pass

def getTransformation(inv = False):
    dst_w = 70
    dst_h = 44
    src = np.zeros((3,2), dtype = np.float32)
    dst = np.zeros((3,2), dtype = np.float32)
    src[0, :] = (300, 100)
    src[1, :] = (195, 166)
    src[2, :] = (300, 232)
    dst[0, :] = (0, 0)
    dst[1, :] = (195, 166)
    dst[2, :] = (300, 232)

    if inv:
        trans = cv2.getAffineTransform(np.float32(dst), np.float32(src))
    else:
        trans = cv2.getAffineTransform(np.float32(dst), np.float32(src))
    return trans

print(getTransformation())



def mapToIso(row, col, halfWidth, halfHeight):
    iso_x = (row*halfWidth - col * halfHeight)
    iso_y = (row*halfWidth + col*halfHeight)/2
    return (iso_x, iso_y)
    
# not sure if works at all
def isoToMap(iso_x, iso_y, halfWidth, halfHeight):
    row = x / halfWidth + y / halfHeight
    col = y / halfHeight*2 - x / halfWidth*2
    return (row, col)