import cv2 as cv


if __name__ == "__main__":
    
    img = cv.imread("../assets/test2.jpg")
    height, width = img.shape[:2]

    # rotating img 45 deg with rotation point equal to center of img
    rotation_matrix = cv.getRotationMatrix2D((width // 2, height // 2), 45, 1)
    output = cv.warpAffine(img, rotation_matrix, (width, height))
    cv.imshow("1) 45 deg rotation", output)

    # rotating img 90 deg with rotation point equal to center of img
    rotation_matrix = cv.getRotationMatrix2D((width // 2, height // 2), 90, 1)
    output = cv.warpAffine(img, rotation_matrix, (width, height))
    cv.imshow("2) 90 deg rotation", output)

    # rotating img 180 deg with rotation point equal to center of img
    rotation_matrix = cv.getRotationMatrix2D((width // 2, height // 2), 180, 1)
    output = cv.warpAffine(img, rotation_matrix, (width, height))
    cv.imshow("3) 180 deg rotation", output)

    # rotating img 300 deg with rotation point equal to center of img
    rotation_matrix = cv.getRotationMatrix2D((width // 2, height // 2), 300, 1)
    output = cv.warpAffine(img, rotation_matrix, (width, height))
    cv.imshow("4) 300 deg rotation", output)

    # rotating img 90 deg with rotation point equal to center of img
    rotation_matrix = cv.getRotationMatrix2D((width // 2, height // 2), -90, 1)
    output = cv.warpAffine(img, rotation_matrix, (width, height))
    cv.imshow("5) -90 deg rotation", output)

    # rotating img -135 deg with rotation point equal to center of img
    rotation_matrix = cv.getRotationMatrix2D((width // 2, height // 2), -135, 1)
    output = cv.warpAffine(img, rotation_matrix, (width, height))
    cv.imshow("6) -135 deg rotation", output)

    cv.waitKey(0)
    cv.destroyAllWindows()


# hint
# rotations are counter clockwise unless the degree value is negative
# 90 degree counter clockwise == -270 degree clockwise 