import cv2 as cv
from math import sqrt

GREEN = (0, 153, 0)

if __name__ == "__main__":
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    cap = cv.VideoCapture('yellow.mp4')
    scale_factor = 0.3
    while True:
        res, frame = cap.read()
        if not res:
            break
        frame = cv.resize(frame, None, fx=scale_factor, fy=scale_factor)
        face_rects, n = face_cascade.detectMultiScale2(frame, scaleFactor=1.3, minNeighbors=3)
        print(n)
        for (x, y, w, h) in face_rects:
            frame = cv.circle(frame, (x + w // 2, y + h // 2), int(w // sqrt(2)), GREEN, 3)

        cv.imshow('Detected', frame)

        key = cv.waitKey(20)
        if key == 27:
            break

    cap.release()
    # for _ in range(15):
    #     img = cv.imread('assets/test%d.jpg'%(_+1))
    #     img = cv.resize(img, None, fx=.5, fy=.5)
    #     face_rects = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=3)
    #     for (x, y, w, h) in face_rects:
    #         img = cv.rectangle(img, (x, y), (x + w, y + h), GREEN, 3)

    #     cv.imshow('Detected', img)
    #     cv.waitKey(0)
    cv.destroyAllWindows()