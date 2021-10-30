from seamcarving import *
import cv2
import numpy as np
# Draw rectangle on top of the input image
def draw_rectangle(event, x, y, flags, params):
 global x_init, y_init, drawing, top_left_pt, bottom_right_pt, img_orig
 # Detecting a mouse click
 if event == cv2.EVENT_LBUTTONDOWN:
    drawing = True
    x_init, y_init = x, y
 # Detecting mouse movement
 elif event == cv2.EVENT_MOUSEMOVE:
    if drawing:
        top_left_pt, bottom_right_pt = (x_init,y_init), (x,y)
        img[y_init:y, x_init:x] = 255 - img_orig[y_init:y, x_init:x]
        cv2.rectangle(img, top_left_pt, bottom_right_pt, (0,255,0), 2)
    # Detecting the mouse button up event
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        top_left_pt, bottom_right_pt = (x_init,y_init), (x,y)
        img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]
        # Draw rectangle around the selected region
        cv2.rectangle(img, top_left_pt, bottom_right_pt, (0,255,0), 2)
        rect_final = (x_init, y_init, x-x_init, y-y_init)
        # Remove the object in the selected region
        remove_object(img_orig, rect_final)
# Computing the energy matrix using modified algorithm
def compute_energy_matrix_modified(img, rect_roi):
 # Compute weighted summation i.e. 0.5*X + 0.5*Y
 energy_matrix = create_energy_matrix(img)
 x,y,w,h = rect_roi
 # We want the seams to pass through this region, so make sure the
 energy_matrix[y:y+h, x:x+w] = 0
 return energy_matrix
# Remove the object from the input region of interest
def remove_object(img, rect_roi):
 num_seams = rect_roi[2] + 10
 energy = compute_energy_matrix_modified(img, rect_roi)
 # Start a loop and rsemove one seam at a time
 for i in range(num_seams):
    # Find the vertical seam that can be removed
    seam = find_vertical_seam(img, energy)
    # Remove that vertical seam
    img = remove_vertical_seam(img, seam)
    x,y,w,h = rect_roi
    # Compute energy matrix after removing the seam
    energy = compute_energy_matrix_modified(img, (x,y,w-i,h))
    print('Number of seams removed =', i+1)
 img_output = np.copy(img)
 # Fill up the region with surrounding values so that the size
 # of the image remains unchanged
 for i in range(num_seams):
    seam = find_vertical_seam(img, energy)
    img = remove_vertical_seam(img, seam)
    img_output = add_vertical_seam(img_output, seam)
    energy = create_energy_matrix(img)
    print('Number of seams added =', i+1)
 cv2.imshow('Input', img_input)
 cv2.imshow('Output', img_output)
 cv2.waitKey()
if __name__=='__main__':
 img_input = cv2.imread('../assets/test1.jpg')
 drawing = False
 img = np.copy(img_input)
 img_orig = np.copy(img_input)
 cv2.namedWindow('Input')
 cv2.setMouseCallback('Input', draw_rectangle)
 print('Draw a rectangle with the mouse over the object to be removed')
 while True:
    cv2.imshow('Input', img)
    c = cv2.waitKey(10)
    if c == 27:
        break
 cv2.destroyAllWindows()
