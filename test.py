import cv2 as cv
import numpy as np

if __name__ == "__main__":
    img = cv.imread('assets/test14.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)
    cv.imshow("d", img)
    mask = cv.inRange(img, (0, 0, 0), (200, 200, 200))
    img = cv.bitwise_and(img, img, mask=mask)
    cv.imshow('', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
