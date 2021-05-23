import cv2 as cv

if __name__ == "__main__":
    # read and display an image at each 3 seconds
    for i in range(1, 15):
        img = cv.imread('../../assets/test%d.jpg' %i)
        cv.imshow('Tests Preview', img)
        cv.waitKey(3000)


    cv.destroyAllWindows()

# some pictures may not be seen completely because of their scale!
# we will fix this later in "image scaling" section.
# also these are the 15 sample pictures we use in this tutorial.