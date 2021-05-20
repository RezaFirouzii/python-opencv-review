import cv2 as cv

if __name__ == "__main__":
    # read and display an image at each 5 seconds
    for i in range(1, 6):
        img = cv.imread('../assets/test%d.jpg' %i)
        cv.imshow('Tests Preview', img)
        cv.waitKey(5000)


    cv.destroyAllWindows()

# some pictures may not be seen completely because of their scale!
# we will fix this later in "image scaling" section.
# also these are the test pictures we use in this tutorial.