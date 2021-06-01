import cv2 as cv
import numpy as np


if __name__ == "__main__":
    img = cv.imread('../../assets/test1.jpg')
    cv.imshow("Original Image", img)

    rows, cols = img.shape[:2]

    # creating vignette mask using guassian kernels
    kernel_x = cv.getGaussianKernel(cols, 200)
    kernel_y = cv.getGaussianKernel(rows, 200)
    print(kernel_x.shape)
    print(kernel_y.shape)
    kernel = kernel_y * kernel_x.T

    print(np.linalg.norm(kernel))