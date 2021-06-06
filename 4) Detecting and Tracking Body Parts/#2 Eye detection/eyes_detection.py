import cv2

GREEN = (0, 255, 0)

if __name__ == "__main__":
    img = cv2.imread('../../assets/test2.jpg')
    img = cv2.resize(img, None, fx=.5, fy=.5)
    cv2.imshow("Original Image", img)

    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    if eye_cascade.empty():
        raise IOError("Unable to load the eyes cascade classifier file.")

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # converting to grayscale for faster computation
    eyes_rects = eye_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in eyes_rects:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)  # drawing rectangle around each found eye

    cv2.imshow("Eye Detector", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# hint:
#   you could also detect faces first,
#   then try detecting the eyes in each face.
#   this way is much more efficient and faster

# as an excercise try impolementing the eye detection
# by face detection on your own.