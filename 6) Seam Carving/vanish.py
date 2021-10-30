# using seam carving we'll be removing an object completely
# from an image like it never existed and has totally vanished!

import cv2 as cv
import seamcarving


DRAG = False
x_init, y_init = (-1, -1)
GREEN = (0, 255, 0)


# modifying the energy_matrix to be totally uninteresting on selected region
def modify_energies(img, rect_roi):
    energies = seamcarving.create_energy_matrix(img)
    x, y, w, h = rect_roi
    energies[x: x + w, y: y + h] = 0
    return energies

# remove the object from the input region of interest
# def remove_object(img, rect_roi):
#     # number of seams must be greater than or equal to rect_roi width to cover the region
#     seams_num = rect_roi[2]

#     # start a loop and remove one seam at a time
#     for i in range(seams_num):
#         x, y, w, h = rect_roi
#         energy_matrix = modify_energies(img, (x, y, w - i, h))
#         # find the vertical seam that could be removed
#         seam = seamcarving.find_vertical_seam(img, energy_matrix)
#         # remove the seam
#         img = seamcarving.remove_vertical_seam(img, seam)
#         # print('Number of seams removed =', i+1)

#     output = img.copy()
#     # filling up the region with surrounding values so the image size remains unchanged
#     for i in range(seams_num):
#         energy_matrix = seamcarving.create_energy_matrix(img)
#         seam = seamcarving.find_vertical_seam(img, energy_matrix)
#         # expanding img
#         img = seamcarving.remove_vertical_seam(img, seam)
#         output = seamcarving.add_vertical_seam(output, seam)
#         print('Number of seams added =', i+1)


#     cv.imshow("Vanishing Object", output)
#     cv.waitKey()

# Remove the object from the input region of interest
def remove_object(img, rect_roi):
    img = img_original.copy()
    num_seams = rect_roi[2] + 5
    energy = modify_energies(img, rect_roi)
    # Start a loop and rsemove one seam at a time
    for i in range(num_seams):
        # Find the vertical seam that can be removed
        seam = seamcarving.find_vertical_seam(img, energy)
        # Remove that vertical seam
        img = seamcarving.draw_vertical_seam(img, seam)    
        cv.imshow('Output', img)
        cv.waitKey()
        img = seamcarving.remove_vertical_seam(img, seam)
        x,y,w,h = rect_roi
        # Compute energy matrix after removing the seam
        energy = modify_energies(img, (x,y,w - i,h))
        print('Number of seams removed =', i+1, img.shape)
    img_output = img.copy()
    # Fill up the region with surrounding values so that the size
    # of the image remains unchanged
    for i in range(num_seams):
        seam = seamcarving.find_vertical_seam(img, energy)
        img = seamcarving.remove_vertical_seam(img, seam)
        img_output = seamcarving.add_vertical_seam(img_output, seam)

        energy = seamcarving.create_energy_matrix(img)
        print('Number of seams added =', i+1)
    cv.imshow('Output', img_output)
    cv.waitKey()




def update_rect(params, x, y):
    global x_init, y_init
    params["top_left"]     = (min(x_init, x), min(y_init, y))
    params["bottom_right"] = (max(x_init, x), max(y_init, y))

    (x1, y1), (x2, y2) = params["top_left"], params["bottom_right"]
    img[y1: y2, x1: x2] = 255 - img_original[y1: y2, x1: x2]


def mouse_handler(event, x, y, flags, params):
    global img, x_init, y_init, DRAG

    if event == cv.EVENT_LBUTTONDOWN:
        DRAG = True
        x_init, y_init = x, y
        img = img_original.copy()

    elif event == cv.EVENT_MOUSEMOVE and DRAG:
        update_rect(params, x, y)

    elif event == cv.EVENT_LBUTTONUP:
        DRAG = False
        update_rect(params, x, y)

        # creating a rectangle out of selected region
        rect_roi = (x_init, y_init, abs(x - x_init), abs(y - y_init))
        remove_object(img, rect_roi)


if __name__ == "__main__":
    img = cv.imread('../assets/test9.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)
    img_original = img.copy()
    
    event_params = {
        "top_left": (x_init, y_init),
        "bottom_right": (x_init, y_init)
    }
    cv.namedWindow('Vanishing Object')
    cv.setMouseCallback("Vanishing Object", mouse_handler, event_params)

    while True:        
        cv.imshow("Vanishing Object", img)
        if cv.waitKey(10) == 27: # ESC key
            break

    cv.destroyAllWindows()