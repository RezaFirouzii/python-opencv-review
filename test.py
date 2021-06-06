import cv2 as cv
from math import sqrt

GREEN = (0, 153, 0)

if __name__ == "__main__":
    
    img = cv.imread('assets/test4.jpg')
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    res, mask = cv.threshold(gray_img, 100, 255, 0)
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[3]
    print(cv.contourArea(cnt))
    # cv.waitKey(0)
    # cv.destroyAllWindows()