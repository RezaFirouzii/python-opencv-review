import cv2 as cv
import numpy as np


if __name__ == "__main__":

    img = cv.imread("../../assets/test2.jpg")  # fox 
    rows, cols = img.shape[:2]

    cv.imshow("Original Image", img)

    # example 1
    # source points
    src = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
    # destination points
    dst = np.float32([[50, 50], [cols - 1, rows / 3], [cols / 3, rows - 1], [2 * cols / 3, rows - 1]])

    # tranformation matrix
    projective_matrix = cv.getPerspectiveTransform(src, dst)
    output = cv.warpPerspective(img, projective_matrix, (rows, cols))

    cv.imshow("Example 1", output)
    
    # example 2
    src = np.float32([[0,   0], [cols / 2, 0], [0, rows - 1  ], [cols / 2, rows - 1]])
    dst = np.float32([[0, 100], [cols / 2, 0], [0, rows - 101], [cols / 2, rows - 1]])
    
    projective_matrix = cv.getPerspectiveTransform(src, dst)
    output = cv.warpPerspective(img, projective_matrix, (rows, cols))

    cv.imshow("Example 2", output)
    cv.waitKey(0)
    cv.destroyAllWindows()
