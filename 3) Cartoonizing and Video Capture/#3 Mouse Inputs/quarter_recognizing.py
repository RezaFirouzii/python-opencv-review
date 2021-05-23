# captcha simulation / bot recognizing simulation
# asking user to select the quarter with no face in
# a tiny project with use of mouse handling in opencv

import cv2 as cv
import numpy as np


GREEN = (0, 153, 0)
RED = (0, 0, 255)
TARGET = None       # number of the quarter with no face
DETECTED = -1       # -1: not chosen, 0: wrong choice, 1: correct


def draw_quarter(q, sample, img):

    row = q // 2
    col = q % 2

    x_range = slice(row * height // 2, (row + 1) * height // 2)
    y_range = slice(col * width  // 2, (col + 1) * width  // 2)

    quadrant = cv.imread('../../assets/test%d.jpg'%sample)
    quadrant = cv.resize(quadrant, (width // 2, height // 2))
    img[x_range, y_range] = quadrant



def draw_image(img):
    global TARGET
    TESTS_COUNT = 8                     # number of sample images containing face
    tests = np.arange(TESTS_COUNT) + 1  # first 8 images are faces (look at assets folder)

    # image quarters numbers
    # [0 | 1]
    # [2 | 3]
    quarters = np.arange(4)     # quarters numbers: [0, 1, 2, 3]
    
    # assigning 3 random "face images" to 3 random quarters
    for _ in range(3):
        sample = np.random.choice(tests)   # random item from samples numbers array
        index = np.where(tests == sample)  # index of the random value
        tests = np.delete(tests, index)

        q = np.random.choice(quarters)
        index = np.where(quarters == q)
        quarters = np.delete(quarters, index)

        draw_quarter(q, sample, img)


    # placing the main image with no face
    TARGET = quarters[0]                    # only one spot left
    target_pic = np.random.randint(9, 15)   # images 9 to 14 are pictures without face (test9.jpg , ... , test14.jpg)
    draw_quarter(TARGET, target_pic, img)   # passing a random picture out of 6 pictures which could be the target



def detect_quadrant(event, x, y, flags, param):
    global DETECTED
    top_left = None
    selected_quadrant = None

    if event == cv.EVENT_LBUTTONDOWN:
    
        if x > width / 2:
            if y > height / 2:  # bottom right quarter
                top_left = (width // 2, height // 2)
                selected_quadrant = 3
            else:               # top right quarter
                top_left = (width // 2, 0)
                selected_quadrant = 1

        else:
            if y > height / 2:  # bottom left quarter
                top_left = (0, height // 2)
                selected_quadrant = 2
            else:               # top left quarter
                top_left = (0, 0)
                selected_quadrant = 0
                
        img = param["img"]
        if top_left:
            x, y = top_left
            
            if TARGET == selected_quadrant:     # drawing a "✓" on target
                point1 = (x + 50, y + height // 4)
                point2 = (x + width // 4 - 50, y + height // 2 - 50)
                point3 = (x + width // 2 - 50, y + 50)

                img = cv.line(img, point1, point2, GREEN, 10)
                img = cv.line(img, point2, point3, GREEN, 10)

                DETECTED = 1

            else:                               # drawing a "X" on selected quadrant
                bottom_left  = x, y + height // 2
                top_right    = x + width // 2, y
                bottom_right = x + width // 2, y + height // 2

                original_copy = img.copy()
                img = cv.line(img, top_left, bottom_right, RED, 10)
                img = cv.line(img, top_right, bottom_left, RED, 10)

                DETECTED = 0


if __name__ == "__main__":

    width, height = 750, 600    # img size
    img = np.zeros((height, width, 3), np.uint8)
    title = 'Which image does NOT contain any face ?'

    cv.namedWindow(title)
    cv.setMouseCallback(title, detect_quadrant, {"img": img})
    
    draw_image(img)
    original_copy = img.copy()
    
    while True:

        key = cv.waitKey(1)
        if key == 27:
            break
                    
        cv.imshow(title, img)

        if DETECTED == 1:
            cv.waitKey(1000)
            draw_image(img)
            original_copy = img.copy()
            DETECTED = -1

        elif not DETECTED:
            cv.waitKey(1000)
            img[:] = original_copy[:]
            DETECTED = -1

    cv.destroyAllWindows()

# you can customize this project with more images