import cv2 as cv
import numpy as np


if __name__ == "__main__":
    img = cv.imread('../../assets/test1.jpg')
    cv.imshow("Original Image", img)

    # to sharpen an image, we gotta make a kernel matrix
    # this kernel must have negative values such that the
    # sum of all values equals 1

    # example 1
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    output = cv.filter2D(img, -1, kernel)
    cv.imshow("First Sharpened Sample", output)

    # example 2
    kernel = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
    output = cv.filter2D(img, -1, kernel)
    cv.imshow("Second Sharpened Sample", output)

    # example 3
    kernel = np.full((5, 5), -1)
    kernel[1:4, 1:4] = np.full((3, 3), 2)
    kernel[2, 2] = 8
    kernel = kernel / 8   # sum of kernel must be 1
    output = cv.filter2D(img, -1, kernel)
    cv.imshow("Third Sharpened Sample", output)

    cv.waitKey(0)
    cv.destroyAllWindows()

# try to mess with the values of kernel matrices
# and run the code to see how new results differ
# compared to previous ones