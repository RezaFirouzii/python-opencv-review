# let's edit our webcam video stream and have some fun!
# we'll devide each frame to 4 quadrants and rotate
# each part clockwise every one second
# every part has different look and effects

import cv2 as cv
import numpy as np
from collections import deque

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 128, 255)


if __name__ == "__main__":
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Webcam could not be opened!")

    count = 0
    while True:
        res, frame = cap.read()
        if not res:
            break
        
        frame = cv.resize(frame, None, fx=.5, fy=.5)
        height, width = frame.shape[:2]

        img = frame.copy()
        frame = cv.resize(frame, None, fx=.5, fy=.5)
        
        part1 = frame.copy()                            # original
        part2 = cv.Laplacian(frame, cv.CV_64F)          # edge detection filter

        part3 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)   # grayscale effect
        part3 = np.stack((part3, ) * 3, axis=-1)        # converting to 3 channel matrix
        
        part4 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)    # HSV color space

        # every 100 milli seconds shift the deque for a new rotation
        parts = deque([part1, part2, part3, part4])
        parts.rotate(count // 100)

        # assigning each quadrant based on clockwise rotation
        img[:height // 2, :width // 2] = parts[0]   # top left
        img[:height // 2, width // 2:] = parts[1]   # top right
        img[height // 2:, width // 2:] = parts[2]   # bottom right
        img[height // 2:, :width // 2] = parts[3]   # bottom left

        cv.imshow('Video Capture', img)

        key = cv.waitKey(1)
        if key == 27: # ESC key
            break

        count += 1         # every 100 times looping 1 shift
        count %= 400       # count %= len(parts) * 100

    cap.release()
    cv.destroyAllWindows()
