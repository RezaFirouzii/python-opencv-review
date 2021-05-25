import cv2 as cv
import numpy as np


def cartoonize(image):
    scale_factor = 2
    sigma_color = 5
    sigma_space = 7
    # converting to gray color space
    edited_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    # applying median blur filter
    edited_img = cv.medianBlur(edited_img, 7)

    # detecting edges with laplacian method
    edited_img = cv.Laplacian(edited_img, cv.CV_8U, ksize=5)

    # creating the sketch mode with threshold
    res, mask = cv.threshold(edited_img, 100, 255, cv.THRESH_BINARY_INV) # returns (bool, ndarray)

    # since bilateral filter is a slow filter to be applied,
    # we resize it to a smaller shape for faster computation
    small_img = cv.resize(image, None, fx=1/scale_factor, fy=1/scale_factor)    # you can make it as small as you like but devidable

    # applying bilateral 10 times to smoothen more (making closer to cartoonish)
    for _ in range(10):
        small_img = cv.bilateralFilter(small_img, 7, sigma_color, sigma_space)

    # bringing back the normal scale
    small_img = cv.resize(small_img, None, fx=scale_factor, fy=scale_factor)

    # finally by applying the sketch mode mask to the original image we get the cartoonish effect
    cartoonized_img = cv.bitwise_and(small_img, small_img, mask=mask)

    # return sketch mode and cartoonized
    return mask, cartoonized_img


if __name__ == "__main__":
    # multiple sketch mode and cartoonized images
    # displaying each 2 for 5 seconds

    # example 1
    img = cv.imread('../../assets/test1.jpg')
    sketch, cartoon = cartoonize(img)
    cv.imshow('Sketch Mode', sketch)
    cv.imshow('Cartoonize Image', cartoon)
    cv.waitKey(5000)

    # example 2
    img = cv.imread('../../assets/test4.jpg')
    sketch, cartoon = cartoonize(img)
    cv.imshow('Sketch Mode', sketch)
    cv.imshow('Cartoonize Image', cartoon)
    cv.waitKey(5000)
    
    # example 3
    img = cv.imread('../../assets/test5.jpg')
    sketch, cartoon = cartoonize(img)
    cv.imshow('Sketch Mode', sketch)
    cv.imshow('Cartoonize Image', cartoon)
    cv.waitKey(5000)
    
    cv.destroyAllWindows()
