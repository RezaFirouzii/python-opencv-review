import cv2 as cv
import numpy as np


if __name__ == "__main__":
    img = cv.imread('../../assets/test11.jpg')
    cv.imshow('Original Image', img)
    size = 9    # all kernel matrices will be 9x9

    # horizontal motion blur kernel matrix
    h_kernel = np.zeros((size, size))
    h_kernel[size // 2, :] = np.ones(size)    # assigning 1 to middle row
    h_kernel /= size                          # normalizing the kernel
    # applying above kernel to image
    motion_blur = cv.filter2D(img, -1, h_kernel)
    cv.imshow('Horizontal Motion Blur', motion_blur)


    # vertical motion blur kernel matrix
    v_kernel = np.zeros((size, size))
    v_kernel[:, size // 2] = np.ones(size)    # assigning 1 to middle column
    v_kernel /= size
    motion_blur = cv.filter2D(img, -1, v_kernel)
    cv.imshow('Vertical Motion Blur', motion_blur)


    # diagonal motion blur kernel matrix
    d_kernel = np.zeros((size, size))
    index_list = np.arange(size)              # [0, 1, ... , 8]
    d_kernel[index_list, index_list] = 1      # assigning 1 to digonal values (top-left to bottom-right)
    d_kernel /= size
    # applying the kernel to image
    motion_blur = cv.filter2D(img, -1, d_kernel)
    cv.imshow('Diagonal Motion Blur', motion_blur)

    print(h_kernel, end='\n\n')
    print(v_kernel, end='\n\n')
    print(d_kernel)

    cv.waitKey(0)
    cv.destroyAllWindows()

# for better understanding about the kernels,
# set the size to 5 and run, the look at the
# terminal to see how are the matrices.

# size of kernel ∝ size of blurrines