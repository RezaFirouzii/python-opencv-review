import cv2 as cv


def put_on_sunglasses(img):
    layer = cv.imread('sunglasses.jpg')

    face_rects = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in face_rects:
        h = 4 * h // 7  # AKA  h // 1.75 (testing distance by chance)
        imgROI = img[y: y + h, x: x + w]    # extracting the face part (Region of Interest)
        layer = cv.resize(layer, (w, h))    # resizing the layer to same shape as face part

        # thresholding the layer to filter out glasses positive (white pixels)
        # and the rest of the layer false (black pixels)
        gray_layer = cv.cvtColor(layer, cv.COLOR_BGR2GRAY)
        res, mask = cv.threshold(gray_layer, 230, 255, cv.THRESH_BINARY_INV)
        new_face = cv.bitwise_and(layer, layer, mask=mask)          # filtering out only sunglasses
        
        # combination
        img[y: y + h, x: x + w] = cv.add(imgROI, new_face)          # combining the new face with the modified img

    return img


# same logic as above method but different positioning
def put_on_mask(img):
    layer = cv.imread('mask.jpg')

    face_rects = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in face_rects:
        y += h // 4 + 9     # test different numbers untill the closest result
        imgROI = img[y: y + h, x: x + w]    # extracting the face part (Region of Interest)
        layer = cv.resize(layer, (w, h))    # resizing the layer to same shape as face part
        
        # thresholding the layer to filter out health-mask positive (white pixels)
        # and the rest of the layer false (black pixels)
        gray_layer = cv.cvtColor(layer, cv.COLOR_BGR2GRAY)
        res, mask = cv.threshold(gray_layer, 227, 255, cv.THRESH_BINARY_INV)
        mask = cv.medianBlur(mask, 5)       # removing little noise of black dots
        mask_inv = cv.bitwise_not(mask)     # mask inverse helps us create a transparent gap for health-mask in combination

        new_face = cv.bitwise_and(layer, layer, mask=mask)      # filtering out only health-mask
        gap_img = cv.bitwise_and(imgROI, imgROI, mask=mask_inv) # filtering out everything except health-mask

        # combination
        img[y: y + h, x: x + w] = cv.add(new_face, gap_img)     # combining the new face with the modified img

    return img
        


if __name__ == "__main__":
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    if face_cascade.empty():
        raise IOError("Unable to load the face cascade classifier XML file.")

    img = cv.imread('../../assets/test2.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)
    original = img.copy()

    img = put_on_mask(img)
    img = put_on_sunglasses(img)

    cv.imshow("Original Image", original)
    cv.imshow("Face with Glasses and Mask", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

# hint:
#   - some number parameters used in methods such as
#   thresholding or "h" variable assignments in loops
#   might seem unknown... these numbers are calculated
#   just base on guesses and tests.
#   
#   - as an excercise try to implement the same project,
#   this time on a live webcam video stream!