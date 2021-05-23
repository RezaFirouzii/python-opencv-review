import cv2 as cv

if __name__ == "__main__":
    img = cv.imread('assets/test5.jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('g', img)
    img = cv.medianBlur(img, 7)
    img = cv.Laplacian(img, cv.CV_8U, ksize=5)
    cv.imshow('l', img)
    res, img = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)
    cv.imshow('threshold', img)
    cv.waitKey(0)
    cv.destroyAllWindows()