import cv2
import numpy as np

# Read image
img = cv2.imread("Images/puppy.jpg")
# np.ones is used to make a matrix of all 1's of size (5,5).
# np.uint8 means we're defining the type of object (datatype)
kernel = np.ones((5, 5), np.uint8)
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# GaussianBlur is used to add blur to an image.
# (9,9) is an argument used to define how strong the blur is. It can only be odd numbers.
img_blur = cv2.GaussianBlur(img_grey, (99, 99), 0)
# Canny is used to detect edges in the image.
# The numbered arguments are threshold values for how defined edges should be.
# Higher the threshold values, lower the edge detection.
img_canny = cv2.Canny(img, 200, 400)
# dilate is used to dilate the image (also increase the thickness of the edges in case of canny picture)
# The kernel argument is a matrix of all 1's.
# Changing iterations increases/decreases the thickness of the edges
img_dilated = cv2.dilate(img_canny, kernel, iterations=1)
cv2.imshow("dilated image", img_dilated)
cv2.imshow("canny image", img_canny)
cv2.imshow("blur image", img_blur)
cv2.imshow("grey image", img_grey)
cv2.waitKey(0)
