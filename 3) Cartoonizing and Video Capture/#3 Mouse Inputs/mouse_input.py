# handling mouse events with opencv

import cv2 as cv


GREEN = (0, 153, 0)


def mouse_handler(event, x, y, flags, param):
    img = param["img"]

    if event == cv.EVENT_LBUTTONDOWN:                   # left button click
        img = cv.circle(img, (x, y), 25, GREEN, -1)     # drawing a filled circle with 25 pixels radius at the mouse position
    elif event == cv.EVENT_RBUTTONDOWN:                 # right button clicked
        img[:] = original_copy[:]                       # clear the circles


if __name__ == "__main__":
    
    img = cv.imread('../../assets/test1.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)
    original_copy = img.copy()  # a copy of img to clear later

    cv.namedWindow("Mouse Input Detection")
    cv.setMouseCallback("Mouse Input Detection", mouse_handler, {"img": img})
    
    while True:
        cv.imshow("Mouse Input Detection", img)
    
        key = cv.waitKey(1)
        if key == 27:
            break
            
    cv.destroyAllWindows()
