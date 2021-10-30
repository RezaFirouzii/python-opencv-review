# press any numeric key on your keyboard including [0 to 9]
# to change the color space of your stream and current frame!

import cv2 as cv


if __name__ == "__main__":
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)

    if not cap.isOpened():
        raise IOError("Webcam could not be opened!\nTry a static video instead.")

    options = {
        0: None,    # reset
        1: cv.COLOR_BGR2GRAY,
        2: cv.COLOR_BGR2HSV,
        3: cv.COLOR_BGR2YUV,
        4: cv.COLOR_BGR2RGB,
        5: cv.COLOR_BGR2LUV,
        6: cv.COLOR_BGR2XYZ,
        7: cv.COLOR_BGR2HLS,
        8: cv.COLOR_BGR2LAB,
        9: cv.COLOR_BGR2YCrCb
    }

    current_mode = 0
    while True:
        res, frame = cap.read()
        if not res:
            break

        # frame = cv.resize(frame, None, fx=.5, fy=.5)

        key = cv.waitKey(20)
        if key == 27:
            break

        key -= 48   # ascii code of key - ascii of '0'
        if key in options.keys():
            current_mode = key

        if current_mode:
            frame = cv.cvtColor(frame, options[current_mode])

        cv.imshow('Webcam', frame)
        
    cap.release()
    cv.destroyAllWindows()
