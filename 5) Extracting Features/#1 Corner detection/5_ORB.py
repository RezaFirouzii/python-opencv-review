# ORB (Oriented FAST and Rotated BRIEF) algorithm
# the final corner detection algorithm as a combination of FAST & BRIEF
# a robust algorithm, free to use, open source and no extra lib needed.

import cv2 as cv


if __name__ == "__main__":
    img = cv.imread('../../assets/test10.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)

    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # initiate the ORB object
    orb = cv.ORB_create()

    # finding keypoints with ORB
    keypoints = orb.detect(gray_img, None)

    # computing descriptors with ORB
    keypoints, descriptors = orb.compute(gray_img, keypoints)

    # drawing keypoints without size or orientation
    output = img.copy()
    cv.drawKeypoints(img, keypoints, output, (255, 0, 0))

    cv.imshow('ORB Corner Detection', output)
    cv.waitKey(0)
    cv.destroyAllWindows()

# doc: https://docs.opencv.org/master/d1/d89/tutorial_py_orb.html