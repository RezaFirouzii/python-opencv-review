import cv2 as cv
import numpy as np
from os import listdir
from skimage.metrics import structural_similarity


def match(rects):
    names = [f for f in listdir('patterns')]
    patterns = [cv.imread('patterns/%s'%f, 0) for f in listdir('patterns')]

    patterns = list(map(lambda x: cv.adaptiveThreshold(x, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 15, 10), patterns))
    
    k = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
    patterns = list(map(lambda x: cv.morphologyEx(x, cv.MORPH_OPEN, k), patterns))

    k = cv.getStructuringElement(cv.MORPH_ELLIPSE, (9, 9))
    patterns = list(map(lambda x: cv.morphologyEx(x, cv.MORPH_CLOSE, k), patterns))

    patterns = list(map(lambda x: cv.medianBlur(x, 7), patterns))
    patterns = list(map(lambda x: cv.Canny(x, 50, 240), patterns))
    
    cnts = list(map(lambda x: cv.findContours(x, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)[0][0], patterns))
    cnts = list(map(cv.boundingRect, cnts))
    
    for i in range(len(cnts)):
        x, y, w, h = cnts[i]
        patterns[i] = patterns[i][y: y+h, x: x+w]

    text = []
    for image in rects:
        char = ''
        max_similarity = 0

        for i in range(len(patterns)):
            symbol, pattern = names[i][0], patterns[i]
            pattern = cv.resize(pattern, tuple(reversed(image.shape[:2])))
            score = structural_similarity(image, pattern, full=True)[0]
            if score > max_similarity:
                max_similarity = score
                char = symbol

        text.append(char)
    return ''.join(text)


# sorting contours from left to right
def sort_contours(contours):
    dic = {}
    for contour in contours:
        x_points = contour[:, :, 0]
        dic[min(x_points)[0]] = contour
    
    dic = dict(sorted(dic.items()))
    return dic.values()


if __name__ == "__main__":
    captcha = cv.imread('abcd123.png', 0)
    img = captcha.copy()
    
    # removing extra horizontal lines and noises
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 10))
    captcha = cv.morphologyEx(captcha, cv.MORPH_CLOSE, kernel)
    
    captcha = cv.adaptiveThreshold(captcha, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 15, 10)
    
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
    captcha = cv.morphologyEx(captcha, cv.MORPH_OPEN, kernel)

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (9, 9))
    captcha = cv.morphologyEx(captcha, cv.MORPH_CLOSE, kernel)

    captcha = cv.medianBlur(captcha, 5)
    captcha = cv.Canny(captcha, 50, 240)


    contours, hierarchy = cv.findContours(captcha, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    contours = filter(lambda x: cv.contourArea(x) > 1e3, contours)
    contours = sort_contours(contours)

    rects = list(map(cv.boundingRect, contours))
    rects = list(map(lambda rect: captcha[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]], rects))

    result = match(rects)
    print(result)