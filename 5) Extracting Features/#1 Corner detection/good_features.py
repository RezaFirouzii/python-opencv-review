import cv2 as cv
import numpy as np


if __name__ == "__main__":
    img = cv.imread('../../assets/test10.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)
    cv.imshow("Original Image", img)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # detecting corners using good features 
    corners = cv.goodFeaturesToTrack(gray_img, 100, 0.05, 25)   # second param is how many corners we want
    corners = np.float32(corners)
    
    # for each corner coordiantes, draw a filled circles
    for item in corners:
        x, y = item[0]
        img = cv.circle(img, (x, y), 5, 255, -1)

    cv.imshow('Corners Detected Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

