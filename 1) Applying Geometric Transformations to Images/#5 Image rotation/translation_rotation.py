# preventing getting cropped after rotation

import cv2 as cv
import numpy as np
import math


if __name__ == "__main__":
    
    img = cv.imread("../../assets/test4.jpg")
    img = cv.resize(img, None, fx=.5, fy=.5)    # ignore this line as we'll get through it next part
    height, width = img.shape[:2]

    ANGLE = 45  # degree

    diameter = int(math.hypot(width, height))

    dx = (diameter - width)  // 2
    dy = (diameter - height) // 2

    # translating image to center so the result won't be cropped
    translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    img = cv.warpAffine(img, translation_matrix, (diameter, diameter))
    cv.imshow("Original Image", img)

    # rotating img 45 deg with rotation point equal to center of img
    rotation_matrix = cv.getRotationMatrix2D((diameter // 2, diameter // 2), ANGLE, 1)
    output = cv.warpAffine(img, rotation_matrix, (diameter, diameter))
    cv.imshow("Rotated Image", output)
    print(output.shape)


    cv.waitKey(0)
    cv.destroyAllWindows()
