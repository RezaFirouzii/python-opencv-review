import cv2 as cv
import numpy as np


if __name__ == "__main__":
    img = cv.imread('../../assets/test15.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)
    cv.imshow('Original Image', img)

    # to apply embossing filter we must change the color space to gray
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # embossing kernel features:
    #   1. sum of all values equals 0
    #   2. kernel matrix must be symmetric
    #      as it declares the direction of embossing
    #   3. in order to create a direction for embossing,
    #      put the positive values in the same direction in matrix


    # example 1
    # north-west embossing kernel
    kernel = np.array([
        [1, 0,  0],
        [0, 0,  0],
        [0, 0, -1]
    ])
    output = cv.filter2D(gray_img, -1, kernel) + 128    # 128 is the offset
    cv.imshow("North West Embossing", output)

    # example 2
    # south-east embossing kernel
    kernel = np.array([
        [-1, -1, 0],
        [-1,  0, 1],
        [ 0,  1, 1]
    ])
    output = cv.filter2D(gray_img, -1, kernel) + 128
    cv.imshow("South East Embossing", output)

    cv.waitKey(0)
    cv.destroyAllWindows()