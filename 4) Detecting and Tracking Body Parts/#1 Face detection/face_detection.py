import cv2 as cv

RED = (0, 0, 255)

if __name__ == "__main__":
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    cap = cv.VideoCapture('../../yellow.mp4')
    if not cap.isOpened():
        raise IOError("Webcam was not opened!")

    while True:
        res, frame = cap.read()
        if not res:
            break

        frame = cv.resize(frame, None, fx=.5, fy=.5)
        face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)
        for (x, y, w, h) in face_rects:
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), RED, 3)

        cv.imshow("Face Detected Frame", frame)
        
        if cv.waitKey(1) == 27:
            break

    cv.destroyAllWindows()