import cv2 as cv
import numpy as np


if __name__ == "__main__":
    img = cv.imread('../../assets/test3.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)
    cv.imshow('Original Image', img)

# a blurring kernel matrix has the following properties:
#       1: "all the values in blurring kernels are positive"
#       2: "the sum of all the values is equal to 1"
#       3: "as the size of the kernel grows, more smoothing effect will take place."

    # 3 by 3 kernel matrix
    kernel_3x3 = np.ones((3, 3), np.float)
    kernel_3x3 = kernel_3x3 / np.sum(kernel_3x3)    # normalizing kernel
    blur_img = cv.filter2D(img, -1, kernel_3x3)     # applying the kernel effect
    cv.imshow('Blur Image with 3x3 Kernel', blur_img)

    # 7 by 7 kernel matrix
    kernel_7x7 = np.ones((7, 7), np.float)
    kernel_7x7 = kernel_7x7 / np.sum(kernel_7x7)
    blur_img = cv.filter2D(img, -1, kernel_7x7)
    cv.imshow('Blur Image with 7x7 Kernel', blur_img)

    # in both above examples we make the kernel ourselves manually
    # opencv has a method called cv.blur() which takes care of the kernel for us
    # we just have to specify how blur should be the output (how big the kernel shape is)

    blur_img = cv.blur(img, (11, 11))     # creates a 11 by 11 kernel
    cv.imshow('Blur Image by cv.blur() and 11x11 Kernel', blur_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

# compare all four outputs.
# as you see the bigger the kernel shape is,
# the blurrer output image will be.

# size of kernel ∝ size of blurrines