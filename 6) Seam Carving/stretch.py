# resizing img to a larger img
# by increasing width and height
# based on uninteresting regions

import cv2 as cv
import seamcarving

if __name__ == "__main__":
    # make sure the size of the input image is reasonable
    # large images take a lot of time to be processed
    # recommended size is 640x480
    img = cv.imread('../assets/test12.jpg')

    # dw & dh are differences of the current width and height with new shape or
    # simply number of rows and columns to be add to the new img
    # e.g. dh = 5 => adding 5 rows to height (5*cols pixels to be added in total)
    dw, dh = 30, 20

    img_seam = img.copy()
    for _ in range(dw):
        energy_matrix = seamcarving.create_energy_matrix(img_seam)
        seam = seamcarving.find_vertical_seam(img_seam, energy_matrix)
        img_seam = seamcarving.add_vertical_seam(img_seam, seam)

    for _ in range(dh):
        energy_matrix = seamcarving.create_energy_matrix(img_seam)
        seam = seamcarving.find_horizontal_seam(img_seam, energy_matrix)
        img_seam = seamcarving.add_horizontal_seam(img_seam, seam)

    print("original  image shape: ", img.shape)
    print("stretched image shape: ", img_seam.shape)

    cv.imshow("Original Image", img)
    cv.imshow("Stretched Image", img_seam)
    cv.waitKey(0)
    cv.destroyAllWindows()

# running this code might take a while
# it is based on dw, dh and the size of input img
# the larger these params are, the longer it takes
