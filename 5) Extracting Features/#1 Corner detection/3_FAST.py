# FAST (Features from Accelerated Segment Test) algorithm for feature detection
# free to use algorithm inspired by SIFT & SURF algorithms (patented, not free!)

import cv2 as cv


if __name__ == "__main__":
    img = cv.imread('../../assets/test10.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Initiate FAST object with default values
    fast = cv.FastFeatureDetector_create()

    # finding and drawing the keypoints
    keypoints = fast.detect(gray_img, None)
    img_keypoints_with_nonmax = img.copy() # output
    # params:       input   keypts  ouput   color
    cv.drawKeypoints(img, keypoints, img_keypoints_with_nonmax, (0, 0, 255)) # drawing on keypoints on the main img

    print("Threshold: {}".format(fast.getThreshold()))
    print("nonmaxSuppression: {}".format(fast.getNonmaxSuppression()))
    print("neighborhood: {}".format(fast.getType()))
    print("Total Keypoints with nonmaxSuppression: {}".format(len(keypoints)))

    cv.imshow('FAST Keypoints with non Max Suppression', img_keypoints_with_nonmax)

    # disable nonmaxSuppression
    fast.setNonmaxSuppression(False)
    # detecting keypoints again
    keypoints = fast.detect(gray_img, None)
    img_keypoints_without_nonmax = img.copy() # output
    cv.drawKeypoints(img, keypoints, img_keypoints_without_nonmax, (0, 0, 255))

    print()
    print("Threshold: {}".format(fast.getThreshold()))
    print("nonmaxSuppression: {}".format(fast.getNonmaxSuppression()))
    print("neighborhood: {}".format(fast.getType()))
    print("Total Keypoints without nonmaxSuppression: {}".format(len(keypoints)))
    
    cv.imshow('FAST Keypoints without non Max Suppression', img_keypoints_without_nonmax)
    cv.waitKey(0)
    cv.destroyAllWindows()


# doc: https://docs.opencv.org/master/df/d0c/tutorial_py_fast.html 
