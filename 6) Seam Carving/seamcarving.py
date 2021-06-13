# all seam carving helper functions
# this file will be used as a custom module

import cv2 as cv
import numpy as np


def draw_vertical_seam(img, seam):
    img_seam = img.copy()

    # extracting the points from the seam
    points = [(index, int(item)) for index, item in enumerate(seam)]
    x_coords, y_coords = np.transpose(points)

    # drawing the lines on img
    img_seam[x_coords, y_coords] = (0, 255, 0)
    return img_seam


def draw_horizontal_seam(img, seam):
    img_seam = img.copy()

    # extracting coordinates
    coords = [(y, int(x)) for y, x in enumerate(seam)]
    y_coords, x_coords = np.transpose(coords)

    # drawing horizontal lines on img
    img_seam[x_coords, y_coords] = (0, 255, 0)
    return img_seam


def create_energy_matrix(img):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # computing x deriative of img
    sobel_x = cv.Sobel(gray_img, cv.CV_64F, 1, 0, ksize=3)
    # computing y deriative of img
    sobel_y = cv.Sobel(gray_img, cv.CV_64F, 0, 1, ksize=3)

    sobel_x = cv.convertScaleAbs(sobel_x)
    sobel_y = cv.convertScaleAbs(sobel_y)

    # energy matrix which is weighted sum of 2 imgs
    energy_matrix = cv.addWeighted(sobel_x, .5, sobel_y, .5, 0)
    return energy_matrix


def find_vertical_seam(img, energy_matrix):
    rows, cols = img.shape[:2]

    # filling the seam vector with zeros
    # we store indecies of minimum values along x-axis in seam
    seam = np.zeros(rows)

    # initializing distance and edge marices
    distance = np.full((rows, cols), float("inf")) # filling the matrix with "infinity"
    distance[0, :] = np.zeros(cols)                # filling the first row of distance matrix with zeros

    # keeps track of the index (index difference)
    # of minimum parent out of last 3 parents at previous row
    min_parent = np.zeros((rows, cols))

    # using dynamic programming, we calculate distances and
    # min parent of each pixel with the help of our energy matrix
    for i in range(rows - 1):           # loop through all rows except the last one to prevent overflow
        for j in range(1, cols - 1):    # loop through all columns except the first and last column due to underflow and overflow
            
            # bottom left
            if  distance[i + 1, j - 1] > distance[i, j] + energy_matrix[i + 1, j - 1]:
                distance[i + 1, j - 1] = distance[i, j] + energy_matrix[i + 1, j - 1]
                min_parent[i + 1, j - 1] = 1    # we have came from a parent with less energy which is on right side

            # bottom center
            if  distance[i + 1, j] > distance[i, j] + energy_matrix[i + 1, j]:
                distance[i + 1, j] = distance[i, j] + energy_matrix[i + 1, j]
                min_parent[i + 1, j] = 0        # last parent we have come from is exactly above (same column, above row)

            # bottom right
            if  distance[i + 1, j + 1] > distance[i, j] + energy_matrix[i + 1, j + 1]:
                distance[i + 1, j + 1] = distance[i, j] + energy_matrix[i + 1, j + 1]
                min_parent[i + 1, j + 1] = -1   # a parent with less energy on left side (left column, above row)

    # tracking the path from the last row all the way up to first row
    # we detect the minimum parent in each row as we come up and simply
    # store its index in seam matrix, starting with minimum value of the last row
    seam[rows - 1] = np.argmin(distance[rows - 1, :])   # last element of seam
    
    # note that the first row is not included since we assign previous row each time
    for i in range(rows - 1, 0, -1):
        seam[i - 1] = seam[i] + min_parent[i, int(seam[i])]
    
    return seam


# same as above method but from left to right
def find_horizontal_seam(img, energy_matrix):
    rows, cols = img.shape[:2]

    # store indecies of minimum values along y-axis in seam
    seam = np.zeros(cols)

    distance = np.full((rows, cols), float("inf"))
    distance[:, 0] = np.zeros(rows)     # filling the first column of distance matrix with zeros

    # stores index difference of minimum parent out of 3 in previous column
    min_parent = np.zeros((rows, cols))

    for j in range(cols - 1):           # loop through all columns except the last column due to overflow
        for i in range(1, rows - 1):    # loop through all rows except the first and last one to prevent both underflow & overflow

            # above right
            if  distance[i - 1, j + 1] > distance[i, j] + energy_matrix[i - 1, j + 1]:
                distance[i - 1, j + 1] = distance[i, j] + energy_matrix[i - 1, j + 1]
                min_parent[i - 1, j + 1] = 1          # we have came from a parent with less energy which is underneath
            
            # center right
            if  distance[i, j + 1] > distance[i, j] + energy_matrix[i, j + 1]:
                distance[i, j + 1] = distance[i, j] + energy_matrix[i, j + 1]
                min_parent[i, j + 1] = 0              # last parent we have come from is in the same row

            # bottom right
            if  distance[i + 1, j + 1] > distance[i, j] + energy_matrix[i + 1, j + 1]:
                distance[i + 1, j + 1] = distance[i, j] + energy_matrix[i + 1, j + 1]
                min_parent[i + 1, j + 1] = -1         # a parent with less energy which is in the above row


    # tracking the path from the last column to the very first one
    # we detect the minimum parent in each column as we travel along side x-axis from right to left
    # storing its index in seam, starting with the minimum value of the last column
    seam[cols - 1] = np.argmin(distance[:, cols - 1])   # last element of seam
    
    # note that the first column is not included since we assign previous column each time
    for j in range(cols - 1, 0, -1):
        seam[j - 1] = seam[j] + min_parent[int(seam[j]), j]
    
    return seam



# deleting the vertical seam and reducing the width
def remove_vertical_seam(img, seam):
    rows, cols = img.shape[:2]

    # assign each pixel to its left column to remove the seam
    for i in range(rows):
        for j in range(int(seam[i]), cols - 1):
            img[i, j] = img[i, j + 1]

    # crop last column
    img = img[:, :cols - 1]
    return img



# deleting the horizontal seam and reducing the height
def remove_horizontal_seam(img, seam):
    rows, cols = img.shape[:2]

    # assign each pixel to its above row element to remove the seam
    for j in range(cols):
        for i in range(int(seam[j]), rows - 1):
            img[i, j] = img[i + 1, j]

    # crop last row
    img = img[:rows - 1, :]
    return img




if __name__ == "__main__":
    img = cv.imread('../assets/test10.jpg')
    img = cv.resize(img, None, fx=.5, fy=.5)
    print(img.shape)
    energy_matrix = create_energy_matrix(img)
    seam = find_horizontal_seam(img, energy_matrix)
    img = draw_horizontal_seam(img, seam)
    img = remove_horizontal_seam(img, seam)
    cv.imshow("", img)
    print(img.shape)
    cv.waitKey(0)
    cv.destroyAllWindows()

