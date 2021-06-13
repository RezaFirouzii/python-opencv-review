# resizing img to a smaller img
# by reducing width and height
# based on uninteresting regions

import cv2 as cv
import seamcarving

if __name__ == "__main__":
    # make sure the size of the input image is reasonable
    # large images take a lot of time to be processed
    # recommended size is 640x480
    img = cv.imread('../assets/test1.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)

    # dw & dh are differences of the current width and height with new shape or
    # simply number of pixels to be reduced in new img
    # e.g. dw = 20 => reducing the width by 20 pixels
    dw, dh = 10, 15

    img_seam = img.copy()
    for _ in range(dw):
        energy_matrix = seamcarving.create_energy_matrix(img_seam)
        seam = seamcarving.find_vertical_seam(img_seam, energy_matrix)
        img_seam = seamcarving.remove_vertical_seam(img_seam, seam)

    for _ in range(dh):
        energy_matrix = seamcarving.create_energy_matrix(img_seam)
        seam = seamcarving.find_horizontal_seam(img_seam, energy_matrix)
        img_seam = seamcarving.remove_horizontal_seam(img_seam, seam)


    cv.imshow("Original Image", img)
    cv.imshow("Resized Image", img_seam)
    cv.waitKey(0)
    cv.destroyAllWindows()
