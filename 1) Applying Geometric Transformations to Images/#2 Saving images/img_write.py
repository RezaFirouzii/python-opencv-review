import cv2 as cv

if __name__ == "__main__":
    
    img = cv.imread('../../assets/test1.jpg')

    # save
    cv.imwrite('test1_copy.jpg', img)

    # optional format methods
    cv.imwrite('test1_png_compression.jpg', img, [cv.IMWRITE_PNG_COMPRESSION])
    cv.imwrite('test1_webp_quality.jpg', img, [cv.IMWRITE_WEBP_QUALITY])
    cv.imwrite('test1_jpg_luma_quality.jpg', img, [cv.IMWRITE_JPEG_LUMA_QUALITY])
