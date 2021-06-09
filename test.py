import cv2 as cv
from math import sqrt
import numpy as np

GREEN = (0, 153, 0)

if __name__ == "__main__":
    
    img = cv.imread('assets/test4.jpg')
    cv.imshow('1', img)
    img = cv.add(img, 50)
    cv.imshow('', img)
    cv.waitKey(0)
    cv.destroyAllWindows()