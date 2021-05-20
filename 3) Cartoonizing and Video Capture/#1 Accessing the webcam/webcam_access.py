import cv2 as cv

if __name__ == "__main__":
    
    # 0 => first (default) webcam connected,
    # 1 => second webcam and so on.
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Webcam could not be opened!")

    while True:
        
        res, frame = cap.read()     # returns (bool, ndarray)

        # in case any error occurs
        if not res:
            break

        frame = cv.resize(frame, None, fx=.5, fy=.5)
        cv.imshow("Video Stream", frame)

        keyboardInput = cv.waitKey(1)
        if keyboardInput == 27:     # ESC button ascii code
            break

    cap.release()
    cv.destroyAllWindows()

# you can also replace a normal video with webcam
# in video capture object, just give it the address of
# the video instead of 0 or number of your webcam
