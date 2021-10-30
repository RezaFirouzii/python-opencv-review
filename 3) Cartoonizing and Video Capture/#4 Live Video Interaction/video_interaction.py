import cv2 as cv
import numpy as np


DRAG = False
x_init, y_init = (-1, -1)


def update_rect(params, x, y):
    global x_init, y_init
    params["top_left"]     = (min(x_init, x), min(y_init, y))
    params["bottom_right"] = (max(x_init, x), max(y_init, y))


def draw_rect(event, x, y, flags, params):
    global DRAG, x_init, y_init

    if event == cv.EVENT_LBUTTONDOWN:
        DRAG = True
        x_init, y_init = x, y

    elif event == cv.EVENT_MOUSEMOVE and DRAG:
        update_rect(params, x, y)

    elif event == cv.EVENT_LBUTTONUP:
        DRAG = False
        update_rect(params, x, y)


if __name__ == "__main__":
    event_params = {
        "top_left": (x_init, y_init),
        "bottom_right": (x_init, y_init)
    }

    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    if not cap.isOpened():
        raise IOError("Webcam/Video could not be opened!")

    cv.namedWindow("Live Video Interaction")
    cv.setMouseCallback("Live Video Interaction", draw_rect, event_params)

    while True:
        res, frame = cap.read()
        if not res:
            break

        (x1, y1), (x2, y2) = event_params["top_left"], event_params["bottom_right"]
        frame[y1: y2, x1: x2] = 255 - frame[y1: y2, x1: x2]
        
        cv.imshow("Live Video Interaction", frame)

        key = cv.waitKey(20)
        if key == 27:
            break

    cap.release()
    cv.destroyAllWindows()
