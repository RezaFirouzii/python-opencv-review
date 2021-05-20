import cv2 as cv


if __name__ == "__main__":
    
    img = cv.imread('../assets/test1.jpg')
    cv.imshow("Original Image", img)

    # resizing the img to (500 pixels, 500 pixels)
    resized_img = cv.resize(img, (500, 500))
    cv.imshow("Image with Shape: (500, 500)", resized_img)

    # resizing the img dynamically to half, based on scale
    resized_img = cv.resize(img, None, fx=0.5, fy=0.5)  # this line == (width // 2, height // 2)
    cv.imshow("Resized to Half", resized_img)

    # resizing dynamically to an img 2 times bigger
    resized_img = cv.resize(img, None, fx=2, fy=2)
    cv.imshow("2 Times Bigger Img", resized_img)

    cv.waitKey(0)
    cv.destroyAllWindows()
 
 # hint
 # compare "Resize to Half" with "Original Image"
 