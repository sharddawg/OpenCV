import cv2
# import numpy as np


# we define this function to find contours.
# img1 is the canny image of the original image and img2 is the image we'll draw on.
def get_contours(img1, img2):
    # cv2.RETR_EXTERNAL returns the outer most contours.
    contours, hierarchy = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        # We find the area of the contours.
        area = cv2.contourArea(contour)
        # if the area of the contours is less than what we want then we don't draw the contours on out desired image.
        # this is useful if the cv2.findContours function detects noise in the image.
        if area > 500:
            print(area)
            # -1 argument means we'll draw ON img2.
            cv2.drawContours(img2, contour, -1, (255, 0, 0), 2)
            # we find the perimeters of the shapes.
            # True means the shapes or contours are closed
            perimeter = cv2.arcLength(contour, True)
            # cv2.approxPolyDP returns a matrix.
            # The number of rows in the matrix means the number of vertices or corner points of the shape.
            # The second parameter is related to accuracy. 0.02 * perimeter means 0.2% of the arc length (perimeter).
            # True means the contour is closed
            vertices = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            # printing vertices would give us the matrix.
            # len(vertices) gives us the number of vertices or corner points.
            print(len(vertices))
            object_corners = len(vertices)
            # cv2.boundingRect gives us the x, y, width and height of the box bounding the objects.
            x, y, w, h = cv2.boundingRect(vertices)
            if object_corners == 3:
                object_type = "Triangle"
            elif object_corners == 4:
                aspect_ratio = w / float(h)
                if 0.95 < aspect_ratio < 1.05:
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif object_corners > 4:
                object_type = "Circle or sum"
            else:
                object_type = "Dunno"
            # We draw rectangles using cv2.rectangle and coordinates x, y, w, h
            cv2.rectangle(img_contours, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # we put text near the middle.
            cv2.putText(img_contours, object_type, (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_ITALIC, 0.4,
                        (0, 0, 0), 1)


img = cv2.imread('Images/shapes.png')
img_contours = img.copy()
img_grey = cv2.imread('Images/shapes.png', 0)
img_blur = cv2.GaussianBlur(img_grey, (7, 7), 0)
img_canny = cv2.Canny(img_grey, 200, 400)
get_contours(img_canny, img_contours)
cv2.imshow('img', img)
# cv2.imshow('grey', img_grey)
# cv2.imshow('blur', img_blur)
cv2.imshow('canny', img_canny)
cv2.imshow('contours', img_contours)
cv2.waitKey(0)
