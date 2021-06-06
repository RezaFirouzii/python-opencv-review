import cv2 as cv
import numpy as np


if __name__ == "__main__":
    img = cv.imread('../../assets/test10.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)
    cv.imshow("Original Image", img)
    
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray_img = np.float32(gray_img)

    # detecting corners using harris corner detection
    dst = cv.cornerHarris(gray_img, 5, 5, .04)
    # dilating for marking the corners
    dst = cv.dilate(dst, None)
    img[dst > 0.01 * dst.max()] = [0, 0, 0]

    cv.imshow('Corners Detected Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

# fill free to change the test img