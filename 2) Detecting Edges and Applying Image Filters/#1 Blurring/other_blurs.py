import cv2 as cv
import numpy as np


if __name__ == "__main__":
    img = cv.imread('../../assets/test1.jpg')
    cv.imshow('Original Image', img)
    size = 9    # all kernels will be 9x9

    # median blur filter
    blur_img = cv.medianBlur(img, size)
    cv.imshow("Median Blur Output", blur_img)

    # guassian blur filter
    blur_img = cv.GaussianBlur(img, (size, size), 0)
    cv.imshow("Guassian Blur Output", blur_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

# hint:
    # "median blur"
       # median blur is used to remove salt-pepper noise.
       # it takes the median of a pixel neighbors and replaces it with the median.
    
    # "guassian blur"
       # guassian blur smoothens everything out equally.
       # it makes no difference for edges and makes every pixel blur.