# BRIEF (Binary Robust Independent Elementary Features) algorithm
# computing decriptors quickly and extracting descriptor features
# FAST algorithm is used to detect keypoints in this case

import cv2 as cv


if __name__ == "__main__":
    img = cv.imread('../../assets/test10.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)

    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # initiate FAST detector
    star = cv.xfeatrues2d.StarDetector_create()

    # initiate BRIEF extractor
    brief = cv.xfeatrues2d.BriefDescriptorExtractor_create()

    # finding keypoints with STAR
    keypoints = star.detect(gray_img, None)

    # computing descriptors with BRIEF
    keypoints, descriptors = breif.compute(gray_img, keypoints)

    # drawing keypoints
    output = img.copy()
    cv.drawKeypoints(img, keypoints, output, (255, 0, 0))

    cv.imshow("BRIEF Keypoints", output)
    cv.waitKey(0)
    cv.destroyAllWindows()

# in order to get BRIEF methods and relevant objects
# you need to get extra modules of opencv in blow link:
# https://github.com/opencv/opencv_contrib
