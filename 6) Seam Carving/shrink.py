# resizing img to a smaller img
# by reducing width and height
# based on uninteresting regions

import cv2 as cv
import seamcarving

if __name__ == "__main__":
    # make sure the size of the input image is reasonable
    # large images take a lot of time to be processed
    # recommended size is 640x480
    img = cv.imread('../assets/test5.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)

    # dw & dh are differences of the current width and height with new shape or
    # simply number of rows and columns to be reduced in new img
    # e.g. dw = 20 => reducing the width by 20 columns (20*rows pixels in total)
    dw, dh = 30, 30

    img_seam = img.copy()

    # deleting 1px of each row located in most uninterestring regions each time in loop
    for _ in range(dw):
        energy_matrix = seamcarving.create_energy_matrix(img_seam)
        seam = seamcarving.find_vertical_seam(img_seam, energy_matrix)
        img_seam = seamcarving.remove_vertical_seam(img_seam, seam)

    # deleting 1px of every column located in most uninterestring regions each time in loop
    for _ in range(dh):
        energy_matrix = seamcarving.create_energy_matrix(img_seam)
        seam = seamcarving.find_horizontal_seam(img_seam, energy_matrix)
        img_seam = seamcarving.remove_horizontal_seam(img_seam, seam)

    print("original image shape: ", img.shape)
    print("shrinked image shape: ", img_seam.shape)

    cv.imshow("Original Image", img)
    cv.imshow("Shrinked Image", img_seam)
    cv.waitKey(0)
    cv.destroyAllWindows()

# running this code might take a while
# it is based on dw, dh and the size of input img
# the larger these params are, the longer it takes
