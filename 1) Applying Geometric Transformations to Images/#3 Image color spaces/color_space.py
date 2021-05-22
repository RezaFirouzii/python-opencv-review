import cv2 as cv

if __name__ == "__main__":
    
    img = cv.imread('../../assets/test2.jpg')
    cv.imshow("Original", img)

    # change color space using 'cv2.cvtColor'
    output = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow("RGB", output)

    output = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("GRAY", output)

    output = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow("HSV", output)
    
    output = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    cv.imshow("YUV", output)
    
    output = cv.cvtColor(img, cv.COLOR_BGR2LUV)
    cv.imshow("LUV", output)

    cv.waitKey(0)
    cv.destroyAllWindows()

# run and compare different images for better understanding
# these are the most important color spaces we might come across
