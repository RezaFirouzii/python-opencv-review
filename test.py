import cv2 as cv
import numpy as np

if __name__ == "__main__":
    img = cv.imread('assets/test1.jpg')
    copy = img.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(img, 7)
    img = cv.Laplacian(img, cv.CV_8U, ksize=5)
    res, img = cv.threshold(img, 100, 250, cv.THRESH_BINARY_INV)
    cv.imshow('i;, ', img)
    img = cv.bitwise_and(copy, copy, mask=img)
    cv.imshow('', img)
    print(img)
    cv.waitKey(0)
    cv.destroyAllWindows()
