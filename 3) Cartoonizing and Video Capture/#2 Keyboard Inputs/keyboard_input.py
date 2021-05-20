import cv2 as cv


if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    current_mode = 0

    options = {
        1: cv.COLOR_BGR2GRAY,
        2: cv.COLOR_BGR2HSV,
        3: cv.COLOR_BGR2YUV,
        4: cv.COLOR_BGR2RGB
    }

    while True:
        res, frame = cap.read()
        frame = cv.resize(frame, None, fx=.5, fy=.5)

        key = cv.waitKey(1)
        if key == 27:
            break

        if 48 <= current_mode <= 55:
            current_mode = key

        if 48 <= key <= 55:
            frame = options[key]

        cv.imshow('Webcam', frame)
        
    cap.release()
    cv.destroyAllWindows()

