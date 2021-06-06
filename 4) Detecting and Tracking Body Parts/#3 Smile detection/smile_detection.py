import cv2

BLUE = (255, 0, 0)

if __name__ == "__main__":

    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    if smile_cascade.empty():
        raise IOError("Unable to load the left-ear cascade classifier xml file!")

    cap = cv2.VideoCapture('../../yellow.mp4')
    if not cap.isOpened():
        raise IOError("Webcam could not be opened!")

    while True:
        res, frame = cap.read()

        if not res:
            break

        frame = cv2.resize(frame, None, fx=.5, fy=.5)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        smile_rects = smile_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=30)
        for (x, y, w, h) in smile_rects:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), BLUE, 2)

        cv2.imshow("Smile Detector", frame)
        if cv2.waitKey(1) == 27:    # ESC key
            break

    cv2.destroyAllWindows()

# whenever you smile, it's gonna be detected :)