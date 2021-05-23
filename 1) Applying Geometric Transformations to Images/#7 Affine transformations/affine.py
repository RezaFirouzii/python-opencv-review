import cv2 as cv
import numpy as np


if __name__ == "__main__":
    
    img = cv.imread("../../assets/test3.jpg")
    img = cv.resize(img, None, fx=.5, fy=.5)
    rows, cols = img.shape[:2]

    cv.imshow("Original Image", img)

    # example 1
    # source points
    src = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
    # destination points
    dst = np.float32([[cols // 3, 0], [cols - 1, 0], [cols // 2, rows - 1]])

    # creating the transformation matrix
    affine_matrix = cv.getAffineTransform(src, dst)
    output = cv.warpAffine(img, affine_matrix, (cols, rows))

    cv.imshow("Example 1", output)

    # example 2
    src = np.float32([[0, 0], [0, rows - 1], [cols - 1, rows - 1]])
    dst = np.float32([[0, 0], [cols // 3, rows - 1], [cols - 1, (rows - 1) // 2]])
    affine_matrix = cv.getAffineTransform(src, dst)
    output = cv.warpAffine(img, affine_matrix, (cols, rows))

    cv.imshow("Example 2", output)

    # example 3
    src = np.float32([[0, 0], [0, rows - 1], [cols - 1, rows - 1]])
    dst = np.float32([[0, 0], [0, rows // 2], [cols - 1, 2 * rows // 3]])
    affine_matrix = cv.getAffineTransform(src, dst)
    output = cv.warpAffine(img, affine_matrix, (cols, rows))

    cv.imshow("Example 3", output)


    cv.waitKey(0)
    cv.destroyAllWindows()