import cv2 as cv

if __name__ == "__main__":
    # reading the image
    img = cv.imread('../../assets/test2.jpg')

    # displaying the image
    cv.imshow('Fox', img)

    # wait untill any key is pressed
    cv.waitKey(0)
    cv.destroyAllWindows()
