import cv2

RED = (0, 0, 255)

if __name__ == "__main__":
    img = cv2.imread('../../assets/test4.jpg')
    img = cv2.resize(img, None, fx=.5, fy=.5)
    cv2.imshow("Original Image", img)

    mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'Nariz.xml')
    if mouth_cascade.empty():
        raise IOError("Unable to load the mouth cascade classifier file!")

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mouth_rects = mouth_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=3)

    for (x, y, w, h) in mouth_rects:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), RED, 2)

    cv2.imshow("Mouth detector", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
