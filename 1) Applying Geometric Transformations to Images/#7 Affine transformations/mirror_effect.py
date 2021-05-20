import cv2 as cv
import numpy as np


if __name__ == "__main__":
    
    img = cv.imread("../assets/test5.jpg")
    rows, cols = img.shape[:2]

    cv.imshow("Original Image", img)

    # source points
    src = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
    # destination points
    dst = np.float32([[cols - 1, 0], [0, 0], [cols - 1, rows - 1]])

    # creating the transformation matrix
    affine_matrix = cv.getAffineTransform(src, dst)
    output = cv.warpAffine(img, affine_matrix, (cols, rows))

    cv.imshow("Mirror Image", output)
    cv.waitKey(0)
    cv.destroyAllWindows()