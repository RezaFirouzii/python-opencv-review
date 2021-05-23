import cv2 as cv

if __name__ == "__main__":
    
    img = cv.imread('../../assets/test5.jpg')

    # save
    cv.imwrite('test5_copy.jpg', img)

    # optional format methods
    cv.imwrite('test5_png_compression.jpg', img, [cv.IMWRITE_PNG_COMPRESSION])
    cv.imwrite('test5_webp_quality.jpg', img, [cv.IMWRITE_WEBP_QUALITY])
    cv.imwrite('test5_jpg_luma_quality.jpg', img, [cv.IMWRITE_JPEG_LUMA_QUALITY])
