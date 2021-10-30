import cv2 as cv
import numpy as np
from PIL import Image


if __name__ == "__main__":
    img = cv.imread('../assets/test16.jpg')
    org = img.copy()

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 15, 10)

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
    img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (43, 5))
    img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

    # contour => array of shapes
    # shape   => array of points
    # point   => a tuple or [x, y]
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = list(filter(lambda x: cv.contourArea(x) > 8e3, contours))
    rects = list(map(cv.boundingRect, contours))

    for rectangle in rects:
        x, y, w, h = rectangle
        cv.rectangle(org, (x, y), (x + w, y + h), (255, 0, 0), 3)

    org = cv.resize(org, None, fx=.5, fy=.5)
    cv.imshow('', org)
    cv.waitKey(0)
    cv.destroyAllWindows()