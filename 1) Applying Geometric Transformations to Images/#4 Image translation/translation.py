import cv2 as cv
import numpy as np

if __name__ == "__main__":
    
    img = cv.imread('../assets/test2.jpg')
    height, width = img.shape[:2]   # rows, columns

    # translating the img 200 pixels right (x axis)
    translation_matrix = np.float32([[1, 0, 200], [0, 1, 0]])
    output = cv.warpAffine(img, translation_matrix, (width, height))
    cv.imshow('1) 200 Pixels right', output)

    # translating the img 50 pixels down (y axis)
    translation_matrix = np.float32([[1, 0, 0], [0, 1, 50]])      
    output = cv.warpAffine(img, translation_matrix, (width, height))
    cv.imshow('2) 50 Pixels Down', output)

    # translating the img in both x-y axis.
    translation_matrix = np.float32([[1, 0, 200], [0, 1, 50]])
    output = cv.warpAffine(img, translation_matrix, (width, height))
    cv.imshow('3) (dx, dy) = (200, 50)', output)

    # translating without getting cropped (by increasing the output size)
    translation_matrix = np.float32([[1, 0, 200], [0, 1, 50]])
    output = cv.warpAffine(img, translation_matrix, (width + 200, height + 50))
    cv.imshow("4) Preventing Crop", output)

    cv.waitKey(0)
    cv.destroyAllWindows()
