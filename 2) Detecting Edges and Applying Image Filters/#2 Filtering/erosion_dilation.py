import cv2 as cv
import numpy as np


if __name__ == "__main__":
    # in order to apply erosion and dilation,
    # we should convert the color space to gray.
    # so we read the image in gray scale.
    img = cv.imread('../../assets/test1.jpg', 0)
    cv.imshow("Original Image", img)

    kernel = np.ones((5, 5))

    # iteration param specifies the intensity of erode/dilate operation
    img_erosion = cv.erode(img, kernel, iterations=1)
    cv.imshow("Erosion Filter", img_erosion)

    img_dilation = cv.dilate(img, kernel, iterations=1)
    cv.imshow("Dilation Filter", img_dilation)

    cv.waitKey(0)
    cv.destroyAllWindows()
